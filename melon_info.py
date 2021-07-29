"""Print out all the melons in our inventory."""


from melons import melon_names


def print_melon(melon_dict):
    """Takes in melon dictionary and prints each melon with corresponding attribute information."""
    for melon, attribute_dict in melon_dict.items():
        print(melon.upper())
        for attribute, value in attribute_dict.items():
            print(f"\t{attribute}: {value}")


print_melon(melon_names)
 
