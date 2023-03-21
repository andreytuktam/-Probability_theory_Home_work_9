import numpy as np
import scipy.stats as st

iq = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])

print(st.t.interval(confidence = 0.95, df = len(iq) - 1, loc = np.mean(iq), scale = st.sem(iq)))
