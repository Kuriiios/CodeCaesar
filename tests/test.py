import os
import sys
from app.components.code_caesar import code_caesar 
'''

sys.path.insert(0,
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__),
                        ".."
                    ) ))

'''

def test_code_caesar():
    assert code_caesar('When my time comes, Keep me in your memory', 10) == 'Grox wi dswo mywoc, Uooz wo sx iyeb wowybi'