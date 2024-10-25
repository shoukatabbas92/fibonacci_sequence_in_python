def fibonacci(n):
    sequence = [0,1]
    for i in range(2,n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[:n]

n = int(input("Enter a number"))
print("Fibonacci number is:", fibonacci(n))