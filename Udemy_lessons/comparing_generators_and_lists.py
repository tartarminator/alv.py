import time

# print(sum([number for number in range(10)]))
#
# print(sum(number for number in range(10)))  # This method is faster than previous in case of big data
# It creates first list and than calculates sum
list_start_time = time.time()
print(sum([number for number in range(10000000)]))
list_processing_time = time.time() - list_start_time

# In this case it calculates directly
gen_start_time = time.time()
print(sum(number for number in range(10000000)))
gen_processing_time = time.time() - gen_start_time

print(f'Processing with list is {list_processing_time}')
print(f'Processing with generator is {gen_processing_time}')
print('The difference of speed between those methods is ' + str((list_processing_time - gen_processing_time)))
