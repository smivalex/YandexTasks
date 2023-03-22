# Вход:
# Ширина фотографии, к которой масштабируем
# параметры n - общее число фотографий, m - количество фотографий в ленте
# ширина x высота каждой фотографии
#
# Вывод:
# mini - минимальная длина ленты из m отмасштабированных фотографий
# maxi - максимальная длина ленты из m отмасштабированных фотографий

mini = maxi = 0
wBase = int(input())
parameters = input()
n, m = parameters.split(" ")
n = int(n)
hList = list()
for i in range(int(n)):
    imageData = input()
    w, h = imageData.split("x")
    hList.append(int(h)*wBase/int(w))
hList.sort()
for i in range(int(m)):
    mini += hList[i]
    maxi += hList[int(n)-i-1]
print(mini)
print(maxi)
