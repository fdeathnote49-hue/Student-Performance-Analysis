import pandas as pd

# Excel file ka path
file_path = "../Dataset/student_performance.xlsx"

# Excel file read karna
df = pd.read_excel(file_path)

print("===== Student Performance Dataset =====")
print(df)
print("\n========== First 5 Records ==========")
print(df.head())

print("\n========== Last 5 Records ==========")
print(df.tail())

print("\n========== Dataset Shape ==========")
print(df.shape)

print("\n========== Column Names ==========")
print(df.columns)

print("\n========== Dataset Information ==========")
print(df.info())

print("\n========== Statistical Summary ==========")
print(df.describe())
print("\n========== Missing Values ==========")
print(df.isnull().sum())

print("\n========== Duplicate Records ==========")
print(df.duplicated().sum())
print("\n========== Average Percentage ==========")
print("Average Percentage :", round(df["Percentage"].mean(), 2))

print("\n========== Highest Scorer ==========")
print(df.loc[df["Percentage"].idxmax()])

print("\n========== Lowest Scorer ==========")
print(df.loc[df["Percentage"].idxmin()])
# Department-wise Average Percentage
department_avg = df.groupby("Department")["Percentage"].mean()

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
department_avg.plot(kind="bar")

plt.title("Department-wise Average Percentage")
plt.xlabel("Department")
plt.ylabel("Average Percentage")

plt.tight_layout()

plt.savefig("../Dashboard_Screenshots/department_average.png")

plt.show()
# Attendance Bar Chart

plt.figure(figsize=(10,5))

plt.bar(df["Student_Name"], df["Attendance"])

plt.title("Student Attendance")

plt.xlabel("Student Name")

plt.ylabel("Attendance (%)")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("../Dashboard_Screenshots/attendance_chart.png")

plt.show()
# Percentage Histogram

plt.figure(figsize=(8,5))

plt.hist(df["Percentage"], bins=5)

plt.title("Percentage Distribution")

plt.xlabel("Percentage")

plt.ylabel("Number of Students")

plt.tight_layout()

plt.savefig("../Dashboard_Screenshots/percentage_histogram.png")

plt.show()