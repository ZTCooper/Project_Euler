# -*- coding: UTF-8 -*-
# 模拟竖式除法，余数之前出现过则为循环节


def divide(a, b):
    quotient = []
    remainder = []
    quotient.append(divmod(a, b)[0])
    remainder.append(divmod(a, b)[1])
    while remainder[-1] * 10 % b not in remainder:
        quotient.append(divmod(remainder[-1] * 10, b)[0])
        remainder.append(divmod(remainder[-1] * 10, b)[1])

    if remainder[-1] * 10 % b in remainder:
        quotient.append(divmod(remainder[-1] * 10, b)[0])
        remainder.append(divmod(remainder[-1] * 10, b)[1])
        circular = quotient[remainder[1:].index(
        remainder[-1] * 10 % b) + 1:]
    return len(circular)


def main():
    maxLen = 0
    for d in range(1,1001):
        newLen = divide(1, d)
        if newLen > maxLen:
            maxLen = newLen
            maxD = d
    print(maxD)

if __name__ == '__main__':
    main()
