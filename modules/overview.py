import streamlit as st
import plotly.express as px
import pandas as pd

def show():
    st.title("Global Overview of Undernutrition and Micronutrient Deficiencies")
    # Disclaimer about the app's limitations and demonstration purpose
    st.markdown("""
    **Disclaimer:**
    This application provides a visual representation of undernutrition statistics globally. 
    Please note that the data used in this app is for **demonstration purposes only** and may not represent real-time or fully accurate data. 
    The app is designed for educational and illustrative purposes and may have limitations due to data availability or the nature of the data source.
    Always refer to official organizations like the World Health Organization (WHO) or the World Bank for authoritative and up-to-date information.
    """)
    st.write("""
        This map visualizes the global distribution of undernutrition and micronutrient deficiencies.
    """)

    # Load a list of all countries (Plotly includes country names for choropleth maps)
    country_data = {
        'Country': ['India', 'China', 'USA', 'Brazil', 'Nigeria', 'Indonesia', 'Russia', 'Mexico', 'Japan', 'Germany', 'France', 'UK', 'Italy', 'Canada', 'South Africa'],
        'Undernutrition Percentage': [15.0, 5.0, 2.0, 7.5, 24.0, 11.0, 6.0, 8.0, 4.0, 1.5, 1.0, 2.5, 4.0, 1.0, 13.0],
        'Micronutrient Deficiency Percentage': [30.0, 20.0, 10.0, 22.0, 40.0, 35.0, 25.0, 20.0, 15.0, 5.0, 5.0, 10.0, 12.0, 6.0, 40.0]
    }

    # Convert to DataFrame
    df = pd.DataFrame(country_data)

    # Plot the world map for undernutrition data
    fig = px.choropleth(df,
                        locations="Country",
                        locationmode="country names",
                        color="Undernutrition Percentage",
                        hover_name="Country",
                        color_continuous_scale=px.colors.sequential.Plasma,
                        title="Undernutrition by Country",
                        labels={'Undernutrition Percentage': '% Undernutrition'})

    st.plotly_chart(fig, use_container_width=True)

    # Plot the world map for micronutrient deficiency data
    fig2 = px.choropleth(df,
                         locations="Country",
                         locationmode="country names",
                         color="Micronutrient Deficiency Percentage",
                         hover_name="Country",
                         color_continuous_scale=px.colors.sequential.YlOrRd,
                         title="Micronutrient Deficiency by Country",
                         labels={'Micronutrient Deficiency Percentage': '% Deficiency'})

    st.plotly_chart(fig2, use_container_width=True)
