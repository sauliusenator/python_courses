def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fib_generator(8):
    print(num)
#
#-----------------------------------------------------------
def filtruoti_lyginius(seka):
    for skaicius in seka:
        if skaicius % 2 == 0:
            yield skaicius

skaiciai = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lyginiai = list(filtruoti_lyginius(skaiciai))
print("Lyginiai skaičiai:", lyginiai)

