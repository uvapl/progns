import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

import os
import sys

parpath = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))
sys.path.append(parpath)

from notAllowedCode import *

# toevoegingen christiaan

@t.test(0)
def has_priem_of_niet(test):

	notAllowed = {"list": "[", "break": "break"}
	notAllowedCode(test, lib.source(_fileName), notAllowed)

    test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "priem_of_niet")
    test.description = lambda : "definieert de functie priem_of_niet()"


@t.test(10)
def has_alle_priem_tot(test):
    test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "alle_priem_tot")
    test.description = lambda : "definieert de functie alle_priem_tot()"


@t.test(20)
def has_zoveelste_priem(test):
    test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "zoveelste_priem")
    test.description = lambda : "definieert de functie zoveelse_priem()"

@t.test(30)
def exact1(test):
	test.test = lambda : assertlib.numberOnLine(2, lib.getLine(lib.outputOf(_fileName, stdinArgs=[1]), 0))
	test.description = lambda : "vindt het 1ste priemgetal: 2"

@t.test(40)
def exact1000(test):
	test.test = lambda : assertlib.numberOnLine(7919, lib.getLine(lib.outputOf(_fileName, stdinArgs=[1000]), 0))
	test.description = lambda : "vindt het 1000ste priemgetal: 7919"

@t.test(50)
def exact377(test):
	test.test = lambda : assertlib.numberOnLine(2591, lib.getLine(lib.outputOf(_fileName, stdinArgs=[377]), 0))
	test.description = lambda : "vindt het 377ste priemgetal: 2591"

@t.passed(has_priem_of_niet)
@t.test(60)
def handlesWrongInput(test):
	test.test = lambda : assertlib.numberOnLine(2, lib.getLine(lib.outputOf(_fileName, stdinArgs=[-90, -1, 0, 1]), 0))
	test.description = lambda : "handelt foute input af: -90, -1, 0"


# # originele checks!
# @t.test(0)
# def exact1(test):

# 	notAllowed = {"list": "[", "break": "break"}
# 	notAllowedCode(test, lib.source(_fileName), notAllowed)

# 	test.test = lambda : assertlib.numberOnLine(2, lib.getLine(lib.outputOf(_fileName, stdinArgs=[1]), 0))
# 	test.description = lambda : "vindt het 1ste priemgetal: 2"

# @t.test(10)
# def exact1000(test):
# 	test.test = lambda : assertlib.numberOnLine(7919, lib.getLine(lib.outputOf(_fileName, stdinArgs=[1000]), 0))
# 	test.description = lambda : "vindt het 1000ste priemgetal: 7919"

# @t.test(20)
# def exact377(test):
# 	test.test = lambda : assertlib.numberOnLine(2591, lib.getLine(lib.outputOf(_fileName, stdinArgs=[377]), 0))
# 	test.description = lambda : "vindt het 377ste priemgetal: 2591"

# @t.passed(exact1)
# @t.test(30)
# def handlesWrongInput(test):
# 	test.test = lambda : assertlib.numberOnLine(2, lib.getLine(lib.outputOf(_fileName, stdinArgs=[-90, -1, 0, 1]), 0))
# 	test.description = lambda : "handelt foute input af: -90, -1, 0"

# eind originele checks

# toevoegingen christiaan

# @t.test(0)
# def hasfunctie(test):

# 	notAllowed = {"list": "[", "break": "break"}
# 	notAllowedCode(test, lib.source(_fileName), notAllowed)

#     test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "zoveelste_priem")
#     test.description = lambda : "definieert de functie zoveelse_priem()"

# @t.passed(hasfunctie)
# @t.test(10)
# def exact1(test):

#     test.test = lambda : assertlib.sameType(lib.getFunction("zoveelste_priem", _fileName)(1), 2)
#     test.description = lambda : "vindt het 1ste priemgetal: 2"

# @t.passed(hasfunctie)
# @t.test(20)
# def exact377(test):
# 	test.test = lambda : assertlib.sameType(lib.getFunction("zoveelste_priem", _fileName)(377), 2591)
# 	test.description = lambda : "vindt het 377ste priemgetal: 2591"

# @t.passed(hasfunctie)
# @t.test(30)
# def handlesWrongInput(test):

# 	test.test = lambda : assertlib.sameType(lib.getFunction("zoveelste_priem", _fileName)(-3), 0)
# 	test.description = lambda : "handelt foute input af: -3"

# @t.passed(hasfunctie)
# @t.test(40)
# def handlesWrongInput(test):

# 	test.test = lambda : assertlib.sameType(lib.getFunction("zoveelste_priem", _fileName)(0), 0)
# 	test.description = lambda : "handelt foute input af: 0"

# # eind toevoegingen christiaan
