import streamlit as st
import pandas as pd

def show():
    st.title("Undernutrition Surveillance")
    st.write("This section presents data on global undernutrition surveillance.")

    # Example: sample dataset for surveillance
    data = pd.DataFrame({
        'Country': ['India', 'Nigeria', 'Bangladesh', 'Ethiopia', 'DR Congo'],
        'Undernutrition Rate (%)': [38, 34, 30, 45, 50]
    })

    st.write("### Undernutrition Rate by Country")
    st.bar_chart(data.set_index('Country'))
