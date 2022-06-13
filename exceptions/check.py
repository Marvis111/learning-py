
def is_prime(num: int) -> bool :
    """
    This number checks if a number is prime
    """
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for nums in range(2, num):
            if num % nums == 0 :
                return False
                break
        return True

def sqr(n): return n**2


prime = is_prime(97)

print(prime)

print(sqr(2))
square = lambda n : n ** 2

even = lambda num : num % 2 == 0

print(even(5))

add = lambda x , y : x + y

print(square(10)) 
print(add(2,4))

