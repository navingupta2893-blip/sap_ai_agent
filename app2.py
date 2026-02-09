import streamlit as st
import json
import win32com.client as win32
 
# ---------- Outlook Draft Function ----------
def open_outlook_draft(subject, body, to_email):
    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
 
    mail.To = to_email
    mail.Subject = subject
    mail.Body = body
 
    mail.Display()   # Opens Outlook draft popup (does NOT send)
 
 
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
 
                # ---------- Outlook Button ----------
                if st.button("Open Mail Draft in Outlook"):
                    subject = "SAP Alert: " + item["error"]
                    body = item["mailDraft"]
 
                    # Team routing
                    if item.get("module") == "ABAP":
                        to_email = "abapteam@company.com"
                    elif item.get("module") == "BASIS":
                        to_email = "basisteam@company.com"
                    else:
                        to_email = "support@company.com"
 
                    open_outlook_draft(subject, body, to_email)
 
                break
 
    if not found:
        st.error("No matching SAP error found")