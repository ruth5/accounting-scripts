"""Print out all the melons in our inventory."""


from melons import melon_names


def print_melon(melon_dict):
    """Takes in melon dictionary and prints each melon with corresponding attribute information."""
    for melon in melon_dict:
        print(melon.upper())
        print(f"\ttab test")


print_melon(melon_names)
#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
