import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib
import helpers
import re

def sandbox():
	lib.require("DeBiltTempMaxSUMMER2023.txt", "https://www.nikhef.nl/~ivov/Python/KlimaatData/DeBiltTempMaxSUMMER2023.txt")
	lib.require("DeBiltTempMinSUMMER2023.txt", "https://www.nikhef.nl/~ivov/Python/KlimaatData/DeBiltTempMinSUMMER2023.txt")


def before():
	try:
		import warnings
		warnings.filterwarnings("ignore")
		import matplotlib
		matplotlib.use("Agg")
		matplotlib.use = lambda x, warn=None, force=None: x
		import matplotlib.pyplot as plt
		plt.switch_backend("Agg")
		lib.neutralizeFunction(plt.pause)
		lib.neutralizeFunction(plt.subplot)
		lib.neutralizeFunction(plt.show)
		# lib.neutralizeFunction(matplotlib.use)
	except ImportError:
		pass

def after():
	try:
		# import matplotlib
		import matplotlib.pyplot as plt
		# plt.switch_backend("TkAgg")
		# importlib.reload(matplotlib)
		importlib.reload(plt)
	except ImportError:
		pass

# Thanks to Vera Schild!

@t.test(10)
def correctHighestTemp(test):
	def testMethod():

		# Max temp
		correctAnswerMax = [37.5, 25, 2019]
		if helpers.isHardcodedIn(correctAnswerMax[0], test.fileName):
			test.success = lambda info : "let op: deze output is hardcoded. {} staat in de source code!".format(correctAnswerMax)

		line1 = lib.getLine(lib.outputOf(_fileName), 0)
		numbersMax = lib.getNumbersFromString(line1)

		correctMonthMax = any([assertlib.contains(line1.lower(), month) for month in ["juli", "July", "jul", "Jul"]])

		# Min temp
		correctAnswerMin = [-24.7, 27, 1942]

		line2 = lib.getLine(lib.outputOf(_fileName), 1)
		numbersMin = lib.getNumbersFromString(line2)

		correctMonthMin = any([assertlib.contains(line2.lower(), month) for month in ["januari", "January", "jan", "Jan"]])
	
		# Total check
		if sum(1 for n in numbersMax if n in correctAnswerMax) != 3 or not correctMonthMax or sum(1 for n in numbersMin if n in correctAnswerMin) != 3 or not correctMonthMin:
			return False
		return True

	test.test = testMethod
	test.description = lambda : "print hoogste en laagste temperatuur ooit met correcte datum"

@t.passed(correctHighestTemp)
@t.test(11)
def correctIjstijd(test):
	def testMethod():
		if helpers.isHardcodedIn(1947, test.fileName):
			test.success = lambda info : "let op: deze output is gehardcode. 1947 staat in de source code!"

		correctAnswerIceAge = [21, 24, 1947]

		line3 = lib.getLine(lib.outputOf(_fileName), 2)
		numbersIceAge = lib.getNumbersFromString(line3)

		correctMonthIceAge = any([assertlib.contains(line3.lower(), month) for month in ["februari", "February", "feb", "Feb"]])
	
		# Total check
		if sum(1 for n in numbersIceAge if n in correctAnswerIceAge) != 3 or not correctMonthIceAge:
			return False
		return True

	test.test = testMethod
	test.description = lambda : "print correcte duur en einddatum (dag, maand en jaar) van de kleine ijstijd"

@t.passed(correctIjstijd)
@t.test(21)
def correctDateLowestTemp(test):
	def testMethod():
		correctYear = 1911

		line = lib.getLine(lib.outputOf(_fileName), 3)
		numbers = lib.getNumbersFromString(line)

		check = correctYear in numbers

		return check

	test.test = testMethod
	test.description = lambda : "print het eerste jaar waarin een hittegolf voorkwam"
