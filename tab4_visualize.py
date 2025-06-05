import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def tab4_visualize_data():
    st.header("📊 Visualize Your Bank Transactions")
    vis_file = st.file_uploader("Upload Excel file for visualization", type=["xlsx", "xls"], key="vis_file")

    if vis_file:
        try:
            vis_df = pd.read_excel(vis_file)
            st.subheader("Preview of Uploaded Data")
            st.dataframe(vis_df.head())

            required_columns = {'Date', 'Amount', 'Type'}
            if required_columns.issubset(vis_df.columns):
                vis_df['Date'] = pd.to_datetime(vis_df['Date'])
                
                st.subheader("Choose Visualization Type")
                chart_type = st.selectbox("Select chart type", ["Line Chart", "Bar Chart", "Heatmap", "Scatter Plot"])

                if chart_type == "Line Chart":
                    st.line_chart(data=vis_df, x='Date', y='Amount')

                elif chart_type == "Bar Chart":
                    df_grouped = vis_df.groupby(['Date', 'Type'])['Amount'].sum().unstack().fillna(0)
                    st.bar_chart(df_grouped)

                elif chart_type == "Heatmap":
                    vis_df['Hour'] = vis_df['Date'].dt.hour
                    vis_df['Day'] = vis_df['Date'].dt.day_name()
                    heatmap_data = vis_df.groupby(['Day', 'Hour']).size().unstack().fillna(0)

                    fig, ax = plt.subplots(figsize=(10, 6))
                    sns.heatmap(heatmap_data, cmap="YlGnBu", ax=ax)
                    st.pyplot(fig)

                elif chart_type == "Scatter Plot":
                    fig = px.scatter(vis_df, x="Date", y="Amount", color="Type", size="Amount", title="Transaction Amounts Over Time")
                    st.plotly_chart(fig)
            else:
                st.warning("Your file must contain 'Date', 'Amount', and 'Type' columns.")
        except Exception as e:
            st.error(f"Error processing uploaded file: {e}")
    else:
        st.info("Please upload a file to visualize transactions.")
