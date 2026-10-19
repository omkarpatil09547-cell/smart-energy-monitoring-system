
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Smart Energy Monitor",
    page_icon="⚡",
    layout="wide"
)

st.title("Smart Energy Monitoring System ⚡")
st.write("Monitor electricity consumption and estimated costs.")
st.info("Demo mode: readings use sample data.")

voltage = 230
current = 2.5
power = voltage * current
energy = 12.5
rate = 8.0

c1, c2, c3 = st.columns(3)
c1.metric("Voltage", f"{voltage} V")
c2.metric("Current", f"{current} A")
c3.metric("Power", f"{power:.0f} W")

c4, c5 = st.columns(2)
c4.metric("Energy Used", f"{energy} kWh")
c5.metric("Estimated Cost", f"₹{energy * rate:.2f}")

data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Energy (kWh)": [8.2, 9.5, 7.8, 10.1, 12.5, 11.0, 9.2]
})

st.subheader("Weekly Electricity Consumption")
fig = px.bar(data, x="Day", y="Energy (kWh)")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Electricity Bill Calculator")

units = st.number_input(
    "Energy consumed (kWh)",
    min_value=0.0,
    value=12.5
)

tariff = st.number_input(
    "Rate per unit (₹)",
    min_value=0.0,
    value=8.0
)

st.metric("Estimated Bill", f"₹{units * tariff:.2f}")

if units > 10:
    st.warning("High consumption alert. Review your usage.")
else:
    st.success("Consumption is within the demo threshold.")
  
