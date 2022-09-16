import matplotlib.pyplot as plt

x = ["A", "B", "C", "D", "E", "F", "G", "H"]
y = [50, 85.2, 65.2, 85, 45, 120, 51, 100]

fig, ax = plt.subplots(figsize=(10, 7))
ax.bar(x=x, height=y, width=0.6, align="center", color="grey", edgecolor="red", linewidth=2.0)
ax.set_title("Adjust Styles of plot", fontsize=15)
plt.show()
