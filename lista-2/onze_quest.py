def func(*args,**kwargs):
    print(f"esses sao os argumentos passados em forma de tuple: {args}")
    print(f"esses são os arguementos passados em forma de dicionário: {kwargs}")


if __name__ == "__main__":
     func(1,2,3,4,5,first=1,second=2,third=3)
