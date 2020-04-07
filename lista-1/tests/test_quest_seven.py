import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from quests.quest_seven import sum_of_squares
import pytest

def test():
    assert sum_of_squares([2, 3, 4]) == 29
    assert sum_of_squares([ ]) == 0
    assert sum_of_squares([2, -3, 4]) == 29