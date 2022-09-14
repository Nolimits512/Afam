# Temperature Converter
f = float (input("Enter temperature in F-scale: "))
k = float (input ("Enter temperature in K-scale"))
input = f
if f > 0:
    c = (f - 32) / 9
    print("The temperature in F-Scale:", round(c, 2))

elif k > 0:
    input = k
    c = 273 + k
print ("The temperature in K-Scale:",round(c,2) )




