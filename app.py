# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Load datasets
train_features = pd.read_csv('data/clean/train_features.csv')
train_labels = pd.read_csv('data/clean/train_labels.csv')

# Convert 'week_start_date' to datetime if it's not already
train_features['week_start_date'] = pd.to_datetime(train_features['week_start_date'])

# Merge 'total_cases' into train_features for plotting
train_data_merged = train_features.merge(train_labels[['year', 'weekofyear', 'total_cases']], on=['year', 'weekofyear'], how='left')

# Streamlit app
st.title('DengAI: Predicting Disease Spread')

st.write("""
This Streamlit app uses Plotly Express to display total cases of Dengue Fever over time in two cities: San Juan (Puerto Rico) and Iquitos (Peru).
         
We predicted local epidemics of dengue fever to help fight life-threatening pandemics. 
         
Do you notice any patterns?
""")

# Plotting with Plotly Express
fig = px.scatter(train_data_merged,
                 x='week_start_date', 
                 y='total_cases', 
                 color='city',
                 title='Total Cases Over Time by City',
                 labels={'week_start_date': 'Week Start Date', 'total_cases': 'Total Cases'},
                 hover_data=['city'])

fig.update_layout(xaxis_title='Week Start Date', yaxis_title='Total Cases')
fig.update_xaxes(tickangle=45)

st.plotly_chart(fig, use_container_width=True)

st.write("""

The project was created as an entry to the [DengAI: Predicting Disease Spread](https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/page/80/) competition hosted by [Driven Data](https://www.drivendata.org/). 

To find out more about how we interpreted this dataset, see [DengAI](https://github.com/carecodeconnect/dengai)
""")
