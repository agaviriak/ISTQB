import sys
import traceback

try:
    assert True
    assert 7 == 7
    assert 1 == 2
    # many more statements like this
except: #AssertionError:
    _, _, tb = sys.exc_info()
    traceback.print_tb(tb) # Fixed format
    tb_info = traceback.extract_tb(tb)
    filename, line, func, text = tb_info[-1]

    print('An error occurred on line {} in statement {}'.format(line, text))
    #exit(1)