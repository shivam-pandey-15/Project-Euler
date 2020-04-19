import time

def palindrome(n):

    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


start = time.time()

for i in range(999,0,-1):
    for j in range(999,990,-1):
        if palindrome(i*j):
            print(i*j)
            print('Time taken {:.6} secs!!'.format(time.time()-start))
            exit()
