
def wubba_lubba(x):
    numbers = []
    for i in range(1, x+1):
        if i%3==0 and i%5==0:
            numbers.append('Fizbuzz')
        elif i%3==0:
            numbers.append('Fizz')
        elif i%5==0:
            numbers.append('Buzz')
        else:
            numbers.append(str(i))
    print(numbers)

wubba_lubba(20)
