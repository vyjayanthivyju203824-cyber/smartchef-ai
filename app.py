import streamlit as st

recipes = {
    "🍗 Butter Chicken": ["chicken", "butter", "cream", "tomato"],
    "🍚 Fried Rice": ["rice", "egg", "veggie"],
    "🍝 Pasta": ["pasta", "cheese"]
}

st.title("🤖 SmartChef AI")
st.markdown("*Final Year AI Project*")

ing = st.text_input("Your ingredients?")
if st.button("✨ Generate Recipe"):
    user = [x.strip() for x in ing.lower().split(",")]
    best = max(recipes, key=lambda k: sum(any(u in k for u in user)))
    st.header(f"**{best}**")
    st.success("✅ Perfect match for your ingredients!")
    st.balloons()
