import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import math
import importlib

def before():
	try:
		import matplotlib
		matplotlib.use("Agg")
		import matplotlib.pyplot as plt
		plt.switch_backend("Agg")
		lib.neutralizeFunction(plt.pause)
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
	test.test = lambda : assertlib.between(lib.getFunction("twitter", _fileName)(), 0.82, 0.83)
	test.description = lambda : "twitter geeft het juiste antwoord"
	test.timeout = lambda : 90
