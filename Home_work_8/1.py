import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

cov = np.mean(zp * ks) - np.mean(zp) * np.mean(ks)
print("cov 1 =", cov)
print("cov 2 =", np.cov(zp, ks, ddof = 0))

print("corrcoef 1 =", np.cov(zp, ks, ddof = 0) / (np.std(zp, ddof = 0) * np.std(ks, ddof = 0)))
print("corrcoef 2 =", np.corrcoef(zp, ks))

df = pd.DataFrame({'zp': [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
    'ks': [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]}) 
print("corrcoef 3 =", df['zp'].corr(df['ks']))

# plt.scatter(zp, ks)
# plt.title('корреляция zp/ks')
# plt.xlabel('zp')
# plt.ylabel('ks')
# plt.show()
