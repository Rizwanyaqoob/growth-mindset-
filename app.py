import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")

st.title("🌱 Growth Mindset Challenge")
st.subheader("Discover the power of believing you can improve!")

st.markdown("""
---

## 📘 What is a Growth Mindset?

A **growth mindset** is the belief that your abilities and intelligence can be developed through hard work, effort, and learning.

---

## 💡 Why Adopt a Growth Mindset?

- ✅ Don’t be afraid of hard tasks — try and learn from them  
- ✅ Mistakes are okay — learn something from each one  
- ✅ Keep going even when things get tough  
- ✅ Appreciate your effort, not just the final result  
- ✅ Always be ready to learn new things

---

## 🚀 Practice a Growth Mindset

1. Set learning goals  
2. Reflect on your progress  
3. Seek feedback  
4. Stay positive and believe in improvement

---

""")

if st.button("🎯 I will adopt a Growth Mindset!"):
    st.success("That's amazing! You've taken the first step toward a growth mindset. Keep going! 💪")

st.info("Built with Streamlit for the Growth Mindset Challenge.")
