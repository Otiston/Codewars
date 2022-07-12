def diamond(n):
    dia = []
    final = ''
    i = 0
    if not n or n < 0 or n%2 == 0:
        return None
    elif n == 1:
        return "*\n"
    else:
        while i+1 <= int(n/2):
            dia.append(' '*(int(n/2)-i)+'*'*(i*2+1)+"\n")
            i += 1
        final += ''.join(dia)+'*'*n+'\n'+''.join(''.join(list(reversed(dia))))
    return final