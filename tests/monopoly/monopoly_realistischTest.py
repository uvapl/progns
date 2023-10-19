import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib

import os
import sys

parpath = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))
sys.path.append(parpath)

from notAllowedCode import *


def before():
    import matplotlib.pyplot as plt
    plt.switch_backend("Agg")
    lib.neutralizeFunction(plt.pause)
    lib.neutralizeFunction(plt.show)

def after():
    import matplotlib.pyplot as plt
    plt.switch_backend("TkAgg")
    importlib.reload(plt)

@t.test(0)
def hassimuleer_groot_aantal_potjes_Monopoly(test):

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
		correctFunction = False

		if assertlib.fileContainsFunctionDefinitions(_fileName, "simuleer_groot_aantal_potjes_monopoly"):
			nArguments = len(lib.getFunction("simuleer_groot_aantal_potjes_monopoly", _fileName).arguments)

			if nArguments == 3:
				correctFunction = True
		return correctFunction

	notAllowed = {"break": "break"}
	notAllowedCode(test, lib.source(_fileName), notAllowed)

	test.test = testMethod
	test.fail = lambda info : "zorg dat de functie drie argumenten heeft, het aantal potjes, startgeld voor speler 1 en startgeld voor speler 2"
	test.description = lambda : "definieert de functie simuleer_potje_monopoly en simuleer_groot_aantal_potjes_monopoly met drie argumenten"
	test.timeout = lambda : 90


@t.passed(hassimuleer_groot_aantal_potjes_Monopoly)
@t.test(10)
def correctAverageDiv(test):
	def testMethod():
		outcome = lib.getFunction("simuleer_groot_aantal_potjes_monopoly", _fileName)(2000, 1500, 1500)
		if assertlib.sameType(outcome, None):
			info = "zorg er voor dat de functie simuleer_groot_aantal_potjes_monopoly het verschil in het bezit van straten returnt en alleen deze waarde returnt"
		elif assertlib.between(outcome, -99999999, 0):
			info = "als speler 1 meer straten heeft dan speler 2 is het verschil positief"
		else:
			info = "het verschil is niet erg groot, gemiddeld zelfs minder dan 1 straat"
		return assertlib.between(outcome, .15, .45), info

	test.test = testMethod
	test.description = lambda : "monopoly met twee spelers geeft het correcte gemiddelde verschil in gekochte straten"
	test.timeout = lambda : 90



@t.passed(correctAverageDiv)
@t.test(20)
def correctAverageDiv2(test):
	def testMethod():
		def findline(outputOf):
			tsts = ['startgeld', 'evenveel', 'straten']
			for line in outputOf.split("\n"):
				if all([assertlib.contains(line, tst) for tst in tsts]):
					return line
			return ""

		line = findline(lib.outputOf(_originalFileName))

		info = ""
		if assertlib.numberOnLine(75, line):
			info = "de gevonden waarde is 75 euro--checkpy het programma nog een keer"

		return assertlib.numberOnLine(125, line), info

	test.test = testMethod
	test.description = lambda : "monopoly met twee spelers vindt het correcte extra startgeld voor speler 2"
	test.timeout = lambda : 90
