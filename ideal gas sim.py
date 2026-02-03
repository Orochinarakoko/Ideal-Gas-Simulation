from vpython import *
import matplotlib.pyplot as pyp
from numpy import linspace
import math

bodies = []


#-------------------------------------------------------------------------
num_bodies = int(input("How many gas particles >>> "))

area = float(input("Side length of container >>> "))

dt = float(input("Time step >>> "))

steps = int(input("Number of steps >>> "))
#------------------------------------------------------------------------


init_v = area / 10

t = 0

prev_KE = 0

container = box(opacity = 0.2 , width = area + 4, height = area + 4, length = area + 4, pos = vector((area/2),(area/2),(area/2)))


for i in range(num_bodies):
    body = sphere(pos = vector(random()*area,random()*area,random()*area),color = color.magenta , radius = 1)
    bodies.append(body)
    
for i in bodies:
    
    i.mass = (4/3)*pi

    i.v = vector(2*(random() - random())*init_v,2*(random() - random())*init_v,2*(random() - random())*init_v)

    prev_KE += 0.5*i.mass*mag(i.v)**2
                                      
while t < steps*dt:

    num_looped = 1
    
    for body1 in bodies:

        if body1.pos.x < -1 or body1.pos.x > area + 1:
            body1.v.x *= -1
            body1.pos.x -= (body1.pos.x/abs(body1.pos.x))*0.01


        if body1.pos.y < -1 or body1.pos.y > area + 1:
            body1.v.y *= -1
            body1.pos.y -= (body1.pos.y/abs(body1.pos.y))*0.01

        
        if body1.pos.z < -1 or body1.pos.z > area + 1:
            body1.v.z *= -1
            body1.pos.z -= (body1.pos.z/abs(body1.pos.z))*0.01

            
        for i in range(num_looped , len(bodies)-1):
            body2 = bodies[i]
        


            distance = mag(body1.pos - body2.pos)
                
            if distance < 2:
                    
                norm_vect = body1.pos - body2.pos

                norm_vect = norm_vect / mag(norm_vect)

                perp_comp1 = dot(body1.v , norm_vect) * norm_vect

                perp_comp2 = dot(body2.v , norm_vect) * norm_vect

                par_comp1 = body1.v- perp_comp1

                par_comp2 = body2.v - perp_comp2

                body1.v = par_comp1 + perp_comp2

                body2.v = par_comp2 + perp_comp1

                body1.pos += 0.1*norm_vect
                body2.pos -= 0.1*norm_vect

                 
        body1.pos += body1.v * dt

        num_looped += 1

    t = t + dt
    print(t)

velocities = []

KE_avg = 0

for i in bodies:
    velocities.append(mag(i.v))
    KE_avg += 0.5*(i.mass)*((mag(i.v))**2)

#print(prev_KE - KE_avg) # uncomment to show that energy is conserved

KE_avg = KE_avg / num_bodies

vrange = linspace(0,max(velocities),100)
prange = []

for i in vrange:
    MaxB = ((4*math.pi)/(KE_avg**(3/2)))*(i**2)*(math.e**(-(math.pi*(i**2))/KE_avg))
    prange.append(MaxB)

pyp.plot(vrange,prange)
pyp.hist(velocities , bins = 15,density = True)
pyp.show()
    
