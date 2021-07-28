#Выставление времени
import time
start_time = time.monotonic()
time.sleep(5)
print(f'Прошло{time.monotonic() - start_time}')

n = int(input(''))
s = 0
k = 0
while k < n:
    k = k + 1
    s = s + 1
    print(n, s)

