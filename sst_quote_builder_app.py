
import streamlit as st
import pandas as pd

# Surgeon fee schedule (from PDF)
surgeon_fees = {
    "Breast Augmentation": 4000,
    "Breast Lift": 4500,
    "Tummy Tuck": 6000,
    "Liposuction": 3000,
    "Mommy Makeover": 8500,
    "Breast Revision": 4800,
    "Breast Reduction": 5200
}

# Facility fee logic (1st at 100%, rest at 50%)
facility_fees = {
    "Breast Augmentation": 403,
    "Breast Lift": 525,
    "Tummy Tuck": 670,
    "Liposuction": 345,
    "Mommy Makeover": 780,
    "Breast Revision": 490,
    "Breast Reduction": 510
}

# Anesthesia fee schedule (based on exact time tiers)
anesthesia_schedule = {
    1: 750, 1.5: 960, 2: 1165, 2.5: 1365, 3: 1570, 3.5: 1775,
    4: 1980, 4.5: 2185, 5: 2390, 5.5: 2600, 6: 2800, 6.5: 3005,
    7: 3210, 7.5: 3415, 8: 3620, 8.5: 3825, 9: 4030, 9.5: 4235, 10: 4440
}

# Add-on costs
add_ons = {
    "Silicone Implants": 1300,
    "Overnight Stay": 850,
    "Compression Garments": 150
}

st.title("💼 SST Plastic Surgery Quote Builder")

# Procedure selection
selected_procedures = st.multiselect(
    "Select Procedure(s)", options=list(surgeon_fees.keys()), default=["Breast Augmentation"]
)

# Estimated OR time
or_time = st.selectbox(
    "Select Estimated OR Time (Hours)", options=list(anesthesia_schedule.keys()), index=0
)

# Optional add-ons
st.markdown("### Optional Add-ons")
selected_addons = []
for item in add_ons:
    if st.checkbox(f"{item} (+${add_ons[item]})"):
        selected_addons.append(item)

# Fee calculations
primary_proc = max(selected_procedures, key=lambda x: surgeon_fees[x])
surgeon_fee = surgeon_fees[primary_proc] + sum(surgeon_fees[proc] * 0.5 for proc in selected_procedures if proc != primary_proc)
facility_fee = facility_fees[primary_proc] + sum(facility_fees[proc] * 0.5 for proc in selected_procedures if proc != primary_proc)
anesthesia_fee = anesthesia_schedule[or_time]
supplies_fee = sum(add_ons[item] for item in selected_addons)

# Quote summary
st.markdown("## Quote Summary")
st.write(f"**Surgeon Fee:** ${surgeon_fee:,.2f}")
st.write(f"**Anesthesia Fee:** ${anesthesia_fee:,.2f}")
st.write(f"**Facility Fee:** ${facility_fee:,.2f}")
st.write(f"**Supplies/Add-ons:** ${supplies_fee:,.2f}")

total = surgeon_fee + anesthesia_fee + facility_fee + supplies_fee
st.markdown(f"### **Total Estimate: ${total:,.2f}**")
