import streamlit as st

st.set_page_config(page_title="NeuroScreen AI", layout="centered")

st.title("🧠 NeuroScreen AI – Depression & Cognitive Decline Screener")

st.markdown("""
Welcome to NeuroScreen AI – a tool designed to help screen for signs of **depression** and **early cognitive decline** using simple assessments and user inputs.
""")

name = st.text_input("Full Name")
age = st.number_input("Age", min_value=10, max_value=120, step=1)

st.subheader("📝 Depression Screener (PHQ-9)")
q1 = st.slider("1. Little interest or pleasure in doing things", 0, 3)
q2 = st.slider("2. Feeling down, depressed, or hopeless", 0, 3)
q3 = st.slider("3. Trouble falling/staying asleep, or sleeping too much", 0, 3)
q4 = st.slider("4. Feeling tired or having little energy", 0, 3)
q5 = st.slider("5. Poor appetite or overeating", 0, 3)

depression_score = q1 + q2 + q3 + q4 + q5

st.subheader("🧠 Cognitive Screening")
cog_q1 = st.selectbox("How often do you forget recent conversations?", ["Never", "Sometimes", "Often", "Always"])
cog_q2 = st.selectbox("Do you find it hard to concentrate on tasks?", ["No", "Occasionally", "Frequently", "Almost always"])

if st.button("🔍 Analyze"):
    st.markdown("### 🧪 Results")
    st.write(f"Total Depression Score (PHQ-9 subset): **{depression_score}/15**")

    if depression_score >= 10:
        st.error("High likelihood of depression. Consider professional evaluation.")
    elif depression_score >= 5:
        st.warning("Mild to moderate symptoms. Keep monitoring.")
    else:
        st.success("Minimal depressive symptoms.")
