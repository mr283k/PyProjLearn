"""
#!/usr/bin/env python3
with open('/Users/mahi.kalakota/dev/animals.txt', 'w') as the_file:
    the_file.write('man\nbear\npig\ncow\nduck\nhorse\ndog')
with open('/Users/mahi.kalakota/dev/animals.txt', 'r') as the_file:
    print(the_file.read())
    print()

with open('/Users/mahi.kalakota/dev/animals.txt', 'r') as the_file:
    animal_list = []
    for list in the_file:
        animal_list.append(list.rstrip())
        #animal_list = print('{}'.format(list))
    print('animals list')
    print(animal_list)
    print()

with open('/Users/mahi.kalakota/dev/animals_sorted.txt', 'w') as the_sort_file:
    sorted_animal_list = sorted(animal_list)
    for sort_list_items in sorted_animal_list:
        the_sort_file.write('{}\n'.format(sort_list_items))

with open('/Users/mahi.kalakota/dev/animals_sorted.txt', 'r') as the_sort_file:
   print('sorted animal file')
   print(the_sort_file.read())
"""

# code given in course
#!/usr/bin/env python3
unsorted_file_name = '/Users/mahi.kalakota/dev/animals.txt'
sorted_file_name = '/Users/mahi.kalakota/dev/animals_sorted.txt'
animals = []
try:
   with open(unsorted_file_name) as animals_file:
      for line in animals_file:
         animals.append(line)
   animals.sort()
   print(animals)
   print()
except:
   print('Could not open {}.'.format(unsorted_file_name))

try:
    with open(sorted_file_name, 'w') as animals_sorted_file:
        for animal in animals:
            animals_sorted_file.write(animal)
except:
    print('Could not open {}.'.format(sorted_file_name))

try:
    with open(sorted_file_name, 'r') as animals_sorted_file:
        print(animals_sorted_file.read())
except:
    print('Could not open {}.'.format(sorted_file_name))