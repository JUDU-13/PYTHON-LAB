import scipy.stats as stats
female = [60, 54, 46, 41]
male = [40, 44, 53, 57]
rt = [201, 194]
ct = [100, 98, 99, 98]
fem_mul = (rt[0]/395) # 395 = grand_total
male_mul = (rt[1]/395)
female_col_mul, male_col_mul, female_Es, male_Es = [], [], [], []

for i in ct:
    female_col_mul.append(round(i * fem_mul, 4))
    male_col_mul.append(round(i * male_mul, 4))
print(f"Female exp value: {female_col_mul}\nMale exp value: {male_col_mul}")

# O : Observed Values, E : Expected Value
O = female +  male
E = female_col_mul + male_col_mul
print(f"All observations: {O}\nAll Expectations: {E}")
res = 0
for i in range(len(O)):
    res += (pow((O[i] - E[i]), 2) / E[i])
check = stats.chisquare(O, E)
lst = list(check)
print(f"Chi Square value: {round(res, 4)}\nVerification: {check}")
if lst[1] > 0.05: 
    print(f"We accept Null Hypothesis, since {round(lst[1], 5)} > 0.05")
else:
    print("We reject Null Hypothesis")
