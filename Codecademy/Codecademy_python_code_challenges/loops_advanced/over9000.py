def over_nine_thousand(lst):
    sum = 0
    for numbers in lst:
        sum += numbers
        if sum >= 9000:
            break
    return sum




print(over_nine_thousand([8000, 900]))