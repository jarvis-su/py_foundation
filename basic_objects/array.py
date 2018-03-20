

def basic_arrays():
    l1 = [123,234,345,'abc']
    print(len(l1))
    print(l1[1])
    #############################
    l2 = l1 + [4,5,'eee']
    print(l2)
    l2.append(5678)
    print(l2)
    #############################
    l3 = ['aa','bb','dd','cc']
    l3.sort()
    print(l3)
    l3.reverse()
    print(l3)

def nested_arrays():
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    print(m1)
    print(m1[0])
    print(m1[0][2])
    ################################
    col0 = [row[0] for row in m1]
    print(col0)
    col1 = [row[0] + 1 for row in m1] # Add 1 to each item in column 2
    print(col1)
    col2 = [row[0] for row in m1 if row[0]%2 == 0] # Filter out odd items
    print(col2)
    #############################
    diag = [m1[i][i] for i in [0, 1, 2]] # Collect a diagonal from matrix
    print(diag)
    doubles = [c * 2 for c in 'spam'] # Repeat characters in a string
    print(doubles)

    # Note: see later in the book for more on the iteration protocol; its
    # full realization is: G = (...); I = iter(G); I.next() until StopIteration;
    # generators are their own iterator (iter(G) returns G itself), so the iter(G)
    # call described later in this chapter is not required in the following;

    G = (sum(row) for row in m1) # Create a generator of row sums
    print(next(G)) # Run the iteration protocol
    print(next(G)) # Run the iteration protocol


if __name__ == "__main__":
    basic_arrays()
    nested_arrays()