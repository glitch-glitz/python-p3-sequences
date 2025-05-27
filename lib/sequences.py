def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    elif length == 2:
        print([0, 1])
        return

    # Start with the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Build the sequence until it reaches the desired length
    while len(fib_sequence) < length:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    print(fib_sequence)
