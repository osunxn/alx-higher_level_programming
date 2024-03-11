#!/usr/bin/python3

def multiple_returns(sentence):
    ntuple = ()
    if len(sentence) == 0:
        ntuple = 0, "None"
    else:
        ntuple = len(sentence), sentence[0]
    return ntuple
