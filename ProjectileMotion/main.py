from math import cos, sin, pi

gravity = 9.8
height = 0


# turns an angle and speed into their proportionate velocities
def cord_velocities(angle, speed):
    xvelocity = speed * cos(angle / 180 * pi)
    yvelocity = speed * sin(angle / 180 * pi)

    return yvelocity, xvelocity


# takes the y velocity and based on the strength of gravity return how long until the
# object would reach the ground
def air_time(yvelocity, gmult):
    gmult = gmult * gravity
    seconds = 2*yvelocity/gmult
    return seconds


def projectile_motion(angle, speed, gmult=1):
    xvelocity, yvelocity = cord_velocities(angle, speed)
    a = air_time(yvelocity, gmult)*xvelocity
    print(a)


projectile_motion(30, 20)

# could make his all into a single fuction but this is practice
