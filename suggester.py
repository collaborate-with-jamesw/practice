import yaml

def print_suggestion(suggestion_dict):
    print(suggestion_dict['name'])
    print(suggestion_dict['category'])
    print(suggestion_dict['street'])
    print(suggestion_dict['city'])

with open('suggestions/jamesw.yaml', 'r') as suggestion_file:
  DEFAULT_SUGGESTION = yaml.load(suggestion_file)
print('I suggest this restaurant:')
print_suggestion(DEFAULT_SUGGESTION)
