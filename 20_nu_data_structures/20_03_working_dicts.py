# DICTIONARIES
# key value pairs (kvp)

this_dict = {
    "make": "Honda",
    "model": "Accord",
    "year": 1996,
    "ev": False
}

print(type(this_dict))

# dictionaries ordered in Python 3.6 or greater
# dictionaries unordered in Python 3.5 or lesser

print(this_dict['model'])

for k in this_dict.keys():
    print(f"key: {k}")

for v in this_dict.values():
    print(f"value: {v}")
    
for k, v in this_dict.items():
    print(f"key is {k} and value is {v}")
    
# update or add a value
this_dict['ev'] = True
print(this_dict)