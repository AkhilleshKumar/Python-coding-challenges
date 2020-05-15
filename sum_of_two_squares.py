def sum_of_two_squares(n):
    sqr_limit=int(n**(1/2))
    squares=[i**2 for i in range(1,sqr_limit+1)]
    for i in range(len(squares)-1,-1,-1):
        for j in range(i,-1,-1):
            if(squares[i]+squares[j]==n):
                return (i+1,j+1)
    return None

n=int(input("Enter value of n: "))
result=sum_of_two_squares(n)
print(result)

