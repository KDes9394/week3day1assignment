my_string = "This string has 10909090 numbers, but it is only 1 string. I hope you solve this 2day."
compiler = compile('[0-9]+')
found_nums = compiler.findall(my_string)
print(found_nums)
# Output: ['10909090','1',2]




