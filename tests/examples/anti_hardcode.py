def test_anti_hardcode_fail():
    """ Prints the output directly """
    print("Test out-put.")

def test_anti_hardcode_pass():
    """ Prints the output with replacement """
    print("Test {0}.".format("output"))

test_anti_hardcode_fail()
#test_anti_hardcode_pass()