import random

def coinToss():
    heads = 0
    tails = 0
    for i in range(0, 5000):
        prob = round(random.random())
        if prob == 0:
            tails += 1
            toss = "tail"
        else:
            heads += 1
            toss = "head"
        print "Tossing a coin... It's a {}! ... Got {} heads and {} tails so far".format(toss, str(heads), str(tails))
    print "After 5000 coin tosses you got {} heads and {} tails. Please find a new hobby".format(str(heads), str(tails))

coinToss()