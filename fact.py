def fact(n):
    assert n>+0,"factorial not difined for negative values."
    if n < 2:
        return 1
    else:
        return n*fact(n-1)
def main():
    num=int(input("Enter Positive Number:"))
    print("Factorial of",num,"is",fact(num))

main()

