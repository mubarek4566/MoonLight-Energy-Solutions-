import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import os
import sys

# loading modules 
sys.path.append(os.path.abspath('../scripts'))
sys.path.append(os.path.abspath('../src'))

from data_loader import get_file_path, get_cleaned_data, CSVData

@st.cache_data
def load_data():
    benin = get_cleaned_data("benin_cleaned")
    benin_cleaned = CSVData(benin).load_data()

    # Load sierraleone data
    sierraleone_path = get_cleaned_data("sierraleone_cleaned")
    sierraleone_data = CSVData(sierraleone_path).load_data()

    # Load Benin data
    togo_path = get_cleaned_data("togo_cleaned")
    togo_data = CSVData(togo_path).load_data()

   # Add country column for distinction
    benin_cleaned['Country'] = 'Benin'
    sierraleone_data['Country'] = 'SierraLeone'
    togo_data['Country'] = 'Togo'

    return pd.concat([benin_cleaned, sierraleone_data, togo_data], ignore_index=True)

def plot_ghi_boxplot(df, selected_countries):
    df = df[df['Country'].isin(selected_countries)]
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.boxplot(data=df, x='Country', y='GHI', palette='Set2', hue='Country', legend=False)
    ax.set_title('GHI Distribution by Country')
    return fig

def get_top_regions(df, metric='GHI', top_n=5):
    if 'Region' in df.columns:
        grouped = df.groupby(['Country', 'Region'])[metric].mean().reset_index()
        grouped = grouped.sort_values(by=metric, ascending=False).head(top_n)
    else:
        st.warning("⚠️ 'Region' column not found. Showing top countries by average instead.")
        grouped = df.groupby('Country')[metric].mean().reset_index()
        grouped = grouped.sort_values(by=metric, ascending=False).head(top_n)
    return grouped
