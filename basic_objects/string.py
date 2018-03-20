
def basic_string():
    s1 = 'abcdefghijklmn--'
    print(len(s1))
    print(s1[0])
    print(s1[1])
    print(s1[1:3])
    print(s1[-1])
    #############################
    s2 = s1 * 8
    print(s2)
    #############################
    s3 = s1 + 'ABCD'
    print(s3)
    print(s1.find('b'))
    s4 = s1.replace('abc','BCDE')
    print(s4)
    print(s4.upper())
    s5 = 's'
    print(s5.isalpha())
    s6 = '3'
    print(s6.isalnum())
    print(s6.isalpha())

#############################
if __name__ == "__main__":
    basic_string()