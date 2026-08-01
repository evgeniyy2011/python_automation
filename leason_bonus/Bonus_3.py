# Є список ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
# Вивести ТІЛЬКИ коректні імена(тобто стрінги).
# Використовувати Continue.

sen = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
result = []
for i in sen:
    if type(i) is not str:
        continue
    else:
        result.append(i)
print(result)
