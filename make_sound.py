import random
import time
from math import exp
import sys

for i in range(100):
  r = random.randint(0, 100)
  time.sleep(100./r)
  sys.stdout.write('\a')
  sys.stdout.flush()

