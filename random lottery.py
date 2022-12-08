import random
n=0
while True:
    a=int(input('enter your number'))
    b=random.randint(0,10)
    print('random number is ',b)
    if a>b:
        print('too large')
        n+=1
    elif a<b:
      print('too small')
      n+=1
    elif a==b:
        n=n+1
        break
print('you won after',n,"turns")


