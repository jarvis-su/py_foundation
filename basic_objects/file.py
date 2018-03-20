
def write_file(file):
    f = open(file, 'w')
    f.write('hello  \n')
    f.write('world \n')
    f.close()


def read_file(file):
    f = open(file)
    text = f.read()
    print(text)

if __name__ == "__main__":
    file = '../data/test.txt'
    write_file(file)
    read_file(file)

    print("hello")