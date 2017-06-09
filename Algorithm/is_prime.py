from math import sqrt
from itertools import count, islice

def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True
x=0
for i in range(100):
    if i>10 and isPrime(i):
        print(i, end=", ")
        x+=1

print("\n",x)

'''

check this also:http://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime

http://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
I don't actually think the best solution has been found in these answers, so I'm gonna post mine, and explain why this is a better one:

from math import sqrt; from itertools import count, islice

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
Note: the n > 1 check is needed since that 1 is not a prime number, and so is zero and any negative number.

Explanation

I'm gonna give you some insides about that almost esoteric single line of code that will check for prime numbers:

First of all, using range() is really a bad idea, because it will create a list of numbers, which uses a lot of memory. Using xrange() is better, because it creates a generator, which doesn't use any memory to work, but generates every number on-the-fly. By the way, this is not the best solution at all: trying to call xrange(n) for some n such that n > 231-1 (which is the maximum value for a C long) raises OverflowError. Therefore the best way to create a range generator is to use itertools:
xrange(2147483647+1) # OverflowError

from itertools import count, islice

count(1)                        # Count from 1 to infinity with step=+1
islice(count(1), 2147483648)    # Count from 1 to 2^31 with step=+1
islice(count(1, 3), 2147483648) # Count from 1 to 3*2^31 with step=+3
You do not actually need to go all the way up to n if you want to check if n is a prime number. You can dramatically reduce the tests and only check from 2 to √(n) (square root of n). Here is why:

Let's find all the divisors of n = 100, and list them in a table:
 2  x  50 = 100
 4  x  25 = 100
 5  x  20 = 100
10  x  10 = 100 -> Square root of 100
20  x  5  = 100
25  x  4  = 100
50  x  2  = 100
You will easily notice that, after the square root of n, all the divisors we find were actually already found. For example 20 was already found doing 100/5. The square root of a number is the exact mid-line where the divisors we found begin being duplicated. Therefore, to check if a number is prime, you'll only need to check from 2 to sqrt(n).
Why sqrt(n)-1 then, and not just sqrt(n)? That's because the second argument provided to  itertools.islice object is the number of iterations to execute. islice(count(a), b) stops after b iterations. That's the reason why:
for number in islice(count(10), 2):
    print number,

# Will print: 10 11

for number in islice(count(1, 3), 10):
    print number,

# Will print: 1 4 7 10 13 16 19 22 25 28
The function all(...) is the same of the following:

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
it literally checks for all the numbers in the iterable, returning False when a number evaluates to False (which means only if the number is zero). Why do we use it then? First of all, we don't need to use an additional index variable (like we would do using a loop), other than that: just for concision, there's no real need of it, but it looks way less bulky to work with only a single line of code instead of several nested lines.
Extended version

I'm including an "unpacked" version of the isPrime() function, to make it easier to understand and read it:



def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True
'''
