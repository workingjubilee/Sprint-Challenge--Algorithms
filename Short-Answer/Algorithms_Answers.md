Add your answers to the Algorithms exercises here.

# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0 # So we start at 0...
    while (a < n * n * n): # ...then establish a condition of a cube...
      a = a + n * n # and try to meet it with a square.
```
If n is 0 then we're done, but if n is 1, then we loop once, and if n is 2, then we loop twice, and then if n is 3, we loop 3 times. If n is 10, we loop 10 times, etc. This is an O(n) algorithm, in spite of its confusing expression.



```
b)  sum = 0
    for i in range(n):
      i += 1 # aaa...
      for j in range(i + 1, n): # aaaaaa
        j += 1
        for k in range(j + 1, n): #aaaaaaAAAAAAA
          k += 1
          for l in range(k + 1, 10 + k): #AAAAAAああああああああああああああああ
            l += 1
            sum += 1
```
This algorithm is (internal screaming).

The outer "i" loop finishes in half the time of n, because it increments twice. But each iteration of i brings with it an iteration of j, which is also half the time. Then we iterate through k, which will also be half. And we bring with us an iteration of l, reliably about 5 times (because if k is 1, we go from 2 to 11, but if k is 1000, we go from 1001 to 1010). Could be 4, but that doesn't seem terribly important at this point, it's sufficient to know that innermost l loop does not actually increase with the size of n.

So if we fire this up with an n of 10 or so (I'm barely doing the math at this point, yes, because I don't care about the exact values now that I've seen the pattern), we have about 5 iterations of i (scales directly in relation to n), each of which brings about 5, then 4, then 3, then 2, then 1 iterations of j, as j loops over a smaller amount each time (an n log^n scale), each of which does something similar with k (another n log^n scale), and then brings another 4 or 5 iterations of l, just as a gotcha.


This is something nightmarish. It explodes. I am not sure it is n^factorial, but it is O 2^n at least, and it's at least trying to make n^factorial feel nervous. I'll get a more exact number if I finish robot sort early.

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0 # Finish condition.
      return 2 + bunnyEars(bunnies-1) # recurse once per bunny
```
So, if bunnies is 0, we're done, but if bunnies is 1, or 2, or 3, we're pushing a stack frame per bunny. But we aren't doing anything more complex than that. This algorithm will only have one iteration per bunny, so we might as well use a `for` loop, as that will save us from stack overflow, but like a typical single `for` loop, it's _just_ O(n) time once you simplify out that constant (using an iterator vs. using the stack).

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get broken if dropped off a floor less than floor _f_. Devise a strategy to determine the value of _f_ such that the number of dropped eggs is minimized.


When n is 2 and f is 2, I have to throw 2 eggs to determine the value of f, But if n is 2 and f is 1 or 0 (effectively identical), I could find out f is 1 by throwing off the first floor first, and I would not need to throw another egg. So I should probably always test the first floor as my first attempt if I don't have a guarantee that f is non-zero, as that creates a boundary of assuring whether f is a positive whole number greater than 1 (one I can meaningfully search for). However, that doesn't resolve problems like when I am throwing off the Sears Tower (110 stories high!) or something similar, and f is some number like 50 (this seems implausible, but maybe I have very bouncy eggs, or this algorithm is secretly interacting with a very cushy trampoline).

In order to find larger values of f amidst larger values of n with a minimal amount of egg tossing, I could throw an egg at floor n/2, call that floor t (for test), and then if it breaks, I would throw an egg at t/2, if it doesn't, I throw an egg at t+((n-t)/ 2), and so on, slicing the search range in half with each test.