import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Best-fit Line Finder")

n = st.number_input("Enter number of points:", min_value=1, step=1)

x_values = []
y_values = []

for i in range(n):
    x = st.number_input(f"Enter x[{i+1}]:", key=f"x_{i}")
    y = st.number_input(f"Enter y[{i+1}]:", key=f"y_{i}")
    x_values.append(x)
    y_values.append(y)

if st.button("Plot Best-fit Line"):
    x = np.array(x_values)
    y = np.array(y_values)

    m, b = np.polyfit(x, y, 1)
    y_fit = m * x + b

    fig, ax = plt.subplots()
    ax.scatter(x, y, color='blue', label="Data Points")
    ax.plot(x, y_fit, color='red', label=f"Best-fit line: y = {m:.2f}x + {b:.2f}")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Best-fit Line for Given Points")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    st.success(f"Equation: y = {m:.2f}x + {b:.2f}")
    st.info(f"Slope (m): {m:.2f}")

