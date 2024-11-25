import math

x = 17.421
y = 0.010365
z = 82800
s = math.pow((y + math.pow((x - 1), 1/3)),0.25) / (abs(x - y) * (math.sin(z) ** 2 + math.tan(z)))
print(s)