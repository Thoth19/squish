# Ok so what is it that we want to do we want to take a set of strata like differnet colors of clay
#and then stretch them out
#then fold them over
#and smush them again

#1. we need to seam carve? wait do we?
# maybe we can do the stretchin gfirst.
#2. fold this part seems maybe difficult?
#3. put a copy back on top. this seems legit.

# So first we want to first start with some shape

class pixel:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b 
    def __repr__(self):
        return "R:{} G:{} B:{}".format(self.r, self.g, self.b)

import random
def random_pixel():
    return pixel(random.randint(1,255), random.randint(1,255), random.randint(1,255))
# ok now we want to start with a nice pretty thing like
# rrrrrrrrrr
# rrrrrrrrrr
# gggggggggg
# bbbbbbbbbb
# bbbbbbbbbb

stone1 = random_pixel()
stone2 = random_pixel()
stone3 = random_pixel()
row1 = [stone1 for _ in range(5)]
row2 = [stone2 for _ in range(5)]
row3 = [stone3 for _ in range(5)]

# make sure they are copies. might need to be more clever bc the pixels are still the same
starting_rock = [row1[:], row2[:], row3[:]]

# ok now we need to stretch

def div2(x):
    # divides by 2 and rounds up
    return round(x/2 + .4)

def stretch(rock):
    # We want to take the height and reduce it by half and double the width
    # This might cause us to lose some material?
    # What if we just did it from the top?
    print(rock)
    out_rock = [[0 for _ in range(2*len(rock[0]))] for _ in range(div2(len(rock)))]
    for i, row in enumerate(rock):
        for j, pixel in enumerate(row):
            out_rock[i//2][2*j+i%2] = pixel
            print(out_rock)
    i = len(rock)
    for j, pixel in enumerate(rock[-1]):
        out_rock[i//2][2*j+i%2] = pixel
        print(out_rock)
    return out_rock

def fold(rock):
    # mostly TODO, but we can split it apart or something
    h = len(rock)
    w1 = len(rock[0])//2
    w2 = len(rock[0]) - w1
    Lrock = [[rock[r][c] for c in range(w1)] for r in range(h)]
    Rrock = [[rock[r][c+w1] for c in range(w2)] for r in range(h)]

    return Lrock, Rrock
    
