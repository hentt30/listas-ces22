import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from quests.quest_five import count_sam
import pytest

def test():
    assert count_sam(["sam","h","g","d","t"]) == 1
    assert count_sam(["sam","sam","sam","sam"]) == 1
    assert count_sam(["f","d","sam"]) == 3
    assert count_sam(["s","d","d","l","sama","sss"]) == 6
    