def factorial(n):
    
    if n == 0 or n == 1:
        return 1
        
    return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        
        if num < 0:
            print("Invalid Input! Please enter a non-negative number.")
        else:
            result = factorial(num)
            print(f"Factorial of {num} is: {result}")
    
    except ValueError:
        print("Invalid Input! Please enter a valid integer.")
