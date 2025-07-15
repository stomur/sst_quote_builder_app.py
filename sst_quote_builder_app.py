
import streamlit as st
import pandas as pd

# Load Tomur Surgeon Fees
surgeon_fee_df = pd.read_excel("Updated  Cosmetic-pricing PCSC 2025.xlsx", sheet_name=None)
surgical_procedures = {}
for sheet, df in surgeon_fee_df.items():
    df = df.dropna(subset=[df.columns[0], df.columns[1]])
    for _, row in df.iterrows():
        name, price = row.iloc[0], row.iloc[1]
        if isinstance(price, (int, float)):
            surgical_procedures[name] = float(price)

# Anesthesia fee schedule (hardcoded from screenshot)
anesthesia_rates = {
    1.0: 750.00, 1.5: 960.00, 2.0: 1165.00, 2.5: 1365.00, 3.0: 1570.00,
    3.5: 1775.00, 4.0: 1980.00, 4.5: 2185.00, 5.0: 2390.00, 5.5: 2600.00,
    6.0: 2800.00, 6.5: 3005.00, 7.0: 3210.00, 7.5: 3415.00, 8.0: 3620.00,
    8.5: 3825.00, 9.0: 4030.00, 9.5: 4235.00, 10.0: 4440.00
}

st.title("Surgical Quote Builder – Dr. Tomur")

# Procedure selection
selected_procedures = st.multiselect("Select Procedures", options=list(surgical_procedures.keys()))

# Time in OR for Anesthesia and Facility Fee
or_time = st.selectbox("Select OR Time (in hours)", options=list(anesthesia_rates.keys()))

# Quote computation
if st.button("Generate Quote") and selected_procedures:
    # Sort by fee descending to get highest fee
    sorted_procs = sorted(selected_procedures, key=lambda x: surgical_procedures[x], reverse=True)
    surgeon_fee_total = 0
    facility_fee_total = 0

    for i, proc in enumerate(sorted_procs):
        base_fee = surgical_procedures[proc]
        if i == 0:
            surgeon_fee_total += base_fee
            facility_fee_total += base_fee  # 100% of highest
        else:
            surgeon_fee_total += 0.5 * base_fee
            facility_fee_total += 0.5 * base_fee  # 50% of additional

    anesthesia_fee = anesthesia_rates[or_time]

    st.subheader("Quote Summary")
    st.markdown(f"**Surgeon Fee:** ${surgeon_fee_total:,.2f}")
    st.markdown(f"**Facility Fee:** ${facility_fee_total:,.2f}")
    st.markdown(f"**Anesthesia Fee (for {or_time} hr):** ${anesthesia_fee:,.2f}")
    st.markdown("---")
    st.markdown(f"**Total Estimate:** ${surgeon_fee_total + facility_fee_total + anesthesia_fee:,.2f}")
else:
    st.info("Select at least one procedure and click 'Generate Quote'")
