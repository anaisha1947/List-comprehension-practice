numbers = input("Enter a list of numbers separated by spaces: ").split()
odd = [x for x in numbers if int(x)%2==1]
print("List of odd numbers:", odd) 
odd_num = [1,3,5,7,9,11,33,55,77,99]
print(odd_num)
fruits = ["apple", "banana", "pear", "grapes", "strawberry"]
capital_fruits = [fruit for fruit in fruits if fruit[0].isupper()]
print(capital_fruits)