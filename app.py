import streamlit as st
import pandas as pd
st.title("Education Analytics Dashboard")
df = pd.read_csv("EduPro Online Platform.xlsx - Users.csv")
st.write("Total Users:", len(df))
st.dataframe(df.head())
st.subheader("Gender Distribution")
st.bar_chart(df["Gender"].value_counts())
st.subheader("Age Distribution")
st.bar_chart(df["Age"].value_counts().sort_index())
