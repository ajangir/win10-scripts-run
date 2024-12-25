import pprint
message = '''It was a bright cold day in April, and 
the clocks were striking thirteen.'''
count = {}

for char in message:
    character = char.lower()
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)