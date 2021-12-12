def move(frm, to):
    print("Move disc from {} to {}!".format(frm, to))

def recur(n, f, h, t):
    if n == 0:
        pass
    else :
        recur(n-1,f, t, h)
        move(f,t)
        recur(n-1,h,f,t)

recur(4,"A","B","C")
