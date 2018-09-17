import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
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
def showsGraph(test):
	test.test = lambda : assertlib.fileContainsFunctionCalls(_fileName, "savefig") or assertlib.fileContainsFunctionCalls(_fileName, "show")
	test.description = lambda : "slaat een grafiek op, of laat een grafiek zien"

@t.test(1)
def givesMin(test):
	test.test = lambda : assertlib.numberOnLine(0.37, lib.getLine(lib.outputOf(_fileName), 0), deviation = 0.05) and assertlib.numberOnLine(0.69, lib.getLine(lib.outputOf(_fileName), 0), deviation = 0.05)
	test.fail = lambda info : "Zorg dat het juiste minimum op de eerste regel geprint wordt"
	test.description = lambda : "print het juiste minimum van de functies"
