import streamlit as st
import json
# import win32com.client as win32

 
 
# ---------- Load JSON ----------
with open("sap_notes_db2.json", "r") as file:
    data = json.load(file)
 
st.title("SAP BASIS Smart Support Agent 🤖")
 
user_input = st.text_input("Enter SAP Error / Dump Name")
 
# ---------- Search Logic ----------
if user_input:
    found = False
 
    for item in data:
        # Match using errorVariants (case insensitive)
        for err in item["errorVariants"]:
            if err.lower() in user_input.lower():
 
                found = True
 
                st.header(f"Error: {item['error']}")
 
                st.subheader("Description")
                st.write(item["description"])
 
                st.subheader("Possible Causes")
                for c in item["possibleCauses"]:
                    st.write("• " + c)
 
                st.subheader("BASIS Recommendation")
                for r in item["basisRecommendation"]:
                    st.write("• " + r)
 
                st.subheader("Transactions to Check")
                for t in item["transactionCodes"]:
                    st.write("• " + t)
 
                st.subheader("Mail Draft")
                st.code(item["mailDraft"])
 
       
                
 
                break
 
    if not found:

        st.error("No matching SAP error found")
