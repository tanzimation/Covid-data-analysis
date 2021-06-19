import matplotlib.pyplot as plt
import time as t
import numpy as np

print("Press enter to see updates in scatter plot")
entrance = input("Type 'scatter plot' to get the updates in scatter plot:")

while True:
    if entrance == 'Scatter plot'.lower():
        break
    else:
        entrance = input("Type 'scatter plot' correctly again:".lower())
print("Thanks. Wait 2 seconds.")

t.sleep(2)

Metrics = ["Vaccinations", "Tests", "Hospital", "Confirmed cases", "Confirmed death",
           "Reproduction rate", "Policy responses", "Other interests"]
Countries_numbers = [209, 129, 33, 191, 183, 182, 181, 218]

plt.scatter(Metrics, Countries_numbers, label='none', color="r")

plt.title("Latest updates on Covid-19(June 2021). Type 'Scatter plot or Histogram")
plt.xlabel('Metrics')
plt.ylabel('Numbers of countries')
plt.legend()
plt.xticks(Metrics, Countries_numbers)
plt.show()

print("Press enter to see updates in stack plots")
entrance = input("Type 'stack plot' to get the updates in stack plot:")

while True:
    if entrance == 'Stack plot'.lower():
        break
    else:
        entrance = input("Type 'stack plot' correctly again:")
print("Thanks. Wait 2 seconds.")

t.sleep(2)


Metrics = ["Vaccinations", "Tests", "Hospital", "cases", "death",
           "Reproduction", "Policy", "Others"]
Countries_numbers = [209, 129, 33, 191, 183, 182, 181, 218]


plt.title("Latest updates on Covid-19(June 2021). Type 'Scatter plot or Histogram")
plt.xlabel('Metrics')
plt.ylabel('Numbers of countries')
plt.legend()
plt.stackplot(Metrics, Countries_numbers)
plt.show()

print("Press enter to see updates in Histogram")
entrance = input("Type 'histogram' to get the updates in Histogram:")

while True:
    if entrance == 'Histogram'.lower():
        break
    else:
        entrance = input("Type 'histogram' correctly again:")
print("Thanks. Wait 2 seconds.")

t.sleep(2)


Metrics = ["Hospital", "Tests", "P", "R", "vaccination", "cases", "death",
           "Others"]
Bins = [33, 129, 181, 182, 183, 191, 209, 218]

plt.bar(Metrics, Bins, label='bar', color='g')
plt.title("Latest updates on Covid -19 till June 2021")
plt.xlabel('Metrics')
plt.ylabel('Numbers of countries')
plt.legend()
plt.show()


print("Thanks for checking.")