import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("assets/catch.csv")

Creek_Name = data["Creek Name"]
Years = data["Year"]
Number_of_fish_caught = data['Number of Fish Caught']


plt.bar(Creek_Name, Number_of_fish_caught, color="#636664")
plt.legend(loc=1)
plt.xlabel("Names")
plt.ylabel("Number of Fish")
plt.title("Rainbow Trout Anglers")


plt.show()
