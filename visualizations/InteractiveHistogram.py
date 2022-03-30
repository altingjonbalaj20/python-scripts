import matplotlib.pyplot as plt
#Setting up the base plot size
fig, ax = plt.subplots(figsize = (8,6))

# Plot histogram
dataset['score'].plot(kind = "hist", density = True)
# change density to true, because KDE uses density
# Plot KDE
dataset['score'].plot(kind = "kde")
# Plot the graph
plt.show()