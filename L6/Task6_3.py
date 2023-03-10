# Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён,
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы

# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

import os
def clear(): return os.system('cls')


clear()


def create_dict(lst):
    # преобразцем строку в список, откидывая ковычки
    lst = [i[1:-1] for i in lst.split(", ")]
    d = {}
    for i in lst:
        if i[0] not in d.keys():  # Если есть нет кулюча по первому символу слова, создаем его и вешаем на него слово
            d[i[0]] = [i]
        else:
            d[i[0]].append(i)  # Если есть, дописываем в список слово
    return dict(sorted(d.items()))


print(create_dict('"Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"'))
