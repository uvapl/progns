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
		lib.neutralizeFunction(matplotlib.use)
		lib.neutralizeFunction(plt.pause)
		lib.neutralizeFunction(plt.plot)
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
def hasRiemann(test):
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

	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "riemann")
	test.description = lambda : "definieert de functie riemann()"
	test.timeout = lambda : 90

@t.passed(hasRiemann)
@t.test(1)
def correctFunc1(test):
	test.test = lambda : assertlib.between(float(lib.getFunction("riemann", _fileName)(lambda x : x**(x + 0.5), 0, 1, 10000)), 0.52, 0.53)
	test.description = lambda : "riemann werkt correct voor een simpele functie"
	test.timeout = lambda : 90

@t.passed(hasRiemann)
@t.test(2)
def correctFunc2(test):
	test.test = lambda : assertlib.between(float(lib.getFunction("riemann", _fileName)(lambda x : math.tan(math.cos(math.sin(x))), 0.2, 2.2, 10000)), 1.70, 1.71)
	test.description = lambda : "riemann werkt correct wanneer het beginpunt niet gelijk is aan 0"
	test.timeout = lambda : 90

@t.passed(hasRiemann)
@t.test(3)
def correctFunc3(test):
	test.test = lambda : assertlib.between(float(lib.getFunction("riemann", _fileName)(lambda x : math.sin(x**2), 0, math.pi, 10000)), 0.77, 0.78)
	test.description = lambda : "riemann werkt correct voor een functie die onder de x-as komt"
	test.timeout = lambda : 90
