# Ideal-Gas-Simulation
A python script that uses Vpython to model an ideal gas, using the ideal gas equations to show how the velocities of the gas particles are distributed over time.
# The Physics
We start by making some key assumptions and conclusions about the gas.
 - All of the gas particles have radius of 1, and uniform density of 1, and thus mass of 4/3*pi
 - All of the collisions between the gas particles / conatiner are fully elastic, and instantaneous
 - There are no electrostatic or gravitational forces between gas particles, only normal contact force during collisions
 - The particles are initially moving in random directions with random speeds
 - The container is fully rigid, therefore the volume of the gas is fixed.
 - The total energy of the system is fixed, given that:
   - Particles collide elastically, conserving kinetic energy
   - Gravitational forces are negligable/ignored, and so no gravitational potential energy
   - Electromagnetic forces are also ignored, and so the particles also have no electromagnetic potential energy
  (I have found in testing that particles can actually gain some kinetic energy, but it is generally of the order of x10^-14 J)
 - Given that the kinetic energy of the particles is constant, we can conclude that the temperature of the gas is constant (KE = 1.5KbT)
 -We assume that no particles can enter or leave the container, and so the number of mols of gas is fixed.
 - Given that the absolute temperature, volume and temperature of a fixed amount of gas is constant, we conclude that the pressure of the gas is also constant (PV=nRT)


# How it works

1) Code takes the input requirements fron the user, and uses Vpython to generate the number of gas particles requested randomly distributed in a container, of the size specified by the user.
2) A random velocity vector is assgned to each molecule, of both random speed and direction.
3) The code goes through a loop of all particles,checking if it has collided with the container, and then loops through every other particle to check if the magnitude of the position vectors of the first and second particles is less that 2 (2*radius).
4) If the particle has not collided with any other particles, its new position vector = old position vector + velocity vector.
5) If the particle has collided with another particle, an elastic collision is simulated by calcuating the normal vector between the 2 particles, and then resovling the velocities of both particles in to their parallel and perpendicular components. The perpendicular components of each particle is swapped, thus acheiving an elastic collison that obeys the conservation of linear momentum.
6) The loop repeats this for every particle, removing any already collided particles from the second nested loop to halve the complexity of the script. It then increments the time by a small increment, dt.
7) After a certain number of loops, the code stops and calculates the average kinetic energy of the particles, and uses this to plot the Maxwell-Boltzmann distribution for this gas in matplotlib
8) A bar chart of velocities is then plotted over the Maxwell-Boltzmann distribution, and we see that the velocities of the particles do indeed follow the distribution.
