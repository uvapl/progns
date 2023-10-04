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
def correctFunc1(test):
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

	def testMethod():
		import time
		s = time.time()
		res = assertlib.between(lib.getFunction("twitter", _fileName)(), 0.82, 0.83)
		print(time.time() - s)
		return res

	test.test = testMethod
	test.description = lambda : "twitter geeft het juiste antwoord"
	test.timeout = lambda : 90
