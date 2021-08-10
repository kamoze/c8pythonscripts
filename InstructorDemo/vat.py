def calculate_vat(price, country):
    can = 'Canada'
    us = 'United states'
    country = country.capitalize()
    print(country)
    try:
        if country == can:
            ca = 0.13
        elif country == us:
            ca = 0.15
        else:
            ca = '0.20'
        vat = float(price) * ca
        return vat
    except TypeError:
        ca = 0.10
        vat = float(price) * ca
        return vat


print(calculate_vat(input('Provide price here:'), input('Provide Country here:')))
