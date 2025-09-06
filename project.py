import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# App Title
st.title ("💰 Personal Finance Dashboard- Budget and Savings Tracker")

#Sidebar for user input
st.sidebar.header (" Enter Your Monthly Details")

#Income And Expenses
income= st.sidebar.number_input ("Monthly Income (₹)", min_value=0, step=1000)
rent = st.sidebar.number_input ("Rent (₹)", min_value=0, step=500)
food = st.sidebar.number_input ("Food (₹)", min_value=0, step=500)
transport = st.sidebar.number_input ("Transport (₹)", min_value=0, step=500)
entertainment = st.sidebar.number_input ("Entertainment (₹)", min_value=0, step=500)
others = st.sidebar.number_input ("Others (₹)", min_value=0, step=500)

#Calculate Tools
total_expenses = (rent + food + transport + entertainment + others)
savings = income - total_expenses

#Show Results
st.header("📊 Monthly Summary")
st.write(f" Total Income: ₹{income}")
st.write(f" Total Expenses: ₹{total_expenses}")
st.write(f" Savings: ₹{savings}")

#Visualise with a Pie Chart
if income > 0:
    df = pd.DataFrame ({
        'Category': ['Rent', 'Food', 'Transport', 'Entertainment', 'Others', 'Savings'],
        'Amount': [rent, food, transport, entertainment, others, savings]
    })
    st.subheader("💡 Expen                                                       ses & Savings Distribution")
    st.bar_chart(df.set_index('Category'))

    # Message
    if savings > 0:
        st.success("🎉 Great! You are saving money this month.")
    elif savings == 0:
        st.warning("⚠️ You are breaking even. Try to save something.")
    else:
        st.error("❌ Your expenses are more than your income!")
