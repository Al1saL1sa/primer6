if __name__ == '__main__':
    x = tuple(input("Количество Гб: ").split(" "))
    y = tuple(input("Стоимость:     ").split(" "))
    z = []
    s = input("Значение s: ")
    k = 0

    for i in y:
        if (i > s):
            z.append(x[k])
        k += 1

    if k == 0:
        print("Нет винчестеров, которые стоят больше s.")
    else:
        print(z)