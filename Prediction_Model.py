import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

# Sampling locations
locations = ['A', 'B', 'C']

# Known displacement distances per decade (meters)
displacement_2004_2014 = [200, 1423.53, 537]
displacement_2014_2024 = [575, 110, 527]

# Prepare data for regression
X_train = np.array([[1], [2]])
X_pred = np.array([[3]])

# Predict displacement for 2024-2034
predicted_2024_2034 = []
for i in range(len(locations)):
    y_train = np.array([displacement_2004_2014[i], displacement_2014_2024[i]])
    model = LinearRegression()
    model.fit(X_train, y_train)
    pred = model.predict(X_pred)[0]
    predicted_2024_2034.append(pred)
    print(f"Predicted displacement at {locations[i]} for 2024–2034: {pred:.2f} meters")

# Export to CSV
df = pd.DataFrame({
    'Location': locations,
    'Displacement 2004-2014 (m)': displacement_2004_2014,
    'Displacement 2014-2024 (m)': displacement_2014_2024,
    'Predicted Displacement 2024-2034 (m)': predicted_2024_2034
})
csv_path = r'C:\Users\dynam\Downloads\riverbank_displacement_predictions.csv'
df.to_csv(csv_path, index=False)
print(f"\nCSV saved to: {csv_path}")

# Plotting
x = np.arange(len(locations))
width = 0.25
fig, ax = plt.subplots(figsize=(9, 6))
bars1 = ax.bar(x - width, displacement_2004_2014, width, label='2004–2014')
bars2 = ax.bar(x, displacement_2014_2024, width, label='2014–2024')
bars3 = ax.bar(x + width, predicted_2024_2034, width, label='Predicted 2024–2034')

ax.set_xlabel('Sampling Location')
ax.set_ylabel('Displacement (meters)')
ax.set_xticks(x)
ax.set_xticklabels(locations)
ax.legend()

# Add labels
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

plt.tight_layout()

# Save plot image
img_path = r'C:\Users\dynam\Downloads\riverbank_displacement_prediction_plot.png'
plt.savefig(img_path)
print(f"Plot saved to: {img_path}")

plt.show()
