#задание 1

from pprint import pprint


def cookbook():
    cookbooks = {}
    with open('recipes.txt', encoding='UTF-8') as f:
      for line in f:
        dish_name = line.strip()
        count = int(f.readline())
        ingr_list = list()
        for i in range(count):
            ingr = f.readline().strip()
            ingridient = {}
            splited = ingr.split('|')
            ingridient['ingredient_name'], ingridient['quantity'], ingridient['measure'] = splited
            ingridient['quantity'] = int(ingridient['quantity'])
            ingr_list.append(ingridient)
        f.readline().strip()
        cookbooks[dish_name] = ingr_list
    return cookbooks

pprint(cookbook())

#задание 2

cook_book = cookbook()
def get_shop_list_by_dishes(dishes, person_count):
    ingredient_list = dict()
    for dish in dishes:
            for ingredient in cook_book[dish]:
                meas_list = dict()
                if ingredient['ingredient_name'] not in ingredient_list:
                    meas_list['measure'] = ingredient['measure']
                    meas_list['quantity'] = ingredient['quantity'] * person_count
                    ingredient_list[ingredient['ingredient_name']] = meas_list
                else:
                    ingredient_list[ingredient['ingredient_name']]['quantity'] = ingredient_list[ingredient['ingredient_name']]['quantity'] + ingredient['quantity'] * person_count
    return ingredient_list

pprint(get_shop_list_by_dishes(['Утка по-пекински'], 3))

#задание 3

def merge_files(list_of_names_files):
    dict_of_files = {} # ключ - имя файла, значение - количество строк
    for file in list_of_names_files:
        with open(file, mode='rt', encoding='utf8') as f:
            dict_of_files[file] = len(f.readlines())
    with open('output.txt', mode='wt') as main_f:
        data = []
        for file in sorted(dict_of_files, key=lambda key: dict_of_files[key]): # сортировка по количеству строк
            data += [file + '\n', str(dict_of_files[file]) + '\n']
            with open(file, mode='rt', encoding='utf8') as f_1:
                data += f_1.readlines()
                data.append('\n')
        del data[-1]
        main_f.writelines(data)


if __name__ == '__main__':
    num_of_files = input('Введите количество файлов:\n')
    print('Введите названия файлов:')
    list_of_name_files = []
    for i in range(int(num_of_files)):
        list_of_name_files.append(input(str(i + 1) + ' файл:\n'))
    merge_files(list_of_name_files)