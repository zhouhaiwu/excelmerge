import pyprind
import time

n = 50
bar = pyprind.ProgBar(n, monitor=True)
for i in range(50):
    time.sleep(0.15)
    bar.update()
print(bar)