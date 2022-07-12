import operator
ops = { "+": operator.add, "-": operator.sub,"/" : operator.div, "*": operator.mul }
def zero(*arg): 
    if not arg:
        return 0
    else:
        return ops[list(list(arg)[0])[0]](0,list(list(arg)[0])[1])
def one(*arg): 
    if not arg:
        return 1
    else:
        return ops[list(list(arg)[0])[0]](1,list(list(arg)[0])[1])
def two(*arg):
    if not arg:
        return 2
    else:
        return ops[list(list(arg)[0])[0]](2,list(list(arg)[0])[1])
def three(*arg):
    if not arg:
        return 3
    else:
        return ops[list(list(arg)[0])[0]](3,list(list(arg)[0])[1])
def four(*arg): 
    if not arg:
        return 4
    else:
        return ops[list(list(arg)[0])[0]](4,list(list(arg)[0])[1])
def five(*arg): 
    if not arg:
        return 5
    else:
        return ops[list(list(arg)[0])[0]](5,list(list(arg)[0])[1])
def six(*arg):
    if not arg:
        return 6
    else:
        return ops[list(list(arg)[0])[0]](6,list(list(arg)[0])[1])
def seven(*arg): 
    if not arg:
        return 7
    else:
        return ops[list(list(arg)[0])[0]](7,list(list(arg)[0])[1])
def eight(*arg):
    if not arg:
        return 8
    else:
        return ops[list(list(arg)[0])[0]](8,list(list(arg)[0])[1])
def nine(*arg):
    if not arg:
        return 9
    else:
        return ops[list(list(arg)[0])[0]](9,list(list(arg)[0])[1])

def plus(a): return '+',a
def minus(a): return '-',a
def times(a): return '*',a
def divided_by(a): return '/',a