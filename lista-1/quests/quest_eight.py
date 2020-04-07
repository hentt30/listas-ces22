def print_list(numbers):
    for element in numbers:
        print(str(element).rjust(4),end="")
    print("")

def make_matrix():
    numbers=[i+1 for i in range(12)]
    soma = numbers
    print("       ",end="")
    print_list(numbers)
    print("  :----------------------------------------------------")
    
    for i in range(12):
        print(str(i+1).rjust(2)+ ":    ",end="")
        print_list(soma)
        soma= [sum(x) for x in zip(soma, numbers)]  

make_matrix()