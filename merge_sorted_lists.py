from collections import deque


if __name__ == "__main__":
    result = []
    lista = deque([1, 3, 9, 11])
    listb = deque([2, 6, 18])
    while lista or listb:
        if not lista:
            result = result + list(listb)
            listb = []
            continue
        if not listb:
            result = result + list(lista)
            lista = []
            continue
        if lista[0] > listb[0]:
            result.append(listb.popleft())
        else:
            result.append(lista.popleft())
    print result
