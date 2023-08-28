import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

import os
import sys

parpath = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))
sys.path.append(parpath)

from notAllowedCode import *

@t.test(0)
def has_priem_of_niet(test):

	notAllowed = {"list": "[", "break": "break"}
	notAllowedCode(test, lib.source(_fileName), notAllowed)

    test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "priem_of_niet")
    test.description = lambda : "definieert de functie priem_of_niet()"

@t.test(10)
def has_alle_priems(test):
    test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "alle_priems")
    test.description = lambda : "definieert de functie alle_priems()"

@t.test(20)
def has_reeks_niet_priem(test):
    test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "reeks_niet_priem")
    test.description = lambda : "definieert de functie reeks_niet_priem()"

@t.test(30)
def correctBarriers(test):
	def testMethod():
		result = lib.getLine(lib.outputOf(_fileName), 0)
		testResult = assertlib.match(result, ".*9552.*9586.*") or assertlib.match(result, ".*9586.*9552.*")
		return testResult
	test.test = testMethod

	notAllowed = {"break": "break"}
	notAllowedCode(test, lib.source(_fileName), notAllowed)

	test.description = lambda : "geeft het correcte beginpunt en eindpunt van de reeks"
	test.fail = lambda info : "let op: de priemgetallen zelf horen niet bij de reeks!"
	test.timeout = lambda : 30

@t.passed(has_priem_of_niet)
@t.test(40)
def correctDistance(test):
	test.test = lambda : assertlib.numberOnLine(35, lib.getLine(lib.outputOf(_fileName), 1))
	test.fail = lambda info : "print de correcte lengte van de reeks op de tweede regel"
	test.description = lambda : "geeft de correcte lengte van de reeks"
	test.timeout = lambda : 30
