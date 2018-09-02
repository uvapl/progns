import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib

import re

@t.test(0)
def anti_hardcode(test):

    output = str(lib.outputOf(_fileName)).strip()#.split()
    #output = "".join([out_word + " *\\[nt] " for out_word in output_split])
    source = lib.source(_fileName)
    source_no_comments = lib.removeComments(source)

    template = re.compile(output)
    match_found = template.search(source_no_comments)

    test.test = lambda : (True if not match_found else False)
    test.description = lambda : "No hardcoding found"
    test.fail = lambda info : "Check your code for hardcoded output"
    test.timeout = lambda : 10
