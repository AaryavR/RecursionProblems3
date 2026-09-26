def hanoi(n):
    if n == 0:
        return 0
    return 2 * hanoi(n-1) + 1

input("Hanoi(n) counts the minimum moves to shift n disks from peg A to peg C. Press enter ")
print(" hanoi(1) =", hanoi(1))
print(" hanoi(2) =", hanoi(2))

n = int(input("Enter number of disks (try 3 or 4): "))
guess = input("what is hanoi(" + str(n) + ")? " )
print(" hanoi(" + str(n) + ") =", hanoi(n), " your guess:", guess)
