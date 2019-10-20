import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib
import helpers
import re

def sandbox():
	lib.require("DeBiltTempMaxSUMMER2019.txt", "https://www.nikhef.nl/~ivov/Python/KlimaatData/DeBiltTempMaxSUMMER2019.txt")
	lib.require("DeBiltTempMinSUMMER2019.txt", "https://www.nikhef.nl/~ivov/Python/KlimaatData/DeBiltTempMinSUMMER2019.txt")


def before():
	try:
		import matplotlib
		matplotlib.use("Agg")
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

		#Max temp
		correctAnswerMax = [37.5, 25, 2019]
		if helpers.isHardcodedIn(correctAnswerMax[0], test.fileName):
			test.success = lambda info : "let op: deze output is hardcoded. {} staat in de source code!".format(correctAnswer)

		line1 = lib.getLine(lib.outputOf(_fileName), 0)
		numbersMax = lib.getNumbersFromString(line1)

		correctMonthMax = any([assertlib.contains(line1.lower(), month) for month in ["juli", "june", "jun"]])

		#Min temp
		correctAnswerMin = [-24.7, 27, 1942]

		line2 = lib.getLine(lib.outputOf(_fileName), 1)
		numbersMin = lib.getNumbersFromString(line2)

		correctMonthMin = any([assertlib.contains(line1.lower(), month) for month in ["januari", "january", "jan"]])
	
		#Total check
		if sum(1 for n in numbersMax if n in correctAnswerMax) != 3 and correctMonthMax and sum(1 for n in numbersMin if n in correctAnswerMin) != 3 and correctMonthMin:
			return False
		return True

	test.test = testMethod
	test.description = lambda : "print hoogste en laagste temperatuur ooit met correcte datum"

@t.passed(correctHighestTemp)
@t.test(11)
def correctIjstijd(test):
	def testMethod():
		if helpers.isHardcodedIn(1947, test.fileName):
			test.success = lambda info : "let op: deze output is hardcoded. 1947 staat in de source code!"

		line1 = lib.getLine(lib.outputOf(_fileName), 2)

		correctDuration = assertlib.contains(line1, '21')

		line2 = lib.getLine(lib.outputOf(_fileName), 3)

		correctMonth = any([assertlib.contains(line2.lower(), month) for month in ["februari", "february", "feb"]])

		correctAnswer = [4, 24, 1947]
		numbers = lib.getNumbersFromString(line2)
		correctDayAndYear = sum(1 for n in numbers if n in correctAnswer) == 4
		
		return correctDuration and correctMonth and correctDayAndYear

	test.test = testMethod
	test.description = lambda : "print correcte duur en datum van de kleine ijstijd op 2 apparte regels"




@t.test(20)
def correctLowestTemp(test):
	def testMethod():

		years = [1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909, 1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

		nWarm = [93, 57, 53, 65, 79, 71, 40, 67, 41, 60, 94, 44, 57, 83, 67, 60, 92, 59, 64, 62, 103, 55, 50, 57, 62, 64, 58, 73, 83, 71, 56, 75, 91, 95, 75, 78, 69, 68, 85, 62, 66, 61, 69, 71, 82, 62, 103, 60, 92, 73, 75, 71, 74, 43, 79, 42, 55, 66, 112, 69, 62, 42, 51, 75, 44, 60, 74, 71, 91, 85, 87, 53, 81, 61, 97, 96, 64, 56, 62, 69, 63, 88, 82, 56, 75, 77, 61, 69, 103, 78, 75, 99, 66, 73, 96, 70, 91, 76, 97, 91, 89, 97, 116, 89, 88, 110, 97, 95, 94, 90, 93, 77, 82, 110, 69, 108, 105, 132]

		nZomers = [17, 11, 12, 16, 11, 10, 3, 10, 6, 8, 31, 11, 10, 17, 7, 7, 14, 9, 15, 8, 30, 10, 13, 6, 21, 9, 8, 8, 21, 16, 10, 23, 13, 15, 21, 12, 13, 11, 17, 9, 20, 14, 15, 14, 14, 9, 47, 15, 20, 12, 11, 14, 21, 9, 18, 4, 15, 15, 37, 10, 15, 4, 10, 22, 4, 14, 15, 15, 27, 24, 13, 9, 23, 7, 32, 46, 6, 13, 13, 12, 14, 32, 40, 16, 15, 21, 11, 15, 34, 32, 26, 33, 13, 30, 41, 20, 28, 17, 31, 22, 24, 18, 48, 25, 34, 51, 20, 26, 27, 27, 20, 24, 27, 23, 29, 31, 23, 55]

		nTropisch = [1, 1, 0, 2, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 1, 0, 2, 1, 1, 0, 2, 3, 5, 0, 2, 0, 0, 1, 2, 2, 0, 2, 1, 0, 0, 2, 2, 1, 1, 0, 9, 1, 0, 4, 2, 1, 8, 6, 1, 1, 0, 1, 1, 0, 2, 0, 6, 0, 4, 0, 3, 0, 0, 4, 0, 1, 3, 2, 5, 0, 0, 2, 2, 0, 8, 14, 1, 2, 0, 0, 0, 6, 7, 2, 1, 3, 0, 0, 3, 3, 4, 3, 0, 9, 11, 2, 6, 5, 3, 2, 6, 4, 11, 3, 4, 13, 1, 1, 1, 3, 2, 2, 7, 2, 5, 5, 3, 9]

		numLines = len(years)

		def lineContainsAll(line, vals):
			corr = sum([str(val) in line for val in vals])
			elems = len(vals)

			if corr == elems:
				return True
			return False

		
		check = sum([lineContainsAll(lib.getLine(lib.outputOf(_fileName), n+4), [years[n], nWarm[n], nZomers[n], nTropisch[n]]) for n in range(0, numLines)]) == numLines

		
		return check

	test.test = testMethod
	test.description = lambda : "print alle warme, zomerse en tropische dagen voor elk jaar"








@t.passed(correctLowestTemp)
@t.test(21)
def correctDateLowestTemp(test):
	def testMethod():
		correctYears = [1941, 2006, 2018]

		output = lib.outputOf(
			test.fileName,
			overwriteAttributes = [("__name__", "__main__")]
		)


		def findnLineWith(text, value):
			regex = re.compile(".*" + str(value) + ".*", re.DOTALL)
			n = 0
			for line in text.split("\n"):
				if regex.match(line):
					return n
				n += 1
			return None

		def lineContainsAll(line, vals):
			corr = sum([str(val) in line for val in vals])
			elems = len(vals)

			if corr == elems:
				return True
			return False


		startline = findnLineWith(output, "meerdere hittegolven") + 1


		check = sum([lineContainsAll(lib.getLine(lib.outputOf(_fileName), n+startline), [correctYears[n], 2]) for n in range(0, 3)]) == 3


		return check

	test.test = testMethod
	test.description = lambda : "print de jaren waar in er meerdere hittegolven plaats vonden"
