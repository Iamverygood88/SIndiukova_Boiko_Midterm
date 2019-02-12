import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("assets/traa_data2.csv")
Number_of_eggs_received = data["Number of eggs received"]
Years = data["Year"]
Number_of_eggs_hatched = data['Number of eggs hatched/released']


plt.scatter(Years, Number_of_eggs_received, 100, color="#767b75")
plt.scatter(Years, Number_of_eggs_hatched, 100, color="#de6526")
plt.legend(loc=1)
plt.axis("equal")
plt.xlabel("Years")
plt.ylabel("Eggs Amount")
plt.title("Fish Eggs Comparison")


plt.show()
