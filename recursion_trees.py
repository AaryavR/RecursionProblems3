def paths(m, n):
    if m == 1 or n == 1:
        return 1
    return paths(m-1, n) + paths(m, n - 1)

input("paths(m, n) counts routes throgh an m x n grid moving only right or down. Press enter ")
print(" paths(3, 3) =", paths(3, 3))
n = int(input("Enter grid size for both rows and cols (try 5 or 6): "))
guess = input(f"What is paths({str(n)}, {str(n)})? ")
print(f" paths({str(n)}, {str(n)}) =  {paths(n,n)} your guess: {guess}") 
