import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

def load_data():
    conn = sqlite3.connect('finops_datalake.db')
    df = pd.read_sql('SELECT * FROM expenditures', conn)
    conn.close()
    return df

st.set_page_config(layout="wide", page_title="FinOps Dashboard")
st.title("📊 FinOps Real-Time Visibility")

try:
    df = load_data()
    
    # Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Spend", f"${df['amount'].sum():,.2f}")
    c2.metric("Flagged Items", len(df[df['status'] == 'Flagged']))
    c3.metric("Top Dept", df.groupby('department')['amount'].sum().idxmax())

    # Charts
    fig = px.bar(df, x='department', y='amount', color='status', title="Spend Accountability")
    st.plotly_chart(fig, use_container_width=True)

    # Raw Data / Audit Trail
    st.subheader("Immutable Audit Trail")
    st.dataframe(df, use_container_width=True)

except:
    st.error("Data Lake is empty. Run 'python data_simulator.py' first!")