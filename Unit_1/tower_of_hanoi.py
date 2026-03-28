def hanoi(n, source, helper, destination):

    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1   # count 1 move
    
    moves1 = hanoi(n - 1, source, destination, helper)

    print(f"Move disk {n} from {source} to {destination}")
    moves2 = 1
    
    # Move n-1 disks from helper to destination
    moves3 = hanoi(n - 1, helper, source, destination)
    
    return moves1 + moves2 + moves3

if __name__ == "__main__":
    try:
        num = int(input("Enter number of disks: "))
        
        if num <= 0:
            print("Please enter a positive number.")
        else:
            print("\nSteps to solve Tower of Hanoi:\n")
            total_moves = hanoi(num, 'A', 'B', 'C')
            
            print(f"\nTotal Moves: {total_moves}")
            print("Formula Check (2^n - 1):", 2**num - 1)
    
    except ValueError:
        print("Invalid Input! Please enter a valid integer.")
