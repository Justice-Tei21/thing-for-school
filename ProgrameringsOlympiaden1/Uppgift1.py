'''
jag kommer tilbaka senare
'''

from math import sqrt

C4= 0.229*0.324
A3=0.297*0.420
A4=0.210*0.297




def Totala_vikten(kuvert_vikt,affisch_vikt,blad_vikt):
    kuvert = C4
    afischer = A3
    informationsblad = A4

    kuvert_vikt= kuvert*kuvert_vikt
    affisch_vikt=afischer*affisch_vikt
    blad_vikt=informationsblad*blad_vikt

    Helavikten=(2*kuvert_vikt+2*affisch_vikt+blad_vikt)
    print(round(Helavikten,5))


Totala_vikten(120,90,70)


