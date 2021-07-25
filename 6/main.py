"""
    练习6
"""

res = []

for i in range(100, 1000):
    tmp = (i // 100) ** 3 + (i % 100 // 10) ** 3 + (i % 10) ** 3
    if tmp == i:
        res.append(i)

print("100-1000中的水仙花数：", res)
print("总个数：", len(res))
