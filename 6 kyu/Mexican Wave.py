def wave(people):
    wa = []
    for i in range(len(people)):
        j = list(people)
        j[i] = people[i].upper()
        if people[i] != ' ':
            wa.append(''.join(j))
    return wa