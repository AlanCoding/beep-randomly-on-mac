import random
import time
from math import exp

for i in range(100):
  r = random.randint(0, 100)
  time.sleep(100./r)
  print('\a')

