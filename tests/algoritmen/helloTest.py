import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def exactHello(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName), "Hallo Python\n")
	test.description = lambda : "print precies: Hallo Python"

@t.failed(exactHello)
@t.test(1)
def oneLine(test):
	test.test = lambda : assertlib.exact(len(lib.outputOf(_fileName).split("\n")), 2) and assertlib.exact(lib.getLine(lib.outputOf(_fileName), 1), "")
	test.description = lambda : "print precies één regel"
