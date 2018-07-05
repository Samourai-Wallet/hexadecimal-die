# - *- coding: utf- 8 - *-

import numpy as np
from scipy import stats

# dice is 16-sided so every array has 16 elements
# one array means one approach and we are supposing first time there is no expected distibition

dice = np.array([ [10,4,2,9,5,8,7,3,2,8,5,6,6,4,2,4], [12,2,4,5,2,9,7,4,9,7,9,2,8,3,2,5], [10,2,0,4,6,8,7,5,5,5,8,6,7,1,4,4]])

chi2_stat, p_val, dof, ex = stats.chi2_contingency(dice)

print("\n===Chi2 Stat===")
print(chi2_stat)
print("\n===Degrees of Freedom===")
print(dof)
print("\n===P-Value===")
print(p_val)
if(p_val > 0.05):
    print("\nNotice: high value here means that there are not enough rolls in contingency table\n or your dice is not fair and results will repeat itself in the future with probability {0:1.2f}.\n You can expect that results will be around contingency table values coming next to this message.".format(p_val))
print("\n===Contingency Table===")
print(ex)

print("\n===Checking versus uniform distibition===")

rolls = np.sum(dice)
n_cat = len(dice[0])
my_rolls_expected = np.full(n_cat, 1.*rolls/n_cat)
my_rolls_actual = [np.sum(i) for i in dice.transpose()]

print("For {} categories and {} rolls the expected uniform frequency is {}".format(n_cat, rolls, my_rolls_expected[0]))
print("Actual rolls: {}".format(my_rolls_actual))

chi2_stat, p_val = stats.chisquare(my_rolls_actual, my_rolls_expected)
print("\n===Chi2 Stat===")
print(chi2_stat)
print("\n===P-Value===")
print(p_val)
if(p_val < 0.05):
    print("\nWarning: the dice is not fair! The null hypothesis test failed!\n")
else:
    print("\nNull hypothesis test passed statistically significant pvalue.\n")
