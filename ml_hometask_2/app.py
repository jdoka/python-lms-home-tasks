import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def is_good_wine(quality):
    if quality >= 6:
        return 1
    else:
        return 0


# Этап 3

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

red_wine_filtered = red_wine[red_wine['quality'] < r3]
red_wine_filtered = red_wine_filtered[red_wine['quality'] > r1]


# 4
print(red_wine_filtered['quality'].hist())

sns.histplot(data=red_wine_filtered, x='quality', kde=True)
# plt.show()

print("Medians: ")
for column in red_wine_filtered.columns:
    median = red_wine_filtered[column].median()
    print(f"{red_wine_filtered[column].name}: {median}")

red_wine_filtered.boxplot(column=['quality'])
# plt.show()

# Этап 4
red_wine_filtered.hist()
#plt.show()

print("Correlation matrix: ")
pd.set_option('display.max_columns', None)
print(red_wine_filtered.corr().head(10))


# Этап 5
print("Test answers: ")
#1
print(red_wine.shape[0]-red_wine_filtered.shape[0])
#2
red_wine_not_good = red_wine_filtered[red_wine_filtered['good'] == 0]
print(100* red_wine_not_good.shape[0]/red_wine_filtered.shape[0])
#3
print(red_wine_filtered['total sulfur dioxide'].median())
#4 см. пересечение density и sulphates в red_wine_filtered.corr(), равно 0.157177 < 0.2
#5 не влияет
