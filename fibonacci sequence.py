


def fib(term):
   if term <= 1:
       return (term)
   else:
       return (fib(term-1) + fib(term-2))

# Change this value to adjust the number of terms in the sequence.
number_of_terms = 90
for i in range(number_of_terms):
    print(fib(i))
