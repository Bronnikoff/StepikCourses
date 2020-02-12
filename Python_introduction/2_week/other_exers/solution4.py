from collections import namedtuple
from collections import defaultdict
from functools import wraps

statistics = defaultdict(list)
Order = namedtuple('Order', ['success', 'portions'])

def collect_statistics(statistics):
    def decor(func):
        @wraps(func)
        def wrapped(food, count, recipes=recipes, store=store):
            ans = func(food, count, recipes, store)
            if food in statistics:
                statistics[food].append(Order(ans[0], count if ans[0] else count - ans[1]))
            else:
                statistics[food] = [Order(ans[0], count if ans[0] else count - ans[1])]
            return ans
        return wrapped
    return decor


@collect_statistics(statistics)
def check_portions(food, count, recipes=recipes, store=store):
    if food not in recipes or not set(recipes[food].keys()) <= set(store.keys()):
        return (0, 0)
    number = min([store[name] // recipes[food][name] for name in recipes[food].keys()])
    if count <= number:
        return (1, count)
    return (0, number)