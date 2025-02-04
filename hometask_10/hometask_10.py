import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open("events.json", "r") as file:
    data = json.load(file)
    df = pd.DataFrame(data["events"])

plt.figure(figsize=(12, 8))
sns.countplot(data=df, x="signature")

plt.title("Распределение типов событий ИБ")
plt.xticks(rotation=90)
plt.show()
