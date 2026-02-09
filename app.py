import streamlit as st
import json
 
# Load JSON data
with open("sap_notes_db.json", "r") as file:
    data = json.load(file)
 
# Page title
st.title("SAP Notes Smart Agent 🤖")
 
st.write("Paste your ST22 dump / error message below:")
 
# Text input box
user_input = st.text_area("Enter Dump Text")
 
# Button
if st.button("Analyze"):
 
    found = False
 
    # Search for matching error
    for item in data:
        if item["error"] in user_input:
 
            st.success("Error Detected!")
 
            st.write("### Error:")
            st.write(item["error"])
 
            st.write("### Possible Cause:")
            st.write(item["cause"])
 
            st.write("### Suggested SAP Note:")
            st.write(item["note"])
 
            st.write("### Fix:")
            st.write(item["fix"])
 
            found = True
            break
 
    if not found:
        st.error("No matching SAP Note found. Try adding this error to JSON database.")