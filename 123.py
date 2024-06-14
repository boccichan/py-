def f(money,interest,month):
    result = 0
    for i in range(month):
        result += money
        result *= (100+interest)/100

    return round(result)

print(f(100,2,12))
