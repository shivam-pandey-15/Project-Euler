import time

def prime(n):
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True
 
c=0
i=2

start = time.time()
while True:
  if prime(i):
    c+=1
  if c==10001:
    print(i)
    print("Time Taken {:.6f} secs!!".format(time.time()-start))
    exit()
  i+=1