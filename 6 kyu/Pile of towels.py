def sort_the_pile(pile, used):
    for i in used:
        t = pile[(len(pile))-i:]
        pile = pile[:len(pile)-i]
        pile.extend(sorted(t,reverse=True))
    return pile