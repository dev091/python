#sets = unoredered and unique element

my_set = {'mon','tue','wed'}
print(type(my_set))

print(my_set)
my_set.add('fri') # adding new value in set
print(my_set)
my_set.add('tue') # adding again tue in set
print(my_set) # no change coz set is unique and  same new value addition doesnt change old

my_list = ['mon','tue','wed','mon','tue','wed']
days_set =set(my_list) # converting list to set to get unique values
print(days_set)