import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Best-fit Line Finder")

# Input number of points
n = st.number_input("Enter number of points:", min_value=1, step=1)

x_values = []
y_values = []

# Collect x and y values with 5 decimal places
for i in range(n):
    x = st.number_input(f"Enter x[{i+1}]:", key=f"x_{i}", format="%.5f")
    y = st.number_input(f"Enter y[{i+1}]:", key=f"y_{i}", format="%.5f")
    x_values.append(x)
    y_values.append(y)

if st.button("Plot Best-fit Line"):
    x = np.array(x_values)
    y = np.array(y_values)

    # Compute best-fit line
    m, b = np.polyfit(x, y, 1)
    y_fit = m * x + b

    # Plot the graph
    fig, ax = plt.subplots()
    ax.scatter(x, y, color='blue', label="Data Points")
    ax.plot(x, y_fit, color='red', label=f"Best-fit line: y = {m:.5f}x + {b:.5f}")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Best-fit Line for Given Points")
    ax.legend()
    ax.grid(True)

    # Display the plot in Streamlit
    st.pyplot(fig)

    # Show equation with 5 decimal places
    st.success(f"Equation: y = {m:.5f}x + {b:.5f}")
    st.info(f"Slope (m): {m:.5f}")
