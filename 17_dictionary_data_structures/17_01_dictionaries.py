dictionary = {
    'key_value_pairs': 'kvp', 
    'keys': 'unique', 
    'values': 'any immutable data type',
    '>=python_3.16': 'ordered',
    '<python_3.16': 'unordered'
    }

# duplicate keys will overwrite
member_levels = {1: 'Gold', 2: 'Silver', 3: 'Bronze', 3: 'Copper'}
print(member_levels)
#  {1: 'Gold', 2: 'Silver', 3: 'Copper'}