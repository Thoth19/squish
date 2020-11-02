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
row1 = [stone1 for _ in range(9)]
row2 = [stone2 for _ in range(9)]
row3 = [stone3 for _ in range(9)]
row4 = [stone3 for _ in range(9)]

# make sure they are copies. might need to be more clever bc the pixels are still the same
starting_rock = [row1[:], row1[:], row2[:], row4[:], row2[:], row3[:], row3[:]]
#starting_rock = [row1, row2, row3]

# ok now we need to stretch

def div2(x):
    # divides by 2 and rounds up
    return round(x/2 + .4)

def stretch(rock):
    # We want to take the height and reduce it by half and double the width
    # This might cause us to lose some material?
    # What if we just did it from the top?
    # the bottom row might end up as itself twice over
    #print(rock)
    out_rock = [[0 for _ in range(2*len(rock[0]))] for _ in range(div2(len(rock)))]
    for i, row in enumerate(rock):
        for j, pixel in enumerate(row):
            out_rock[i//2][2*j+i%2] = pixel
            #print(out_rock)
    i = len(rock)
    if i%2 == 1:
        for j, pixel in enumerate(rock[-1]):
            out_rock[i//2][2*j+i%2] = pixel
            #print(out_rock)
    return out_rock

def fold(rock):
    # mostly TODO, but we can split it apart or something
    # right rock can end up being larger by at most one col
    h = len(rock)
    w1 = len(rock[0])//2
    w2 = len(rock[0]) - w1
    Lrock = [[rock[r][c] for c in range(w1)] for r in range(h)]
    Rrock = [[rock[r][c+w1] for c in range(w2)] for r in range(h)]

    return Lrock, Rrock

def squish(r1, r2):
    
    # we might have to add an extra col if they aren't lined up
    if len(r1[0]) < len(r2[0]):
        for i, row in enumerate(r1):
            row.append(row[-1])
            r1[i] = row
    
    out_rock = r2[:] + r1[:]
    return out_rock
    
# now we need to make it so that we can actually visualize this
from tkinter import *
root = Tk()
def rgb_to_color(r,g,b):
    """ Takes three integers from 0-255 and transforms them into
    a #XXYYZZ color string. """
    color = "#"
    # print r,g,b
    # print hex(r),hex(g),hex(b)
    r,g,b = int(r), int(g), int(b)
    if len(hex(r)[2:]) != 2:
        color += '0'
    color += hex(r)[2:]
    if len(hex(g)[2:]) != 2:
        color += '0'
    color += hex(g)[2:]
    if len(hex(b)[2:]) != 2:
        color += '0'
    color += hex(b)[2:]
    # print color
    return color
height = 200
width = 400
root.geometry(str(width) + 'x' + str(height))
canvas = Canvas(root, width=width, height=height)
canvas.pack()

item_list = []
def render(rock, scale=20, item_list=item_list, x_push=0):
    if not(x_push):
        for item in item_list:
            canvas.delete(item)
    for i,row in enumerate(rock):
        for j, pixel in enumerate(row):
            item = canvas.create_rectangle(scale*j + scale*x_push, scale*i, scale*j + scale + x_push*scale,scale*i + scale,
                        fill=rgb_to_color(pixel.r, pixel.g, pixel.b))
            item_list.append(item)
    canvas.update()

import time
def metamorph(rock):
    render(rock)
    time.sleep(3)

    stretch_rock = stretch(rock)
    render(stretch_rock)
    time.sleep(3)

    l, r = fold(stretch_rock)
    render(l)
    render(r, x_push=len(l[0])+1)
    time.sleep(2)

    new_rock = squish(l, r)
    render(new_rock)
    return new_rock

def inf_met():
    r = starting_rock
    while True:
        r = metamorph(r)
