''' finding Maximum and Minimum in a list '''
numbers = input("Enter numbers separated by space:").split()
numbers=[int(num)for num in numbers]
max_num = numbers[0]
min_num = numbers[0]
for num in numbers :
    if num > max_num :
        max_num = num
    if num < min_num :
        min_num = num


print(f"Maximum: {max_num}")
print(f"Mininum: {min_num}")
