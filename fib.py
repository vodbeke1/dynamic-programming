import sys

memo = {}
def fib(n):
    global memo
    
    if n <= 2:
        f = 1
    else:
        try:
            n1 = memo[n-1]
        except:
            n1 = fib(n - 1)
            memo[n-1] = n1
        
        try:
            n2 = memo[n-2]
        except:
            print("This is the except: {}".format(n-2))
            n2 = fib(n - 2)
            memo[n-2] = n2
        f = n1 + n2
    return f

if __name__ == "__main__":
    print(fib(100))
    print(len(str(fib(100))))
    print(sys.maxsize)