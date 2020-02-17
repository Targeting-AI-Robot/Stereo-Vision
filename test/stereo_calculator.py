import math

B = 0.136
seta_0 = 62.2
x_0 = 640

l_x = int(input())
r_x = int(input())

D = (B*x_0)/(2*(math.tan(seta_0/2))*(l_x-r_x))
																													
tangent = math.tan(seta_0/2)

print("distance m",D)
print("distance inch",D*39.3701)
#print(tangent)
