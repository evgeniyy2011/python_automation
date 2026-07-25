
new_sent = str(input("Enter any characters - "))
sentence = ''
for i in new_sent:
    if i not in sentence:
        sentence+=i
if len(sentence) > 10:
    print(True)
else:
    print(False)



