# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


#PART 1 GREET TEMPLATE
def greet(name, greeting="Hello, <name>!"):
    if "<name>" in greeting:                                              # Toch stiekem de <name> handling erin geprogrammeerd, gewoon omdat het kan. Give it a go op lijn 15-17
        return greeting.replace("<name>", name)                     
    else:
        return(f"{greeting}, {name}!")

#print(greet("Chris"))
#print(greet("Chris", "What is up"))
#print(greet("Chris", "How is it hanging, <name>!"))             


#PART 2 FORCE
bodies = {
    "sun"     : 274.0,
    "jupiter" :  24.9,
    "neptune" :  11.2,
    "saturn"  :  10.4,
    "earth"   :   9.8,
    "uranus"  :   8.9,
    "venus"   :   8.9,
    "mars"    :   3.7,
    "mercury" :   3.7,
    "moon"    :   1.6,
    "pluto"   :   0.6
}

def force(mass, body="earth"):
    return mass * bodies[body]

#print(force(2,"uranus"))


#PART 3 
def pull(m1, m2, d):
    return 6.674*10**-11 * ((m1 * m2) / d**2)

#print(pull(800,1500,3)) #Dit was het voorbeeld van de 2 auto's op de website.





