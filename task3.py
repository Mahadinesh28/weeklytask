import numpy as np

marks = np.array([
    [80, 75, 85],
    [85, 80, 70],
    [90, 85, 95],
    [70, 75, 80]])

print("Shape:", marks.shape)

print("Student averages:", marks.mean(axis=1))

print("Subject averages:", marks.mean(axis=0))

grace_marks = marks + 5

print("Grace marks:")
print(grace_marks)

weights = np.array([0.5, 0.3, 0.2])

weighted_scores = np.dot(grace_marks, weights)

print("Weighted scores:", weighted_scores)

import pandas as pd

df = pd.read_csv("employees.csv")

print("\nEmployee Data:")
print(df)

print("\nData Information:")
df.info()

print("\nDescription:")
print(df.describe())

print("\nLOC:")
print(df.loc[0:2, ["name", "salary"]])

print("\nILOC:")
print(df.iloc[0:3, 0:4])

print("\nSalary above 50000:")
print(df[df["salary"] > 50000])

df["salary"] = pd.to_numeric(
    df["salary"], errors="coerce")

print("\nMissing values:")
print(df.isnull().sum())

median_salary = df["salary"].median()

df["salary"] = df["salary"].fillna(median_salary)

df = df.drop_duplicates()

df["id"] = df["id"].astype(int)

print("\nCleaned Data:")
print(df)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

summary = df.groupby("department").agg(
    headcount=("name", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max"))

print("\nDepartment Summary:")
print(summary)

departments = pd.read_csv("departments.csv")

inner = pd.merge(
    departments, summary,
    on="department",
    how="inner")

print("\nInner Join:")
print(inner)

left = pd.merge(
    departments, summary,
    on="department",
    how="left")

print("\nLeft Join:")
print(left)

outer = pd.merge(
    departments, summary,
    on="department",
    how="outer")

print("\nOuter Join:")
print(outer)

empty_departments = departments.merge(
    summary.reset_index(),
    on="department",
    how="left",
    indicator=True)

print("\nDepartments without employees:")
print(empty_departments[
        empty_departments["_merge"] == "left_only"]["department"]
)

import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

summary["average_salary"].plot(
    kind="bar",
    title="Average Salary by Department",
    legend=True)

plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.savefig("charts/bar_chart.png")
plt.show()
plt.close()

print("Insight: The bar chart compares average salaries.")

plt.hist(df["salary"], bins=5, edgecolor="black")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend(["Salary"])
plt.tight_layout()
plt.savefig("charts/histogram.png")
plt.show()
plt.close()

print("Insight: The histogram shows salary distribution.")

plt.scatter(df["id"], df["salary"], label="Employees")

plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("charts/scatter_chart.png")
plt.show()
plt.close()

print("Insight: The scatter plot compares employee IDs and salaries.")

sorted_df = df.sort_values("id")

plt.plot(
    sorted_df["id"],
    sorted_df["salary"],
    marker="o",
    label="Salary"
)

plt.title("Employee Salary Line Chart")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("charts/line_chart.png")
plt.show()
plt.close()

print("Insight: The line chart shows salary changes by employee ID.")