def remove_palindroms(spells):
    d = 0
    for i in spells:
        d += 1
        if i.lower() == i[::-1].lower():
            spells.pop(d - 1)
    return spells
