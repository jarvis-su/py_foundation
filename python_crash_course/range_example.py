def range_example1():
    print("###################################")
    total = 0
    for i in range(101):
        total += i
    return total

def range_example2():
    print("###################################")
    total = 0
    for i in range(10, 20):
        print(i)
        total += i
    return total

def range_example3():
    print("###################################")
    total = 0
    """步长为2"""
    for i in range(0, 20, 2):
        print(i)
        total += i
    return total

print(range_example1())
print(range_example2())
print(range_example3())