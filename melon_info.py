"""Print out all the melons in our inventory."""


from melons import melon_names


def print_melon(melon_dict):
    """Takes in melon dictionary and prints each melon with corresponding attribute information."""
    for melon, attribute_dict in melon_dict.items():
        print(melon.upper())
        for attribute, value in attribute_dict.items():
            print(f"\t{attribute}: {value}")


print_melon(melon_names)
#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
