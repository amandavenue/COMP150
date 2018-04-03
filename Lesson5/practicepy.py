def any_equal(x, y, z):
    if x == y or y == z or z == x:
        print "at least two inputs are the same"
    else:
        print "No inputs match"

any_equal(1,2,3)
any_equal(1,1,2)
any_equal(1,2,1)
any_equal("ant", "ant", 3)
any_equal("ant", "ant", "ant")

def next_level(a,b,c,d,e,f):
    if a+b+c+d+e+f-min(a,b,c,d,e,f) >= 200:
        print "Pass"
    else:
        print "Repeat"

next_level(1,2,3,4,5,6)
next_level(1,2,3,4,5,186)
next_level(200,1,2,3,4,5)
