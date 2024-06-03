import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 

plt.style.use('seaborn-v0_8-darkgrid')

x_totals = [741, 753, 723, 202, 275] #collected per gene

def expected_unlinked_distribution(totals):
    """Expects int of total progeny counted)
    Returns y-axis list of 9:3:3:1 ratio values of total in that order"""
    ratio = np.array([9,3,3,1])/16
    total = sum(totals)
    print(total)

    total_list = np.full((4), total)
    expected = total_list*(ratio)

    return expected

def calc_proportion(total, value):
    return list((np.array(value))/total)

X = ['WT', 'WT GFP', 'Dpy GFP', 'Dpy']
X_axis = np.arange(len(X))

wT_GFP = [406, 458, 403, 130, 157]
wT_noGFP = [171, 176, 140, 43, 66]
Dpy_GFP = [113, 91, 67, 25, 47]
Dpy_noGFP = [51, 28, 67, 4, 5]

gfp1 = [406, 171, 113, 51]
gfp2 = [458, 176, 91, 28]
gfp3 = [403, 140, 25, 67] 
gfp4 = [130, 43, 25, 4]
gfp5 = [157, 66, 47, 5] 

# Calculate expected values
y_expected = expected_unlinked_distribution(x_totals)
y_expected_proportions = calc_proportion(sum(x_totals), y_expected)
# Plot bars
bar_width = 0.1
plt.bar(X_axis + 2*bar_width, calc_proportion(x_totals[0], gfp1), bar_width, label='GFP1')
plt.bar(X_axis + bar_width, calc_proportion(x_totals[1], gfp2), bar_width, label='GFP2')
plt.bar(X_axis, calc_proportion(x_totals[2], gfp3), bar_width, label='GFP3')
plt.bar(X_axis - bar_width, calc_proportion(x_totals[3], gfp4), bar_width, label='GFP4')
plt.bar(X_axis - 2*bar_width, calc_proportion(x_totals[4], gfp5), bar_width, label='GFP5')

# Add expected value lines above each subgroup
for i, (expected) in enumerate(zip(y_expected_proportions)):
    plt.hlines(y=expected, xmin=X_axis[i] - 2.5*bar_width, xmax=X_axis[i] + 2.5*bar_width, color='black', linestyles='--', linewidth=1)
plt.plot(np.random.rand(0), linestyle='--', color='black', label='Expected')
plt.xticks(X_axis, X)
plt.xlabel("Phenotype")

plt.ylabel('Proportion of Population')
plt.legend()

# plt.savefig('Lab4AnalysisFigure')
plt.show()