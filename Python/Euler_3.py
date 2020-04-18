import time
start = time.time()

def prime(n):

    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n = 600851475143 

ans = 0
for i in range(2,int(n**0.5)+1):
    if n%i == 0:
        if prime(n//i):
            print(n//i)
            print('Time taken {} sec'.format(time.time()-start))
            exit()
        elif prime(i):
            ans = i
print(ans)
print('Time taken {} sec'.format(time.time()-start))