import streamlit as st
import pandas as pd

# Streamlit app title
st.title("NBA MVP Top 5 Predictions (1982-2024) Using Ridge Regression")

# Explanation of Ridge Regression
st.markdown("""
### About This Model 🏀📊  
This model predicts the top 5 MVP candidates for each season from **1982 to 2024** using **Ridge Regression**.  
Ridge Regression is a machine learning technique that improves predictions by **penalizing large coefficients**, making the model more stable and reducing overfitting.

The model's performance is measured using **Mean Average Precision (MAP)**, which is **0.7599**.  
- **Mean Average Precision (MAP)**: Measures how well the model ranks the correct players at the top.  
  - A score of **1.0** means perfect ranking.  
  - Our score of **0.7599** indicates strong but not perfect predictions.

### 📂 Where to Find the Code  
The full **data scraping, data cleaning, and model training** process can be found in this GitHub repository:  
👉 [NBA-MVP-2025 GitHub Repo](https://github.com/SalyanKarki/NBA-MVP-2025)  

### 📊 Data Source  
The data used for training the model was taken from **[Basketball Reference](https://www.basketball-reference.com/)**,  
which provides historical MVP voting data and player statistics.
""")

# Load data (handle missing file with file uploader)
uploaded_file = st.file_uploader("Upload the MVP data CSV", type=["csv"])
if uploaded_file is not None:
    top_5_per_year = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")
else:
    try:
        top_5_per_year = pd.read_csv("top5.csv")  
    except FileNotFoundError:
        st.error("No data available. Please upload 'top5.csv' to continue.")
        st.stop()  # Stop execution if no file is available

# Dropdown to select year
selected_year = st.selectbox("Select a Year", sorted(top_5_per_year["Year"].unique(), reverse=True))

# Filter data for the selected year
filtered_df = top_5_per_year[top_5_per_year["Year"] == selected_year].copy()

# Adjust ranking to be 1-based instead of 0-based
filtered_df["Rk"] += 1
filtered_df["Predicted_Rk"] += 1

# Display the table
st.write(f"### Top 5 MVP Candidates for {selected_year}:")
st.dataframe(filtered_df[["Player", "Share", "Rk", "Predicted_Rk", "Diff"]].reset_index(drop=True))

# Column explanations
st.markdown("""
### Column Definitions 📊  
- **Player**: The name of the MVP candidate.  
- **Share**: The percentage of MVP votes received (1.0 = 100% of votes).  
- **Rk (Rank)**: The actual ranking based on votes.  
- **Predicted_Rk**: The rank predicted by the Ridge Regression model.  
- **Diff**: Difference between the predicted and actual ranking (**negative = underestimated**, **positive = overestimated**).  
""")
