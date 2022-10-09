import pytest

import exercises.variables.variables1 as variables

def test_exercise() :
    assert variables.exercise() == 5, "\n\n-> Expected value '5' but got None instead.\nChange the 'variables1.py' file at the 'exercises/variables folder'\n"
    #assert "maximum recursion" in str(excinfo.value)
    #assert variables.exercise() == 5, "\nExpected value '5' but got None instead.\nFix the 'variables1.py' file at 'exercises/variables'"
