#元组基本就像一个不可以改变的列表，一旦创建后就不能改变，
# 也就是说元组是不可改变的序列

def basic_tuple():
    T = (1,2,3,45)
    print(len(T))
    T = T + (5,6)
    print(T)
    #'tuple' object does not support item assignment
    # T[1] = 3

if __name__ == "__main__":
    basic_tuple()
    print("hello")