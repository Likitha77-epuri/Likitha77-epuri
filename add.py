def greet_1():
    a = "Hello"
    print(a)
    print(id(a))

def greet_2():
    a = "Hey"
    print(a)
    print(id(a))

print("Namespace - 1")
greet_1()
print("Namespace - 2")
greet_2()