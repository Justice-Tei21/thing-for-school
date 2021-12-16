'''
Jag behöver mer erfarenhet
'''


def tid_tagen(N, M):
    tid = 0
    klattrat= 0
    maximalt=400000000
    if 2 <= N <= maximalt and 0 <= M <= maximalt:
        on=N
        om=M
        while klattrat < on+om:
            if M==0:
                M=N//2


            elif N > M:
                overfors = N - M
                M = M + overfors
                N = N - overfors
            klattrat = klattrat + M
            M = M - N
            N=on
            tid = tid + 10
    print(tid)
    return tid

tid_tagen(3,3)

