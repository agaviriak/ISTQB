import sys
import math
from contextlib import redirect_stdout


def solve(weight_0, weight_1, weight_2):
    arreglo=[weight_0,weight_1,weight_2]
    maximo=max(arreglo)
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    return maximo


# Ignore and do not change the code below
def main():
    # pylint: disable = C, W

    # game loop
    while True:
        weight_0 = int(input())
        weight_1 = int(input())
        weight_2 = int(input())
        with redirect_stdout(sys.stderr):
            action = solve(weight_0, weight_1, weight_2)
        print(action)


if __name__ == "__main__":
    main()