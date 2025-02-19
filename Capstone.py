import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd

data=pd.read_csv("CAPSTONEDATA.csv")

st.write("Sales Daily Chart")
st.line_chart(data,x="billdate", y = "total_bill")

st.divider()

st.write("Tip Chart")