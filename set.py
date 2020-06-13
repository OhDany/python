# set unique objects
my_set = {1, 2, 3, 4, 5, 5, 5}
my_set.add(50)
my_set.add(100)
my_set.add(3)

print(my_set)
print(len(my_set))

print('\n')
print('convert list to set to deduplicate')
my_list = [1, 2, 2, 2, 2, 5, 6, 7, 7, 7]
print(my_list)
deduplicate = set(my_list)
print(deduplicate)
print(type(deduplicate))

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8}

# difference
print(my_set.difference(your_set))

# discard
print(my_set.discard(4))
print(my_set)

# difference_update
print(my_set.difference_update(your_set))
print(my_set)

# intersection
print(my_set.intersection(your_set))

# isdisjoint
print(my_set.isdisjoint(your_set))

# union
print(my_set.union(your_set))
print(my_set | your_set)

# issubset
print(my_set.issubset(your_set))

# issuperset
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set))
