# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

a = float(input().rstrip())
b = float(input().rstrip())

c = math.sqrt(a*a + b*b)
d = c/2
beta = math.atan(a/b)

l = math.sqrt(b*b + d*d - 2*b*d*math.cos(beta))

theta = math.asin(d * math.sin(beta) / l) * 180 / math.pi
print(str(round(theta)) + u"\N{DEGREE SIGN}")

# math.sin(45)
# math.asin(math.sin(math.pi/4)) * 180 / math.pi

# print(chr(248))
# print('°')
# int('°')
# u"\N{DEGREE SIGN}"