
NAV = "NAV"
ERTICA = "ERTICA"
NAVERTICA = "NAVERTICA"

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(NAVERTICA)
    elif i % 3 == 0:
        print(NAV)
    elif i % 5 == 0:
        print(ERTICA)
    else:
        print(i)