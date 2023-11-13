def solvecubic(a,b,e,f):
    x = ((e + (((e ** 2) + f) ** 0.5)) ** (1/3)) + ((e - ((( e**2 ) + f) ** 0.5)) ** (1/3)) - (b / 3 * a) # The formula to find x.
    return(x.real)
def final(a,b,c,d,name):
    can = str(a) # Transform the int to str
    cen = str(b)
    cin = str(c)
    con = str(d)
    answer = "Hello " + name + ", I will solve " + can + "x^3+" + cen + "x^2+" + cin + "x+" + con + "=0"
    answer = answer.replace('+-', '-') # Avoid "+-6"
    answer = answer.replace('1x^3', 'x^3') # Remove the coefficient of x^3 if it is 1
    return(answer)
name = str(input("Hello there, please tell me your name")) # Ask the name
a = int(input("The a is?")) # Ask a
b = int(input("The b is?")) # Ask b
c = int(input("The c is?")) # Ask c
d = int(input("The d is?")) # Ask d
e = ((-b) ** 3)/( 27 * (a ** 3)) + (b * c)/(6 * (a ** 2)) - (d / 2 * a) # The bracket1
f = ((c / 3 * a) - (b ** 2)/(9 * (a ** 2))) ** 3 # The (bracket2)**3
print(final(a,b,c,d,name)) # Print greeting and the equation
print("The root of the cubic is", solvecubic(a,b,e,f)) # Print the result
quit()