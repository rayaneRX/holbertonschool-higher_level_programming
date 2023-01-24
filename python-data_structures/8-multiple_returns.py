#!/usr/bin/python3
def multiple_returns(sentence):
    #first_c = sentence[0]
    if sentence == "":
        #first_c = None
        return (len(sentence), None)
    else:
        return (len(sentence), sentence[0])
