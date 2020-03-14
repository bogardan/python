import random

a = [random.randint(0,10) for x in range(10,random.randint(20,30))]
b = [a[x] for x in range(0,len(a)) if a.count(a[x]) == 1]
print("Исходный список:\n",a)
print("Сформированный список:\n",b)

