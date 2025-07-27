import streamlit as st

st.title("🏫 Feynman Mode")
st.markdown("**The Feynman Technique**: Explain complex concepts in simple terms as if teaching someone else.")
st.markdown("Choose a topic you want to understand better and explain it in your own words. The AI will help identify gaps in your understanding.")

# Select the topic
topic = st.text_input("What topic would you like to explain?", placeholder="e.g., Quantum Physics, Machine Learning, Economics...")

if topic:
    st.markdown(f"**Explain '{topic}' as if teaching it to someone who knows nothing about it:**")
    
    explanation = st.text_area(
        "Your explanation:", 
        height=300, 
        placeholder="Start with the basics and build up your explanation. Use simple language and analogies..."
    )
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("Get AI Feedback", type="primary"):
            if explanation:
                st.success("🤖 AI feedback coming soon! The AI will help identify knowledge gaps and suggest improvements.")
            else:
                st.warning("Please write your explanation first.")
    
    with col2:
        if st.button("Save Explanation"):
            if explanation:
                st.success("Explanation saved!")
            else:
                st.warning("Please write something before saving.")

st.markdown("---")
st.subheader("How the Feynman Technique Works:")
st.markdown("""
1. **Choose a concept** you want to understand
2. **Explain it simply** as if teaching a child
3. **Identify gaps** where your explanation breaks down
4. **Go back and study** those specific areas
5. **Repeat** until you can explain it clearly
""")

st.info("💡 **Tip**: If you can't explain it simply, you don't understand it well enough!")
