def licz(czescRzeczywista, czescUrojona, potega):
    modul = round((czescRzeczywista ** 2 + czescUrojona ** 2) ** (1 / 2), 2)
    cos = czescRzeczywista / modul
    sin = czescUrojona / modul
    if cos < 0:
        if sin < 0:
            pass
        else:
            pass

    else:
        if sin < 0:
            pass
        else:
            pass

    return modul


print(licz(1, 9**(1/2), 2))
