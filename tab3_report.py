import streamlit as st

def tab3_report_fraud():
    st.header("Report a fraud to our Company")
    st.text("Also provide the attachment while drafting the mail")
    issue_description = st.text_area("Enter the issue you want to report:", key="problem_of_user")

    if issue_description:
        subject = "Fraud Report Submission"
        body = issue_description.replace("\n", "%0A")
        recipient = "Adarsh@iacuity.com"

        mailto_link = f"mailto:{recipient}?subject={subject}&body={body}"

        st.markdown(f"""
        <a href="{mailto_link}" target="_blank">
            <button style='background-color:green; color:white; padding:10px 20px; border:none; border-radius:5px; cursor:pointer;'>
                Submit via Gmail
            </button>
        </a>
        """, unsafe_allow_html=True)
    else:
        st.info("Please describe the issue to enable Gmail submission.")
