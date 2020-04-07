def is_prime(number):
    isPrime = False
    if(number > 1):
        for cont in range(2,number//2):
            if(number%cont == 0):
                break
                
        else:
            isPrime = True
    return isPrime