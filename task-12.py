#12 Compress the String
import itertools
string = input("Enter the String:")
input_list = list(string)
key_func = lambda x: x[0]
grouped_data = itertools.groupby(input_list,key_func)
for key,value in grouped_data:
    print("(" + str(len(list(value))) + ", " + str(key) + ")", end=" ")