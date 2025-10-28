import math
def valid(a,b,c):
    if a+b >= c and a+c >= b and b+c >= a:
        return True
    else:
        return False

def face(a,b,c):
    small_face = (a+b+c)/2
    almost_face = small_face*(small_face-a)*(small_face-b)*(small_face-c)
    area = math.sqrt(almost_face)
    return area
x = int(input("stranata a:"))
z = int(input("stranata b:"))
y = int(input("stranata c:"))
valid(x,z,y)
if not valid:
    quit("Nepravilen triugulnik")
else:
    print(round(face(x,y,z),2))