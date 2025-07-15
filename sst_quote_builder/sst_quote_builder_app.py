
import streamlit as st

# --------------------------------------------
# SST Plastic Surgery Quote Builder
# --------------------------------------------

# Surgeon Fee Schedule (editable for your needs)
surgeon_fees = {
    "Breast Augmentation": 4000,
    "Mastopexy (Breast Lift)": 6000,
    "Augmentation + Lift": 6500,
    "Capsulectomy (Unilateral)": 4500,
    "Capsulectomy (Bilateral)": 6500,
    "Implant Exchange + Capsulectomy": 7500,
    "Tummy Tuck (Full)": 6000,
    "Mini Tummy Tuck": 5500,
    "Tummy Tuck + Lipo": 6500,
    "Neck Liposuction": 2500,
    "Face + Neck Lift": 7500,
    "Upper + Lower Eyelid": 5500,
    "Brow Lift": 4000,
    "Combo Facelift + Brow + Eyelid": 11500
}

# Anesthesia Fee Schedule (from USAP chart)
anesthesia_rates = {
    0.5: 750 * 0.5, 1: 750, 1.5: 960, 2: 1165, 2.5: 1365, 3: 1570,
    3.5: 1775, 4: 1980, 4.5: 2185, 5: 2390, 5.5: 2600, 6: 2800,
    6.5: 3005, 7: 3210, 7.5: 3415, 8: 3620, 8.5: 3825, 9: 4030,
    9.5: 4235, 10: 4440
}

# Facility fee: Park Cities Surgical Center rate
facility_rate_per_hour = 806

# --------------------------------------------
# UI Begins
# --------------------------------------------
st.set_page_config(page_title="SST Quote Builder", layout="centered")
st.title("💼 SST Plastic Surgery Quote Builder")

# Select procedure
procedure = st.selectbox("Select Procedure", list(surgeon_fees.keys()))

# Select estimated operating room time
base_time = st.selectbox("Select Estimated OR Time (Hours)", sorted(anesthesia_rates.keys()))

# Optional Add-ons
st.subheader("Optional Add-ons")
implants = st.checkbox("Silicone Implants (+$1300)")
overnight = st.checkbox("Overnight Stay (+$850)")
garments = st.checkbox("Compression Garments (+$150)")

# --------------------------------------------
# Cost Calculation
# --------------------------------------------
surgeon_fee = surgeon_fees[procedure]
anesthesia_fee = anesthesia_rates[base_time]
facility_fee = base_time * facility_rate_per_hour

supplies_fee = 0
if implants: supplies_fee += 1300
if overnight: supplies_fee += 850
if garments: supplies_fee += 150

total_quote = surgeon_fee + anesthesia_fee + facility_fee + supplies_fee

# --------------------------------------------
# Display Breakdown
# --------------------------------------------
st.markdown("### Quote Summary")
st.write(f"**Surgeon Fee:** ${surgeon_fee:,.2f}")
st.write(f"**Anesthesia Fee:** ${anesthesia_fee:,.2f}")
st.write(f"**Facility Fee:** ${facility_fee:,.2f}")
st.write(f"**Supplies/Add-ons:** ${supplies_fee:,.2f}")
st.markdown("---")
st.write(f"## **Total Estimate: ${total_quote:,.2f}**")

# Optional PDF or email feature to be added later
