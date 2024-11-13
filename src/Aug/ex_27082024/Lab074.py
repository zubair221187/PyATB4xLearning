def make_pizza(*toppings, base):  # only one argument with * is allowed
    print(toppings, base)


def make_pizza2(base, *toppings):  # only one argument with * is allowed and that should be the 1st argument
    print(base, toppings)


zubair = make_pizza("mushroom", "tomato", "cheese", base="thin crust")
zubair = make_pizza2("mushroom", "tomato", "cheese", "thin crust")