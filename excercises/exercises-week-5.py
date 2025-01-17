
hrs = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

if hrs > 40:
    print("Wow, you worked over 40 hours this week!")
    pay = hrs * 1.5 * rate
    print('Pay (1.5x rate):', pay)
else:
    pay = hrs * rate
    print('Pay:', pay)
