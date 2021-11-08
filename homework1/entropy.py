import numpy as np


def __entropy_internal(val):
    if val == 0:
        return 0
    elif val > 1:
        raise ValueError("Probability over 1")
    elif val < 0:
        raise ValueError("Probability less than 0")
    else:
        return -val * np.log2(val)


def entropy(data):
    res = 0
    for i in data:
        res += __entropy_internal(i)
    return res


def main():
    raw_data = input("Insert values: ")
    data = list(map(float, raw_data.split(" ")))
    print(data)
    print(entropy(data))


if __name__ == "__main__":
    main()

