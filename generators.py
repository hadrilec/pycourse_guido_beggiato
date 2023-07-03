# iterABLE: something that can be iterated over, i.e.: you can do a for loop on it
# iterATOR: something that is iterATING on an iterABLE, i.e.: it's a ONE TIME STREAM of data

    # ONE TIME -> once you use it, it's gone
    # STREAM: elements are given ONE AT TIME and not all toghether


import itertools
from pprint import pprint

from pathlib import Path

# iterable (list, tuple, set, dict)
lst = [1, 2, 3]

# the built-in 'iter' returns an iterator created from the provided iterable
it = iter(lst) 

# the built-in 'next' advances the given iterator by 1
# it 'yelds' the first available element
a = next(it) 
b = next(it)
c = next(it)
#d = next(it) #raises error, because the iterator is exhausted (all elements have already been given)

# when writing a for loop, under the hood what happens is that
# an iterator is created
# 'next' is called until the iterator is exhausted
for i in it:
    print(i)

# given the concept of 'stream of data', we can now 
# use iterators to define data pipelines
# -> memory efficient, as only 1 element is kept in memory at time
# faster than regular python (as we delegate to C code) [even if not as fast as numpy, pandas, scipy, ...]


# range, map, filter, itertools, ... -> they all provide objects belonging
# to the family of 'one stream of data' (as a CONCEPT, they may be implemented
# differently)

def some_func(n):
    return n + 2

# this can be arbitrarily big but we 
# will not run into memory issues, as we 
# take one element at time. there could be speed
# issues, though
big = range(100) 
step1 = map(some_func, big)
step2 = map(lambda x: x*3, step1)
step3 = itertools.filterfalse(lambda x: x%2, step2)
# here we need our elements: sum needs one element and 
# will look for it in 'step3', that as well will look
# in 'step2' up to 'big'. elements will then be fed
# one by one to the 'sum' function and 'res' will be returned
res = sum(step3) 

# --------------------------
base = [4, 6, 8]
# no need to use 'map' if the function to 
# apply is really easy: just use a 
# generator expression
gen = (i/2 for i in base)

z = next(gen) 
print(z) # 2
print(tuple(gen)) # (3, 4)


# if you use square brackets around a 
# generator, you get a list comprehension:
# this is in-memory, meaning all elements 
# will be collected

# one-step
gen_as_list = [i/2 for i in base]

# same thing, but in 2 steps
s1 = (i/2 for i in base)
s2 = list(s1)

# generators and iterators are everywhere
# in the standard library
p = Path.home()
for f in p.iterdir():
    print(f)

# try looking up the 'csv' module
big_file = "some_file.csv"

# itertools
# https://docs.python.org/3/library/itertools.html

# this is a module all built around the
# concept of iterator and provides
# lots of functionality
# 99% of the time, what you need is in this 
# module already or is a simple combination
# of the functions provided
nums = list(range(20))
letters = itertools.cycle("ABCD")

# keep your generator expressions simple: less 
# lines do not imply more speed nor less memory use

# with iterators
alt = (n for n in nums if n%2==0)
alt = filter(lambda x: x%2==0, nums)
alt = ( (n, next(letters)) for n in alt)
pprint(tuple(alt))

# with a regular loop
for n in nums:
    if n % 2 == 0:
        t = (n, next(letters))
        print(t)

# -------------

def func(a, b):
    return a + b

elems = range(4)
seconds = 1

res = map(func, elems, itertools.repeat(seconds, len(elems)))

print(list(res))

# ----------------
elems = range(4)
seconds = itertools.repeat(1, len(elems))

res = map(func, elems, seconds)

print(list(res))

la = [1, 2]
lb = [3, 4]
lc = [5, 6]
z = zip(la, lb, lc) # zip !
pprint(tuple(z))
for i in z:
    print(i)

# ------------------

# nested for loops can be elegantly hidden (and slightly sped-up)
# by using 'itertools.product'

pool = [1, 2, 3]
pool2 = [4, 5, 6]
pool3 = [7, 8, 9]

for i in pool:
    for j in pool2:
        for k in pool3:
            print(i, j, k)

its = itertools.product(pool, pool2, pool3)
for t in its:
    i, j, k = t # unpack the returned tuple here for symmetry with the above example
    print(i, j, k)
