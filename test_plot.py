import streamlit as st
import pandas as pd

annual_income = st.sidebar.number_input('Annual Retirement income', value=55000)
payout_duration = st.sidebar.number_input("Payout duration (yrs)", value=40)
policy_value = st.sidebar.number_input("Policy value", value=800000)
ror = st.sidebar.number_input("Rate of return", value=5)
cpi = st.sidebar.slider("Consumer Price Index growth", min_value=0.0, max_value=10.0, step=0.1, value=1.5)
inflation = st.sidebar.slider("Annual inflation rate", min_value=0.0, max_value=10.0, step=0.1, value=2.1)

balance = policy_value
balance_list = [balance]
sbp_payment = annual_income * 0.55
sbp_list = [sbp_payment]

for _ in range(payout_duration + 9):
    sbp_payment = sbp_payment * (1 + cpi / 100)
    sbp_list.append(sbp_payment)
    balance = (balance - sbp_payment) * (1 + (ror / 100))
    balance_list.append(balance)


df = pd.DataFrame(
    {'Calendar year': [str(x + 2021) for x in range(payout_duration + 10)],
     'Balance': balance_list,
     'SBP Payment': sbp_list}

)

sw_df = df.set_index('Calendar year')

st.line_chart(sw_df)
st.table(sw_df)
