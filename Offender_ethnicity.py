import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import janitor
from openpyxl import load_workbook

location_data = pd.read_csv('Offender_ethnicity.csv')

fig = px.bar(location_data, x='key', y='value', 
             title="Offender ethnicity Distribution",
             labels={'key': 'Victim Type', 'value': 'Count'},
             color='key', color_continuous_scale='Viridis')
fig.update_layout(xaxis_tickangle=-45)
fig.show()

location_data_correlation = location_data.set_index('key')

plt.figure(figsize=(10, 6))
sns.heatmap(location_data_correlation.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap for Victims')
plt.show()

fig = px.scatter(location_data, x='key', y='value', 
                 title="Scatter Plot: Offender ethnicity vs. Value",
                 labels={'key': 'Offender ethnicity', 'value': 'Value'},
                 color='key', size='value', hover_data=['key'])
fig.update_layout(xaxis_tickangle=-45)
fig.show()

print("Summary statistics for 'value' column:")
print(location_data['value'].describe())

fig = px.box(location_data, x='key', y='value', points="all",
             title="Value Distribution Across Offender ethnicity",
             labels={'key': 'Offender ethnicity', 'value': 'Value'})
fig.show()
