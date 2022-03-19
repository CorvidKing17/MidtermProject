
def ast_grav(): #Gravitational pull while on an asteroid
    g_const = 6.6742*(10**-11) #Based on average spin speed of an asteroid in the main belt
    mass = float(input("What is the mass of the asteroid (kg)? "))
    radius = float(input("What is the radius of the asteroid (km)? "))
    gravity = ((g_const * mass) / (radius**2))
    print(gravity) #Prints out the calculated gravitational pull
    
ast_grav()