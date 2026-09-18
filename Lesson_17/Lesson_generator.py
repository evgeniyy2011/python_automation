def generator_list_of_numbers(numbers:int):
    for numb in range(numbers+1):
        if numb%2 == 0:
            yield numb

n = generator_list_of_numbers(21)
for i in n:
    print(i)
