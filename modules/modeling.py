import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

def show():
    st.title("Nutrition Modeling")
    st.write("This section explores predictive modeling for nutrition outcomes.")

    # Example: predictive model dataset (generated as dummy data)
    np.random.seed(42)
    countries = ['India', 'Nigeria', 'Bangladesh', 'Ethiopia', 'DR Congo']
    rates = np.random.uniform(25, 50, size=len(countries))  # Dummy data for undernutrition rates

    data = pd.DataFrame({
        'Country': countries,
        'Undernutrition Rate (%)': rates
    })

    st.write("### Predicted Undernutrition Rates by Country")
    chart = alt.Chart(data).mark_line().encode(
        x='Country',
        y='Undernutrition Rate (%)',
        tooltip=['Country', 'Undernutrition Rate (%)']
    ).properties(height=400)
    
    st.altair_chart(chart, use_container_width=True)

    st.markdown("""
### Nutrition Modeling Methodology

Nutrition modeling uses mathematical techniques to simulate the relationships between diet, health, and external factors to improve public health decisions.

1. **Data Collection**:
   - **Dietary Data**: Food consumption patterns and nutrient intake.
   - **Health Data**: Prevalence of diseases like undernutrition, obesity, and micronutrient deficiencies.
   - **Socioeconomic & Environmental Data**: Factors like food security, climate change, and income levels.

2. **Types of Models**:
   - **Static Models**: Snapshot analysis of current nutrition status.
   - **Dynamic Models**: Simulate changes over time (e.g., the impact of interventions).
   - **Individual-Level Models**: Focus on specific health impacts of individual diets.
   - **Population-Level Models**: Assess broader health outcomes in populations.

3. **Key Approaches**:
   - **Linear Programming (LP)**: Optimizes diets based on cost and nutrition.
   - **Markov Models**: Simulate transitions between health states (e.g., healthy to undernourished).
   - **Agent-Based Modeling (ABM)**: Simulates individual behaviors and interactions.
   - **Microsimulation**: Simulates individual life courses for understanding nutrition impacts on health.

4. **Calibrating and Validating Models**:
   - **Calibration**: Adjust model parameters based on real data.
   - **Validation**: Compare model outputs with observed health data to ensure accuracy.

5. **Interventions**:
   - Models simulate different interventions (e.g., fortification, supplementation) to assess their impact on public health outcomes.

6. **Limitations**:
   - **Data Gaps**: Incomplete or low-quality data can affect model accuracy.
   - **Simplified Assumptions**: Assumptions made in models may not capture all real-world complexities.
   - **Uncertainty**: Small changes in inputs can lead to significant output variations.

This methodology helps guide decisions on nutrition interventions and policies to improve global health, with a focus on undernutrition, food security, and sustainability.
""")