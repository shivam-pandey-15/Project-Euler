import time

start = time.time()
sum_of_square = sum([i**2 for i in range(1,101)])
square_of_sum = sum([i for i in range(1,101)])**2

print(abs(sum_of_square-square_of_sum))
print('Time Taken {:.6f} sec!!'.format(time.time()-start))