# reading: 3.4

# Problems:
# Write a function that returns the unique prime factors of a number as a set, e.g. f(8) = {2}, f(9) = {3}, f(10) = {2, 5}, f(12) = {2, 3}.
# No fancy math (e.g. number sieve) required; slow algorithms are ok.
def is_prime(a,N):
    print(a, N)
    if N <= 1:
        return
    else:
        if a >= N:
            print(N)
        else:
            if N == 2:
                print(N)
            elif (N % a) == 0:
                return False
            else:
                return is_prime(a+1,N)

    return False




# Write a function that returns the unique prime factors as a map of the factor to how many times it is used, e.g. f(8) = {2: 3}, f(9) = {3: 2}, f(10) = {2: 1, 5: 1}


# 3.2.6


# 3.2.7


# 3.2.10