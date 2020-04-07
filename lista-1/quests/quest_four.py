def sum_list(numbers):
    first = True
    soma = 0
    for element in numbers:
        if((not (element & 1)) and first):
            first = False
            continue
        soma += element
    return soma


