import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def exactHello(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName), "Hallo Python\n")
	test.description = lambda : "print precies: Hallo Python"
