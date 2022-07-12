def get_average(marks):
    d = 0
    for i in marks:
        if type(i) == int or float:
            d += i
    return int(d/len(marks))