import math

def get_sircles():
    radius = input('radius: ')
    if radius.isdigit():
        print('S =', math.pi * int(radius) ** 2)
        print('P =', math.pi * 2 * int(radius))
        print('D =', 2 * int(radius))
        print('R =', radius)
    return