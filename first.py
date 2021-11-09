prev = 1
next = 1
index = 2
check_fib = int(input())

while check_fib > next:
    new_next = prev + next
    prev = next
    next = new_next
    index += 1

if check_fib == next:
    print(index)
else:
    print(-1)