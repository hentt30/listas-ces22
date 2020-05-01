# Checar se o parâmetro é natural


def test_natural_number(func):
    def helper(x):

        if(type(x) == int and x >= 0):
            return func(x)
        else:
            raise Exception("Argumento não é um número natural")
    return helper


@test_natural_number
def fatorial(n):
    if(n == 0):
        return 1
    return n*fatorial(n-1)
