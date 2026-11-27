import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load employee data
df = pd.read_csv("data/employees.csv")

# Display employee data
print("Employee Data:")
print(df.head())

# Display information
print("\nEmployee Information:")
df.info()

# Calculate average salary
print("\nAverage Salary:")
print(df["salary"].mean())

# Department summary
summary = df.groupby("department")["salary"].mean()

print("\nDepartment Summary:")
print(summary)

# Create bar chart
summary.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.tight_layout()
plt.savefig("reports/salary_chart.png")
plt.show()