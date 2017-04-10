import yaml

def print_suggestion(suggestion_dict):
    print((
        '{name}, it is a {category} place '
        'on {street} in {city}.'
    ).format(
        name=suggestion_dict['name'],
        category=suggestion_dict['category'],
        street=suggestion_dict['street'],
        city=suggestion_dict['city']
    ))

with open('suggestions/jamesw.yaml', 'r') as suggestion_file:
  DEFAULT_SUGGESTION = yaml.load(suggestion_file)
print('I suggest this restaurant:')
print_suggestion(DEFAULT_SUGGESTION)
