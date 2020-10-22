def remove_palindroms(spells):
    c = 0
    for i in spells:
        c += 1
        if i.lower() == i[::-1].lower():
            spells.pop(c - 1)
    return spells
