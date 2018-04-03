
def powers(n):
    print "the first 5 powers of", n, "are", pow(n,1), pow(n,2), pow(n,3), pow(n,4), pow(n,5)

powers(7)

def average(a,b,c):
    print (a+b+c)/3

def score_summary(name,a,b,c):
    print name, ":", "max", max(a,b,c), "min", min(a,b,c), "average", average(a,b,c)

score_summary("fred",1.5,2.4,3.7)

def signature(signature):
    print "Yours sincerely"
    print signature

def reject(m):
    print "Dear", m
    print "I am sorry to inform you that you do not have the job"
    signature

def accept(p):
    print "dear", p
    print "I am please to inform you that you have the job"
    signature

reject("bob")
signature("John")

accept("amanda")
signature("amandav")

def show_first(e,f,g,h):
    print "min", min(e,f,g,h)

show_first("dog","xylophone","elephant","Elephant")
