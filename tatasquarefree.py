def count_square_free(n):

    count = 0
    p = 2

    while p * p <= n:

        if n % p == 0:
            count += 1

            # Remove all occurrences of this prime
            while n % p == 0:
                n //= p

        p += 1

    # If remaining n is a prime number
    if n > 1:
        count += 1

    # 2^count includes 1, so subtract 1
    return (2 ** count) - 1


n = int(input())

print(count_square_free(n))