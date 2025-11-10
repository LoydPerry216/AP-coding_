a = 100
b = 0
if b > a:"a student did not turn in homework"
print("b is greater than a,student did not turn in homework")
a = 0
b = 100
if a > b: "student did turn in homework"
print("a is greater than b,student did turn in homework")





numberList = [1, 5, 10, 20, 39, 48, 83, 89, 72, 90]
x = max(numberList)
y = min(numberList)
print(x)
print(y)

def my_function(x):
  return x[::-1]

mytxt = my_function("Book")

print(mytxt)

def pdCheck():
    print("please enter a number.")
    number = input()
    values = []

    while number != 'q':
        values.append(int(number))
    print(values)
    print("Please enter a number")
    number = input()
else:
print('doing calution...')
total = sum(values)
print(total)
