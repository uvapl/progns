import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

import os
import sys

curPath = os.path.realpath(__file__)
fileName = os.path.basename(__file__)
folderName = "getaltheorie"
sys.path.append(curPath[:-(len(fileName) + len(folderName) + 1)])

from notAllowedCode import *

@t.test(0)
def correctBarriers(test):
	def testMethod():
		result = lib.getLine(lib.outputOf(_fileName), 0)
		testResult = assertlib.match(result, ".*9552.*9586.*") or assertlib.match(result, ".*9586.*9552.*")
		return testResult
	test.test = testMethod

	notAllowed = {"break": "break"}
	notAllowedCode(test, lib.source(_fileName), notAllowed)

	test.description = lambda : "geeft het correcte beginpunt en eindpunt van de reeks"
	test.fail = lambda info : "let op: de priemgetallen horen niet bij de reeks!"

@t.test(10)
def correctDistance(test):
	test.test = lambda : assertlib.numberOnLine(35, lib.getLine(lib.outputOf(_fileName), 1))
	test.description = lambda : "geeft de correcte lengte van de reeks"
