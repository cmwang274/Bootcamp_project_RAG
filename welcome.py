
import streamlit as st

st.title("About this App")
st.write("This is a streamlit app that demonstrates how to use the OpenAI API to generate text completions.")

with st.expander("How to use this App properly?"):
    st.markdown("""
    - Use the sidebar to navigate between pages.
    - On the **Main Page**, enter your query about courses (e.g., "I want to learn data science").
    - The app will detect relevant course categories and recommend suitable options.
    - You can explore additional pages like `Page 2` for browsing or filtering course catalogs.
    - Data is sourced from curated JSON files and AI-enhanced search.
    """)