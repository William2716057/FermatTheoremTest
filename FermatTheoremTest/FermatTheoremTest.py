
def checkFermat(a, b, c, n):
    if n <= 2:
        print(f"{n} should be greater than 2")
        return False
    if pow(a,n) + pow(b,n) == pow(c,n):
        print("Solution found")
    else:
        print("failed")
        
def main():
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = int(input("Enter c:"))
    n = int(input("Enter n:"))
    
    checkFermat(a,b,c,n)
    
if __name__ == "__main__":
    main()
