import streamlit as st
import pandas as pd
import os

# Streamlit app title
st.title("NBA MVP Top 5 Predictions (1982-2024) Using Ridge Regression")

# Print working directory for debugging
cwd = os.getcwd()
st.write(f"Current Working Directory: {cwd}")

# File path for CSV
file_path = os.path.join(cwd, "top_5.csv")

# Check if the CSV file exists
if os.path.exists(file_path):
    top_5_per_year = pd.read_csv(file_path)
    st.success("Loaded 'top_5.csv' from the server!")
else:
    # If file is missing, allow user to upload it
    st.warning("File 'top_5.csv' not found. Please upload it below.")
    uploaded_file = st.file_uploader("Upload the MVP data CSV", type=["csv"])

    if uploaded_file is not None:
        top_5_per_year = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
    else:
        st.error("No data available. Please upload 'top_5.csv' to continue.")
        st.stop()  # Stop execution if no file is available

# Dropdown to select year
selected_year = st.selectbox("Select a Year", sorted(top_5_per_year["Year"].unique(), reverse=True))

# Filter data for the selected year
filtered_df = top_5_per_year[top_5_per_year["Year"] == selected_year]

# Display the table
st.write(f"Top 5 MVP Candidates for {selected_year}:")
st.dataframe(filtered_df[["Player", "Share", "Rk", "Predicted_Rk", "Diff"]].reset_index(drop=True))
