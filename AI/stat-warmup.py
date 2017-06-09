import numpy as np
import scipy.stats as st
n = int(input().strip())
from math import sqrt

num_array = [int(x) for x in input().strip().split(' ')]
num_array = np.array(num_array)
mean = np.mean(num_array)
median = np.median(num_array)
std = np.std(num_array)
print(mean)
print(median)
print(np.argmax(np.bincount(num_array)))
print("%.1f" % std )

mean_conf = st.norm.interval(0.950002, loc=mean, scale=std/sqrt(n))
print("%.1f %.1f" % (mean_conf[0], mean_conf[1]))
