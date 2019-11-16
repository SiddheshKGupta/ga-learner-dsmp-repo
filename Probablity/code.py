# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
total_fico = len(df['fico'])
A = len(df[df['fico']>700])
p_a = A/total_fico
total_pur = len(df['purpose'])
B = len(df[df['purpose'] == 'debt_consolidation'])
p_b = B/total_pur
df1 = pd.DataFrame(df[df['purpose'] == 'debt_consolidation'])
p_a_b = p_b/p_a
result = p_a_b==p_a
result

# code ends here


# --------------
# code starts here
pb = len(df['paid.back.loan'])
y = len(df[df['paid.back.loan']=='Yes'])
prob_lp = y/pb
cp = len(df['credit.policy'])
cy = len(df[df['credit.policy']=='Yes'])
prob_cs = cy/cp
new_df = pd.DataFrame(df[df['paid.back.loan']=='Yes'])
prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0] / new_df.shape[0]
bayes = (prob_pd_cs * prob_lp)/ prob_cs
bayes
# code ends here


# --------------
# code starts here
df['purpose'].value_counts().plot(kind='bar')
df1 = pd.DataFrame(df[df['paid.back.loan']=='No'])
df1['purpose'].value_counts().plot(kind='bar')
# code ends here


# --------------
# code starts here
inst_median = np.median(df['installment'])
inst_mean = df['installment'].mean()
df['installment'].hist(bins=8)
df['log.annual.inc'].hist(bins=8)
# code ends here


