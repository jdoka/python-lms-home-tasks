import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def is_good_wine(quality):
    if quality > 6:
        return 1
    else:
        return 0


# 1
red_wine = pd.read_csv('winequality-red.csv')

# 2
with_empty_cell_rows = red_wine[red_wine.isnull().any(axis=1)]
print(with_empty_cell_rows.empty)  # true - нет строк с пропущенными ячейками

# 3
red_wine['good'] = red_wine['quality'].apply(lambda x: is_good_wine(x))

q1 = red_wine['quality'].quantile(0.25)
q3 = red_wine['quality'].quantile(0.75)
iqr = (q3 - q1)
r1 = q1 - 1.5 * iqr
r3 = q3 + 1.5 * iqr
print(r1)
print(r3)

red_wine = red_wine[red_wine['quality'] < r3]
red_wine = red_wine[red_wine['quality'] > r1]

print(red_wine)

print(red_wine['quality'].hist())


sns.histplot(data=red_wine, x='quality', kde=True)
plt.show()