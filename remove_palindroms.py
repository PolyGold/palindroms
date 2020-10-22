def remove_palindroms(spells):
    for i in spells:
        if i.lower() == i[::-1].lower():
            spells.remove(spell)
    return spells
