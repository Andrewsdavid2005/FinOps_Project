import streamlit as st
from core_engine import get_data
import plotly.express as px

st.set_page_config(layout="wide", page_title="FinOps Platform")
st.title("🛡️ FinOps Real-Time Accountability")

if st.button("🔄 Refresh Data Feeds"):
    df = get_data()
    
    # 1. Metrics
    col1, col2 = st.columns(2)
    col1.metric("Total Spend", f"${df['amount'].sum():,.2f}")
    col2.metric("Violations", len(df[df['status'] == "Flagged"]))

    # 2. Charts
    fig = px.bar(df, x="dept", y="amount", color="status", title="Spending by Department")
    st.plotly_chart(fig, use_container_width=True)

    # 3. Audit Table
    st.subheader("Granular Audit Trail")
    st.dataframe(df, use_container_width=True)
else:
    st.info("Click 'Refresh Data Feeds' to begin.")