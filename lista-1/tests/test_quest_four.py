import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from quests.quest_four import sum_list
import pytest

def test():
    assert sum_list([1,2,3,4,5,6,7,8,9,10]) == 53
    assert sum_list([1,1,1,1,1,1,1,1,1,1]) == 10
    assert sum_list([2,2,2,2,2,2,2,2,2,2]) == 18
    assert sum_list([1,1,1,1,1,1,1,1,1,2]) == 9
    