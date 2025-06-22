# 📈 Riverbank Displacement Trend Prediction Using Linear Regression

This project presents a simple yet insightful model to analyze and predict riverbank displacement over time at specific sampling locations. Using **linear regression**, it forecasts future displacements based on past trends and visualizes the results using a comparative bar chart.

## 🎯 Objective

To analyze riverbank displacement across three decades (2004–2014, 2014–2024, and 2024–2034) using historical data and linear regression. The project estimates future displacement distances to support **sustainable riverbank management** and **environmental planning**.

## 🧠 Aim of the Project

- Understand the **trend** of riverbank shifts over time  
- Predict **future displacement** using basic regression  
- Support **climate resilience**, **buffer zone policy**, and **urban planning**  
- Serve as a reproducible tool for:  
  - Environmental planners  
  - Hydrologists  
  - GIS analysts  

## 📊 Data Requirements

| Parameter                     | Description                          |
|------------------------------|------------------------------------|
| Sampling Locations            | E.g., A, B, C (representing GPS sites) |
| Displacement 2004–2014 (meters) | Riverbank shift during the first decade |
| Displacement 2014–2024 (meters) | Measured shift for the second decade |

## Step-by-Step Workflow

1. Import Libraries  
   Required: `matplotlib`, `numpy`, `pandas`, `scikit-learn`  

2. Define Input Data 
   Locations: A, B, C  
   Historical displacement data for two decades  

3. Train Regression Model  
   Fit linear regression for each location  
   Use decades as `[1, 2]` and predict for `[3]` (2024–2034)  

4. Generate Predictions
   Predict displacement for the third decade  

5. Export to CSV  
   Save data (historical + predicted) to `.csv` file  

6. Visualization
   Create grouped bar chart comparing displacements across the three decades  
   Save as `.png` image  

## Example to Save Plot Image

```python
img_path = r'C:\Users\dynam\Downloads\riverbank_displacement_prediction_plot.png'
plt.savefig(img_path)
print(f"Plot saved to: {img_path}")

