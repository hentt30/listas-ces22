import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from quests.quest_six import is_prime
import pytest

def test():
    assert is_prime(11) == True
    assert not is_prime(35) == True
    assert is_prime(19911121) == True
