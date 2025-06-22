# Riverbank Displacement Trend Prediction Using Linear Regression

This project presents a simple yet insightful model to analyze and predict riverbank displacement over time at specific sampling locations. Using linear regression, it forecasts future displacements based on past trends and visualizes results in a clear comparative bar chart.

## 🎯 Objective

To analyze riverbank displacement across three decades (2004–2014, 2014–2024, and 2024–2034) using historical data and linear regression. The project estimates future displacement distances to support sustainable riverbank management and environmental planning.

## 🧠 Aim of the Project

- Understand the "trend" of riverbank shifts over time.
- "Predict future displacement" using a basic regression model.
- Assist in "climate resilience", "buffer zone policy", and "urban planning".
- Serve as a reproducible tool for "environmental planners", "hydrologists", and "GIS analysts".

## 📊 Data Requirements

| Parameter                         | Description                                     |
|----------------------------------|-------------------------------------------------|
| Sampling Locations               | E.g., A, B, C (representing fixed GPS sites)    |
| Displacement 2004–2014 (meters)  | Distance the riverbank shifted in that decade   |
| Displacement 2014–2024 (meters)  | Measured distance for the next decade           |

## 🔁 Step-by-Step Workflow

###  1. Import Libraries
- `matplotlib`, `numpy`, `pandas`, `scikit-learn`

###  2. Define Input Data
- Locations: A, B, C
- Historical displacements for two decades

###  3. Train Linear Regression Models
- Input decades as 1 and 2
- Fit models to predict decade 3 (2024–2034)

###  4. Generate Predictions
- Predict displacement for each location for 2024–2034

### ✅ 5. Export to CSV
- Save all values (past and predicted) into a structured `.csv` file

### ✅ 6. Visualization
- Create a grouped bar chart comparing all three decades
- Save the chart as a `.png` image

## 📂 Output Files

- `example_outputs/riverbank_displacement_predictions.csv`
- `example_outputs/riverbank_displacement_prediction_plot.png`

## 🖼️ Output Example

![Riverbank Displacement Plot](example_outputs/riverbank_displacement_prediction_plot.png)

## 📦 Installation & Usage

### ▶️ Install Required Libraries
```bash
pip install -r requirements.txt

