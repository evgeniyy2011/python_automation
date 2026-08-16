
def suma(a):
    res = []
    counter = 0
    result = []
    numbers = 0
    for i in a:
        res.append(i.split(","))
    while counter< len(a):
        try:
            for i in res[counter]:
                numbers+=int(i)
            result.append(numbers)
        except ValueError:  # Перехоплення помилки
            result.append("Не можу це зробити!")
        numbers = 0
        counter+=1
    print(result)

li = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
suma(li)