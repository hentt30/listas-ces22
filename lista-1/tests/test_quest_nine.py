import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from quests.quest_nine import is_palindrome
import pytest

def test():
    assert is_palindrome("abba") == True
    assert not is_palindrome("abab") == True
    assert is_palindrome("tenet") == True
    assert not is_palindrome("banana") == True
    assert is_palindrome("straw warts") == True
    assert is_palindrome("a") == True
    assert is_palindrome("") == True
    