from math import sin, cos


def Distance(angle,speed, gmult=1):
    gravity = 9.8 * gmult
    t = 2 * speed * sin(angle) / gravity
    print(t*speed * cos(angle))


Distance(30,10 )