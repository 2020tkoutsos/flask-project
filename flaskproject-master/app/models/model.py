def get_tax(salary):
    #get user tax
    if salary < 20000:
        tax = 0.17 * salary
    elif salary < 100000:
        tax = 0.24 * salary
    elif salary < 200000:
        tax = 0.35 * salary
    elif salary < 400000:
        tax = 0.45 * salary
    else:
        tax = 0.5 * salary
    return tax
