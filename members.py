import csv
import numpy as np
import matplotlib.pyplot as plt
Year_2002 = []
Year_2018 = []


categories = []

with open ("assets/traa_data.csv") as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1
        else:
            if row[0] == "2002":
                Year_2002.append([int(row[0]), row[1]])
            elif row[0] == "2018":
                Year_2018.append([int(row[0]), row[1]])
            line_count += 1

print("processed", line_count, "rows of data")
print("2002:", len(Year_2002))
print("2018:", len(Year_2018))





labels = ["2002","2006","2010", "2014", "2018"]
values = [52, 45, 65, 55, 80]

amount = np.arange(len(labels))


plt.bar(amount, values, color="#1e393c")
plt.xticks(amount, labels)
plt.xlabel('Years')
plt.ylabel('Amount of Members')
plt.title('Members Flow')
plt.legend()
plt.show()
