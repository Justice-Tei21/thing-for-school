import time
file = open('shake.txt', 'r').read()


def timed_output(s):

    for a in s:
        time.sleep(0.3)
        print(a, end='')


timed_output(file)
