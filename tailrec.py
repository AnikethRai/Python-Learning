
def mult(a,b,result):
    for i in range(1,a+1):
        result = result+b
    return result

a = int(input('enter a:'))
b = int(input('enter b:'))
result = 0
if a == 0: 
   print (result)
else:
    print(mult(a,b,result))
        


