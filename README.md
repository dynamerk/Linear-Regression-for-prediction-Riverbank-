Riverbank Displacement Trend Prediction Using Linear Regression

This project presents a simple yet insightful model to analyze and predict riverbank displacement over time at specific sampling locations. Using "linear regression", it forecasts future displacements based on past trends and visualizes the results using a comparative bar chart.

## 🎯 Objective

To analyze riverbank displacement across three decades (2004–2014, 2014–2024, and 2024–2034) using historical data and linear regression. The project estimates future displacement distances to support "sustainable riverbank management" and "environmental planning".

## 🧠 Aim of the Project

* Understand the "trend" of riverbank shifts over time
* Predict "future displacement" using basic regression
* Support "climate resilience", "buffer zone policy", and "urban planning"
* Serve as a reproducible tool for:

  * Environmental planners
  * Hydrologists
  * GIS analysts
## 📊 Data Requirements

| Parameter                       | Description                             |
| ------------------------------- | --------------------------------------- |
| Sampling Locations              | E.g., A, B, C (representing GPS sites)  |
| Displacement 2004–2014 (meters) | Riverbank shift during the first decade |
| Displacement 2014–2024 (meters) | Measured shift for the second decade    |

## Step-by-Step Workflow

1. Import Libraries
   Required: `matplotlib`, `numpy`, `pandas`, `scikit-learn`

2. Define Input Data
   Locations = A, B, C
   Historical displacement data for two decades

3. Train Regression Model
   Fit linear regression for each location
   Use decades as \[1, 2] and predict for \[3] (2024–2034)

4. **Generate Predictions**
   Predict displacement for the third decade

5. Export to CSV
   Save data (past + prediction) to `.csv` file

6. Visualization
   Create grouped bar chart comparing the three decades
   Save as `.png` image

##  Code (Python)

```python
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
```

## 📂 Output Files

| File Path                                    | Description                                         |
| -------------------------------------------- | --------------------------------------------------- |
| `riverbank_displacement_predictions.csv`     | Contains displacement data (historical + predicted) |
| `riverbank_displacement_prediction_plot.png` | Bar chart comparing displacements across decades    |


## ▶️ Install Required Libraries

To run the script, install the dependencies:

```bash
pip install matplotlib numpy pandas scikit-learn
```

Or use a `requirements.txt`:

```
matplotlib
numpy
pandas
scikit-learn
```

Then run:

```bash
pip install -r requirements.txt
```
