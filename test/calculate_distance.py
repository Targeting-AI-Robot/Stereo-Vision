import math
import sys

rx = 1920        #resolution for X
ry = 1080        #resolution for Y
cx = rx//2		#principal point for X
cy = ry//2		#principal point for Y
f = 3.04
h = 165.1
vx = int(input())
vy = int(input())
x = int(input())
y = int(input())
#vx,vy = map(int,input().split()) #sosil_point
#x,y = map(int,input().split())  #object

tilt_ang = math.atan2(vy-cy,f)

u = (x-cx)/f
v = (y-cy)/f

C_P_ = h*math.tan(90+tilt_ang-math.atan(v))
CP_ = math.sqrt(h*h+(C_P_*C_P_))
Cp_ = math.sqrt(1+v*v)
PP_ = u*CP_/Cp_
d = math.sqrt((C_P_)*(C_P_)+(PP_*PP_))
print("distance mm",d)
print("distance inch",d/25.4) 
