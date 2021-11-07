import random

pcnumber = random.randint(1, 100)
print('Number between 1 and 100')
human_number = 101

while human_number != pcnumber:
    print('guess')
    human_number = int(input())
    if human_number > pcnumber:
        print('number too high')
    if human_number < pcnumber:
        print('number too low')
    if human_number == pcnumber:
        print('correct')
        break

