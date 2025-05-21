##  Interactive Dashboard

import streamlit as st
from utils import load_data, plot_ghi_boxplot, get_top_regions

st.set_page_config(page_title='Interactive Dashboard', layout='wide')

st.title("Solar Comparison Dashboard")

df = load_data()

# Sidebar - Country Selector
st.sidebar.header("Filter Options")
countries = df['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect("Select countries:", countries, default=countries)

# Metric Selector (future extension)
selected_metric = st.sidebar.selectbox("Select Solar Metric", ['GHI', 'DNI', 'DHI'])

# Boxplot Display
st.subheader("📊 GHI Distribution")
fig = plot_ghi_boxplot(df, selected_countries)
st.pyplot(fig)

# Top Regions Table
st.subheader("🏆 Top Solar Regions")
top_n = st.slider("Select number of top regions:", min_value=3, max_value=10, value=5)
top_regions = get_top_regions(df[df['Country'].isin(selected_countries)], top_n=top_n)
st.dataframe(top_regions)
