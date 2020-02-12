recipes = {'Бутерброд с ветчиной': {'Хлеб': 50, 'Ветчина': 20, 'Сыр': 20},
           'Салат Витаминный': {'Помидоры': 50, 'Огурцы': 20, 'Лук': 20, 'Майонез': 50, 'Зелень': 20}}

store = {'Хлеб': 250, 'Ветчина': 120, 'Сыр': 120,
         'Помидоры': 50, 'Огурцы': 20, 'Лук': 20,
         'Майонез': 50, 'Зелень': 20}

def check_portions(food, count, recipes=recipes, store=store):
    if food not in recipes or not set(recipes[food].keys()) <= set(store.keys()):
        return (0, 0)
    number = min([store[name] // recipes[food][name] for name in recipes[food].keys()])
    if count <= number:
        return (1, count)
    return (0, number)