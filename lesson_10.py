import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#дз 10.1

data_list = [1, 2, 3, 4, 5]
series_from_list = pd.Series(data_list)
print("Series from list:\n", series_from_list)

data_numpy = np.array([6, 7, 8, 9, 10])
s = pd.Series(data_numpy)
print("\nSeries from NumPy array:\n", s)

data_dict = {'A': 11, 'B': 12, 'C': 13}
series_from_dict = pd.Series(data_dict)
print("\nSeries from dictionary:\n", series_from_dict)

data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

#дз 10.2

series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([3, 5, 6, 7, 8])

unique_to_series1 = series1[~series1.isin(series2)]
unique_to_series2 = series2[~series2.isin(series1)]

print("\nUnique to series1:", unique_to_series1.values)
print("Unique to series2:", unique_to_series2.values)

#дз 10.3

series3 = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
value_counts = series3.value_counts()
print("\nValue counts:", value_counts)

plt.figure(figsize=(8, 6))
plt.bar(value_counts.index, value_counts.values)
plt.xlabel("Уникальные элементы")
plt.ylabel("Частота")
plt.title("Гистограмма частоты")
plt.show()

#дз 10.4

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

vertical_concat = pd.concat([df1, df2], ignore_index=True)
print("\nVertical concatenation:\n", vertical_concat)
df1['C'] = [9, 10]
horizontal_concat = pd.concat([df1, df2], axis=1)
print("\nHorizontal concatenation:\n", horizontal_concat)

# дз 10.5

df3 = pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [2, 4, 1, 3, 5]})

plt.figure(figsize=(8, 6))
plt.plot(df3['X'], df3['Y'], marker='o', linestyle='-')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("График Y от X")
plt.show()