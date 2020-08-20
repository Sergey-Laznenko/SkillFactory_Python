"""
dict_to_sort = {"Петя": 23, "Вася": 40, "Лена": 14, "Катя": 22}
list_dict = sorted(list(dict_to_sort.values()))
print(list_dict)
for i in dict_to_sort:
    print(i)
"""

dict_to_sort = {"Петя": 23, "Вася": 40, "Лена": 14, "Катя": 22}
list_dict = sorted(list(dict_to_sort.items()),key=lambda i: i[1])
for i in list_dict:
    print(i[0], ':', i[1], end=' ')






"""
s = ''
for i in list_d:
    s += i[0] + ' : '+ str(i[1]) +' '
print(s)
"""