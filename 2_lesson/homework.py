num_str = 125
print(type(num_str))
num_str = str(num_str)
print(type(num_str))
message = 'Hi, my name is Python!'
print(message)
message = message.replace('y', '0')
message = message.replace('i', '1')
print(message)
split_test = 'This is a split test'
print(split_test)
split_test = split_test.split()
print(split_test)
string_join = " ".join(split_test)
print(string_join)
print(len(string_join))
list_append = [1, 2, 3]
print(list_append)
list_append.append(4)
print(list_append)
list_append.append(5)
print(list_append)
list_extend = [4, 5, 6]
print(list_extend)
list_extend.extend([7, 8, 9])
print(list_extend)
print(list_extend.index(6))
print(len(list_append))
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'], dict_test['where'])
print(dict_test.keys())
print(dict_test.values())
print(dict_test.items())