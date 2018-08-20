import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib


#def before():
#	import matplotlib.pyplot as plt
#	plt.switch_backend("Agg")
#	lib.neutralizeFunction(plt.pause)

#def after():
#	import matplotlib.pyplot as plt
#	plt.switch_backend("TkAgg")
#	reload(plt)

twoArguments = False

@t.test(0)
def hasworp_met_twee_dobbelstenen(test):
	test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "worp_met_twee_dobbelstenen")
	test.description = lambda : "definieert de functie worp_met_twee_dobbelstenen"
	test.timeout = lambda : 60


@t.passed(hasworp_met_twee_dobbelstenen)
@t.test(10)
def correctDice(test):
	test.test = lambda : assertlib.between(lib.getFunction("worp_met_twee_dobbelstenen", _fileName)(), 2, 12)
	test.description = lambda : "returnt een correcte waarde voor een worp van twee dobbelstenen"
	test.timeout = lambda : 60


@t.passed(correctDice)
@t.test(20)
def hassimuleer_potjeAndsimuleer_groot_aantal_potjes_Monopoly(test):

	def testMethod():
		test_potje = assertlib.fileContainsFunctionDefinitions(_fileName, "simuleer_potje_Monopoly")
		test_groot_aantal_potjes = assertlib.fileContainsFunctionDefinitions(_fileName, "simuleer_groot_aantal_potjes_Monopoly")
		info = ""
		if not test_potje:
			info = "de functie simuleer_potje_Monopoly is nog niet gedefinieerd"
		elif not test_groot_aantal_potjes:
			info = "de functie simuleer_potje_Monopoly is gedefinieerd :) \n  - de functie simuleer_groot_aantal_potjes_Monopoly nog niet"
		return test_potje and test_groot_aantal_potjes, info

	test.test = lambda : testMethod()
	test.description = lambda : "definieert de functie simuleer_potje_Monopoly en simuleer_groot_aantal_potjes_Monopoly"
	test.timeout = lambda : 60


@t.passed(hassimuleer_potjeAndsimuleer_groot_aantal_potjes_Monopoly)
@t.test(30)
def correctAverageTrump(test):

	def try_run():
		try:
			#Trump test
			test.description = lambda : "The function takes one argument, now try with 2."
			testInput = lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(1000)
			test.success = lambda info : "De code werkt zonder startgeld, je kunt nu startgeld invoeren!"
			if assertlib.sameType(lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(10000), None):
				test.fail = lambda info : "Zorg er voor dat de functie simuleer_groot_aantal_potjes_Monopoly het gemiddeld aan benodigde worpen returnt en ook alleen deze waarde returnt"
			return testInput
		except:
			pass
		
		try:
			#Startingmoney test
			test.description = lambda : "Good job! Both arguments."
			testInput = lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(1000, 1000000)
			if assertlib.sameType(lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(10000, 1000000), None):
				test.fail = lambda info : "Zorg er voor dat de functie simuleer_groot_aantal_potjes_Monopoly het gemiddeld aan benodigde worpen returnt en ook alleen deze waarde returnt"
			twoArguments = True
			return testInput
		
		except:
			#total fail
			return 0

	test.fail = lambda info : "Zorg dat de functie simuleer_groot_aantal_potjes_Monopoly als argument het aantal potjes heeft"
	test.test = lambda : assertlib.between(try_run(), 145, 149)
	test.description = lambda : "---"
	test.timeout = lambda : 120


@t.passed(correctAverageTrump)
@t.test(40)
def correctAverageStartgeld(test):

	def try_run():
		if not twoArguments:
			return 0

		else:
			val = lib.getFunction("simuleer_groot_aantal_potjes_Monopoly", _fileName)(10000, 1500)
			return val

	test.fail = lambda info : "Does the function accept two arguments? Answer should be ~187."
	test.test = lambda : assertlib.between(try_run(), 184, 189)
	test.description = lambda : "Monopoly werkt met 1500 euro startgeld"
	test.timeout = lambda : 60

