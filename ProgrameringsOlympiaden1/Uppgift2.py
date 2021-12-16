#vad gör jag

def arabiska():
    vokaler= set('aeiouy')
    konsonanter= not vokaler
    string = 'leende'
    plats = 0
    string = string[::-1]
    newstring = ''
    length= len(string)
    for i in string:

        if i in vokaler:
            try:
                if string[plats+1]not in vokaler and string[plats+2] not in vokaler:
                    pass
            except IndexError:
                if string[plats + 1] not in vokaler:
                    newstring = newstring + i

            else:
                newstring = newstring + i
        else:
            newstring= newstring+i
        plats += 1

    string=string.split(' ')

    print('antal ord '+str(len(string)))
    print(string)
    print(newstring)

arabiska()
