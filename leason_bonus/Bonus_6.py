# Вирішити задачу 4 без словника за 2 строки:
# 1 строка це input
# 2 строка це рішення


www = "".join((input("Enter words - ")).split())
print(set([i+" = "+(str(www.count(i))) for i in www if i.isalpha()]))
