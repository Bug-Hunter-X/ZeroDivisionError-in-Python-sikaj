def my_function(a, b):
    if b == 0:
        return "Division by zero"
    else:
        return a / b

result = my_function(10, 0)
print(result) # Output: Division by zero
result = my_function(10,2)
print(result) # Output: 5.0