import random
import time


def share_diagonal(x0, y0, x1, y1):
    """
        Verificar se duas peças compartilham a mesma diagonal
    """
    return abs(y1-y0) == abs(x1-x0)


def col_clashes(positions, col):
    """
        Checar a colisão com colunas a sua esqueda
    """
    index_newcol = len(positions)
    for index in range(col):
        if(share_diagonal(index, positions[index], col, positions[col])):
            return True
    return False


def has_clashes(positions):
    """
        Verifica se há colisões em um tabuleiro preenchido com 8 rainhas
    """
    for index, position in enumerate(positions):
        if(col_clashes(positions, index)):
            return True
    return False


def solve_chess(size):
    random_generator = random.Random()
    initial_permutation = list(range(size))
    sol_found = 0
    tries = 0
    while sol_found < 10:
        random_generator.shuffle(initial_permutation)
        tries += 1
        if not has_clashes(initial_permutation):
            print(f"Found solution {initial_permutation} in {tries} tries.")
            tries = 0
            sol_found += 1


if __name__ == "__main__":
    sizes = [4, 12, 13, 14, 15, 16]
    for size in sizes:
        print(f"############## PARA O TAMANHO {size} ##############")
        ini = time.time()
        solve_chess(size)
        end = time.time()
        print(end-ini)
        if(end-ini > 60):
            print("##################################################")
            print(f"O maior tamanho que pose ser resolvido em menos de um minuto eh {size}")
            break
