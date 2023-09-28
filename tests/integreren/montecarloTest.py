import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import math
import importlib

import warnings
warnings.filterwarnings("ignore")

def before():
	try:
		import matplotlib
		matplotlib.use("Agg")
		import matplotlib.pyplot as plt
		plt.switch_backend("Agg")
		lib.neutralizeFunction(plt.pause)
		lib.neutralizeFunction(matplotlib.use)
	except ImportError:
		pass

def after():
	try:
		import matplotlib.pyplot as plt
		plt.switch_backend("TkAgg")
		importlib.reload(plt)
	except ImportError:
		pass


@t.test(0)
def hasMontecarlo(test):
	# v---- Filter global code from source file -----

	global _originalFileName
	global _fileName

	_originalFileName = _fileName

	with open(_fileName, 'r') as f:
		tempfile = f"_{_fileName}.tmp"
		file_contents = f.readlines()
		
	with open(tempfile, 'w') as f:
		state = 0
		for line in file_contents:
			if state == 0:
				if line.startswith('def '):
					state = 1
				f.write(line)
			elif state == 1:
				if not (line.strip() == '' or line.startswith(' ') or line.startswith("\t") or line.startswith("def ") or line.startswith("#")):
					state = 2
					continue
				f.write(line)
			elif state == 2:
				if line.startswith('def '):
					f.write(line)
					state = 1

	_fileName = tempfile

	# ^---- Filter global code from source file -----

	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "montecarlo")
	test.description = lambda : "definieert de functie montecarlo()"
	test.timeout = lambda : 90

@t.passed(hasMontecarlo)
@t.test(1)
def correctFunc1(test):
	def testMethod():
		montecarlo = lib.getFunction("montecarlo", _fileName)
		power = lib.documentFunction(lambda x : x**(x + 0.5), "f(x) = x**(x + 0.5)")
		outcome = montecarlo(power, 0, 0, 1, 1)
		return assertlib.between(outcome, 0.51, 0.54)

	test.test = testMethod
	test.description = lambda : "montecarlo werkt correct voor een simpele functie"
	test.timeout = lambda : 90

@t.passed(hasMontecarlo)
@t.test(2)
def correctFunc2(test):
	def testMethod():
		montecarlo = lib.getFunction("montecarlo", _fileName)
		tanCosSin = lib.documentFunction(lambda x : math.tan(math.cos(math.sin(x))), "f(x) = tan(cos(sin(x)))")
		outcome = montecarlo(tanCosSin, 0.2, 0, 2.2, 1.5)
		return assertlib.between(outcome, 1.69, 1.73)

	test.test = testMethod
	test.description = lambda : "montecarlo werkt correct wanneer het beginpunt niet gelijk is aan 0"
	test.timeout = lambda : 90

@t.passed(hasMontecarlo)
@t.test(3)
def correctFunc3(test):
	def testMethod():
		montecarlo = lib.getFunction("montecarlo", _fileName)
		sin_squared = lib.documentFunction(lambda x : math.sin(x**2), "f(x) = sin(x**2)")
		outcome = montecarlo(sin_squared, 0, -1, math.pi, 1)
		return assertlib.between(outcome, 0.75, 0.79)

	test.test = testMethod
	test.description = lambda : "montecarlo werkt correct voor een functie die onder de x-as komt"
	test.timeout = lambda : 90
