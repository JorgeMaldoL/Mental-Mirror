import streamlit as st

st.title("📝 Your Journal")
st.markdown("This is simply your daily journal. Talk about your day and explain ideas that you have. You can also press the 'Explain to AI' Button and this will trigger the AI to respond to your text with clarifying questions and advice.")

st.markdown("**:green[What was your day like?] " + "&nbsp;" + ":green[What's on your mind?] " + "&nbsp;" + ":green[Do you have an idea that you'd like to write out?]**")
# Text area for journal entry
journal_text = st.text_area("", height=300, placeholder="Start writing about your day, thoughts, or ideas...")

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Save Entry", type="primary"):
        if journal_text:
            st.success("Entry saved!")
        else:
            st.warning("Please write something before saving.")

with col2:
    if st.button("Explain to AI"):
        if journal_text:
            st.info("🤖 AI Analysis coming soon! This will provide clarifying questions and advice based on your entry.")
        else:
            st.warning("Please write something for the AI to analyze.")

# Display saved entries section
st.markdown("---")
st.subheader("Previous Entries")
st.info("The journal entries will be displayed here")
