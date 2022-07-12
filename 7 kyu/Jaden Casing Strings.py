def to_jaden_case(string):
    c = []
    for b in string.split(): 
        c.append(b.capitalize())
    return ' '.join(c)