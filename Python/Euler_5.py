from math import gcd
import time

start = time.time()

ans = 1

for i in range(2,21):
    ans = ans* i // (gcd(ans,i))
print(ans)
print('Time Taken {:.6f} sec!!'.format(time.time()-start))