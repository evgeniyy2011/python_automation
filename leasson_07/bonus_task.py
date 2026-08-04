def solution(grades1, grades2):
    new_dic = {}
    for i in grades1:
        if i in grades2:
            new_dic[i]= grades1[i]-grades2[i]
    return new_dic





grades_1 = {'Анна Коваленко': 92, 'Олег Петров': 85, 'Ірина Сидорова': 78, 'Свирид Свиридович': 99}
grades_2 = {'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 80}
for i, m in solution(grades_1,grades_2).items():
    print(i,m)


    # print(solution(grades_1,grades_2))