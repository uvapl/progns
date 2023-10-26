import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib
import importlib

import re

from checkpy import *

include("autorit.py")
download("AutoRitData.csv", "http://www.nikhef.nl/~ivov/Python/SensorData/AutoRitData.csv")

def before():
    try:
        import warnings
        warnings.filterwarnings("ignore")
        import matplotlib
        matplotlib.use("Agg")
        matplotlib.use = lambda x, warn=None, force=None: x
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
        import matplotlib.pyplot as plt
        # plt.switch_backend("TkAgg")
        importlib.reload(plt)
    except ImportError:
        pass

# @t.test(10)
# TODO this test is not registered because it would change the # of tests used for assigning points
def checkDatafile(test):
    """bestand is in orde"""
    global _fileName

    with open(_fileName, 'r') as f:
        file_contents = f.read()

    new_file_contents = re.sub(r'with\s+open\s*\(\s*[\'"][^\'"]*[\'"]', 'with open("AutoRitData.csv"', file_contents)
    
    tempfile = f"_{_fileName}.tmp"
    with open(tempfile, 'w') as f:
        f.write(new_file_contents)

    _fileName = tempfile
    
    return True

@t.test(20)
def correctDistance(test):
    checkDatafile(test)

    def testMethod():
        output = lib.outputOf(
            _fileName,
            overwriteAttributes = [("__name__", "__main__")]
        )
        line = lib.getLine(output, 0)
        correctKm = assertlib.numberOnLine(10.86, line, deviation = 0.02)
        correctM = assertlib.numberOnLine(10860, line, deviation = 20)
        return correctKm or correctM
    test.test = testMethod
    test.description = lambda : "print de afgelegde afstand"

@t.test(30)
def showsGraph(test):
    test.test = lambda : assertlib.fileContainsFunctionCalls(_fileName, "savefig") or assertlib.fileContainsFunctionCalls(_fileName, "show")
    test.description = lambda : "slaat een grafiek op, of laat een grafiek zien"
