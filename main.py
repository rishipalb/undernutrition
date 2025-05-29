import streamlit as st
from modules import overview, data_viz, surveillance, modeling, policy

st.set_page_config(page_title="Nutrition Insights", layout="wide")
st.sidebar.title("📊 App Sections")

section = st.sidebar.radio("Go to:", [
    "Overview",
    "Global Data",
    "Surveillance & Epidemiology",
    "Modeling",
    "Policy & Program Impact"
])

if section == "Overview":
    overview.show()
elif section == "Global Data":
    data_viz.show()
elif section == "Surveillance & Epidemiology":
    surveillance.show()
elif section == "Modeling":
    modeling.show()
elif section == "Policy & Program Impact":
    policy.show()
