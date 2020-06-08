"""Temel bir kayan yazı uygulaması"""

import time
x = input("Yazıyı giriniz : ")
# bu program şuna benzer çıktı verecektir:
# 1234
#  123
#   12
#    1
#
# 4
# 34

liste = [i for i in x]
print(*liste, end="")

for k in liste:
    for i in k:

        liste.pop(-1)
        liste.insert(0, " ")

    print("\r", end="")
    print(*liste, end="")
    time.sleep(1)

for l in range(len(liste)):
    liste.insert(0, x[-l-1])

    print("\r", end="")
    print(*liste, end="")
    time.sleep(1)
