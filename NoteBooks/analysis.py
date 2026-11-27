import pandas as pd
import matplotlib.pyplot as plt# %% [markdown]
# Employee Data Analysis
# 
# ## Introduction
# This project analyzes employee data using Python.
# 
# ## Objectives
# - Load employee data
# - Analyze employee salary
# - Calculate average salary
# - Create charts

# %%
df = pd.read_csv("../employees.csv")

# %%
print(df.head())

print(df.info())

print(df.describe())

# %% [markdown]
# # Employee Data Analysis
# 
# ## 1. Import Libraries
# 
# This project uses Pandas and Matplotlib
# for employee data analysis.

# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../employees.csv")

print(df.head())

df.info()

print(df.describe())

print("Average Salary:", df["salary"].mean())

print("Total Employees:", len(df))

print("Columns:", df.columns)

df.info()

print(df.describe())
# %%
print("Total Employees:", len(df))

print("Columns:", df.columns)

print(df.info())

print(df.describe())

# %%
print(df.columns.tolist())


# %%
df.columns = df.columns.str.strip()
print(df.columns.tolist())

# %%
print(df.head())
print(df.columns.tolist())

# %%
print(df["department"].value_counts())

# %%
print("Average Salary:", df["salary"].mean())

# %%
print("Highest Salary:", df["salary"].max())

# %%
print("Lowest Salary:", df["salary"].min())

# %%
high_salary = df[df["salary"] > 60000]

print(high_salary)

# %%
avg_salary = df.groupby("department")["salary"].mean()

print(avg_salary)

# %%
import matplotlib.pyplot as plt

avg_salary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()

#%%
plt.figure(figsize=(8, 5))

avg_salary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.savefig("../Reports/salary_chart.png")

plt.show()

# %%



