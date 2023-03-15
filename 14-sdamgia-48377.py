def f(x):
    return 14*13**0 + 18*13**1 + (x+2)*13**2 + (6+x)*13**3 + 6*13**4


for x in range(0, 13):# [0, 13)
    if f(x) % 34 == 0:
        print(f(x) // 34)
        break