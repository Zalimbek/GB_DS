#  Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
#  Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
#  номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
#  Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

items = []
i=1

while input("Добавить товар? Введите y или n: ") == 'y':
    number = i
    i += 1
    features = {}
    while input("Добавить характеристику? Введите y или n: ") == 'y':
        feature_key = input("Введите название параметра: ")
        feature_value = input("Введите значение параметра: ")
        features[feature_key] = feature_value
    items.append(tuple([number, features]))
print(items)

summary = {}
for item in items:
    for feature_key, feature_value in item[1].items():
        if feature_key in summary:
            summary[feature_key].append(feature_value)
        else:
         summary[feature_key] = [feature_value]
print(summary)
