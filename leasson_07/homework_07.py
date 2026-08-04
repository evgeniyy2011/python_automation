# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    multiplier = 1

    while True:
        result = number * multiplier
        if  result > 25 or result<=0:
            break
        print (str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def plus(a,b):
    return f"{a}+{b}= {a+b}"

print(plus(2,5))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def midle_of_list(lis):
    return sum(lis)/len(lis)
print(midle_of_list([4,6,8,2,5,9,10]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def turn_around(strin):
   return strin[::-1]

print(turn_around("Hello world"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def the_longest(lis):
    res = ""
    for i in lis:
        if len(i)>len(res):
            res=i
    return res
print(the_longest(["Helloo", "world", "!!!"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


# task 7
#docstring
def unic_symbol():
    '''
    This function returning True if user entered more than 10 unic characters
     or False if less than 10 unic characters.
     link with  -----> https://lms.ithillel.ua/groups/69f1acc4f9879ecbe3a13f01/homeworks/6a50ac6dfa22625a0f26cb2c

    :return: True or False
    '''

    new_sent = len(set(input("Enter any characters ---> ")))
    return new_sent > 10
print(unic_symbol())

# task 8

#docstring
def finder_latter():

    '''
    This function sending request wille user entering any words without letter 'h' or 'H'.
    When function getting words with h or H, proces whill be complete and in console appear title "Correct"
    Condition link ----> https://lms.ithillel.ua/groups/69f1acc4f9879ecbe3a13f01/homeworks/6a50ac6dfa22625a0f26cb2d
    :return: str ---> Correct if user has done all conditions
    '''

    res = input("Enter any words include latter h or H - ")
    while 'h' not in res.lower():
        res = input("Try Again. Enter any words include latter h or H - ")
    return "Correct"
print(finder_latter())

# task 9
#docstring
def list_sep (lst:list) -> list[str]:
    '''
    Returns all string elements from the given list and skips elements of other types.
    Condition link ---> https://lms.ithillel.ua/groups/69f1acc4f9879ecbe3a13f01/lessons/6a670cad333313bba80e9914
    :param lst: A list containing elements of different types.
    :return: A list containing only string elements.
    '''
    result = []
    for i in lst:
        if type(i) is not str:
            continue
        else:
            result.append(i)
    return result

sen = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
jer = ['Jack', '1111', 55, None, 32, 'Bob']
print(list_sep(jer))

# task 10
#docstring
def car_searcher(cars:dict) -> dict:

    '''
    This function performs filtering. The search criteria are the parameters of the vehicle to be returned.
    Condition link ---> https://lms.ithillel.ua/groups/69f1acc4f9879ecbe3a13f01/homeworks/6a50ac6dfa22625a0f26cb28
    :param cars: A dictionary containing car names and their characteristics.
    :return: A dictionary containing up to five filtered cars.
    '''

    search_criteria = (2017, 1.6, 36000)
    # рік ≥, об'єм двигуна ≥, ціна ≤
    result = {}
    new_dict = {k: val for k, val in car_data.items() if
                val[1] >= search_criteria[0] and val[2] >= search_criteria[1] and val[4] <= search_criteria[2]}
    sort_cars = (sorted(new_dict.items(), key=lambda item: item[1][4]))[:5]
    for key, val in sort_cars:
        result[key]=val
    return result

car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
for k, v in car_searcher(car_data).items():
    print(k, v)


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""