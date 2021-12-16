'''
Jag borde ha pluggat mer
'''

letters='ABCDEFGHI'
numbers='123456789'



def mala(N):

    floor=[]
    columns=[]

    if 1<=N<=9:
        rows=-1
        for i1 in range(N):
            columns.insert(0,'.')

        for i2 in range(N):
            floor.insert(0,columns)

        dictionary = {numbers[0]: floor[0]
            ,numbers[1]: floor[1]
            ,numbers[2]: floor[2]
            ,numbers[3]: floor[3]
            ,numbers[4]: floor[4]
            ,numbers[5]: floor[5]
            ,numbers[6]: floor[6]
            ,numbers[7]: floor[7]
            ,numbers[8]: floor[8]
            ,numbers[9]: floor[9]



                      }






        for i in range(N):
            floor[i][2]='B'












        for i3 in floor:
            print(floor[rows])
            rows +=rows+1
mala(7)