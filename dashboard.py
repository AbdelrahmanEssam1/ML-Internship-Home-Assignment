import streamlit as st

from dashboard_comp.eda import EDAComponent
from dashboard_comp.train import TrainComponent
from dashboard_comp.infer import InferComponent

st.title("Resume Classification Dashboard")
st.sidebar.title("Dashboard Modes")

sidebar_options = st.sidebar.selectbox("Options", ("EDA", "Training", "Inference"))

if sidebar_options == "EDA":
    EDAComponent().render()

elif sidebar_options == "Training":
    TrainComponent().render()

else:
    InferComponent().render()