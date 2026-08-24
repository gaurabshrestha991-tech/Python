def sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You added sprinkles")
        func(*args, **kwargs)
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You added a fudge")
        func(*args, **kwargs)
    return wrapper


def add_price(func):
    def wrapper(*args, **kwargs):
        # result = func(*args, **kwargs)
        print("Price: 150")
        func(*args, **kwargs)
        # return result
    return wrapper



@sprinkles
@add_fudge
@add_price
def get_icecream(flavour):
    print(f"Here is your {flavour} icecream.")

get_icecream("Choclate")