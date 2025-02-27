#!/usr/bin/env python
# coding: utf-8

# In[13]:


import streamlit as st
import pandas as pd


# In[16]:


st.title("NBA MVP Top 5 Predictions (1982-2024) Using Ridge Regression")
top_5_per_year = pd.read_csv("top_5_mvp_1982-2024.csv") 
# Dropdown to select year
selected_year = st.selectbox("Select a Year", sorted(df["Year"].unique(), reverse=True))

# Filter data for the selected year
filtered_df = top_5_per_year[top_5_per_year["Year"] == selected_year]

# Display the table
st.write(f"Top 5 MVP Candidates for {selected_year}:")
st.dataframe(filtered_df[["Player", "Share", "Rk", "Predicted_Rk", "Diff"]].reset_index(drop=True))



# In[ ]:




