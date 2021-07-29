melon_names = {
    'Honeydew': {"price": 0.99, "seedlessness": True}, 
    'Crenshaw': {"price": 2.00, "seedlessness": False},
    'Crane': {"price": 2.50, "seedlessness": False},
    'Casaba': {"price": 2.50, "seedlessness": False} ,
    'Cantaloupe': {"price": 0.99, "seedlessness": False} 
}

for attribute_dict in melon_names.values():
    attribute_dict['flesh_color'] = attribute_dict.get('flesh_color', None)
    attribute_dict['weight'] = attribute_dict.get('weight', None)
    attribute_dict['rind_color'] = attribute_dict.get('rind_color', None)
