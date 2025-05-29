import streamlit as st
import pandas as pd
import altair as alt

def show():
    st.title("Nutrition Data Visualization")
    st.write("This section presents visual insights into nutrition data.")

    # Example: sample dataset
    data = pd.DataFrame({
        'Country': ['India', 'Nigeria', 'Bangladesh', 'Ethiopia', 'DR Congo'],
        'Stunting (%)': [30, 32, 28, 36, 42]
    })

    st.write("### Childhood Stunting by Country")
    
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X('Country', sort=None),
        y='Stunting (%)',
        tooltip=['Country', 'Stunting (%)']
    ).properties(height=400)
    
    st.altair_chart(chart, use_container_width=True)
