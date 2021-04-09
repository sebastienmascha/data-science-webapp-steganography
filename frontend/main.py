import streamlit as st
from multiapp import MultiApp
from apps import home, how_it_works, analysis # import your app modules here

# CONFIGURATIONS
# Hide default menu
# hide_streamlit_style = """
# <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# </style>
# """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
# Full Screen mode
# enable_fullscreen_content()


# MULTI-APPLICATION
# st.set_page_config(layout="wide")
app = MultiApp()
# Add all your application here
app.add_app("Home", home.app)
app.add_app("Research & Analysis", analysis.app)
app.add_app("How it works?", how_it_works.app)


# Sidebar Menu
st.sidebar.title('Navigation')
# The main app
app.run()
# Sidebar Menu
st.sidebar.title("Contribute")

st.sidebar.subheader("Backend")
st.sidebar.markdown("FastAPI is a modern, fast (high-performance), web framework for building APIs.")
st.sidebar.markdown("[API & Swagger docs](https://hr-api.smascha.ai/docs)")
st.sidebar.markdown("[GitHub: sources & docs](https://github.com/sebastienmascha/data-science-viz-streamlit-hr-analytics)")

st.sidebar.subheader("Frontend")
st.sidebar.markdown("Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.")
st.sidebar.markdown("[GitHub: sources & docs](https://github.com/sebastienmascha/data-science-viz-streamlit-hr-analytics)")

st.sidebar.subheader("Jupyter Notebook")
st.sidebar.markdown("Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text.")
st.sidebar.markdown("[Sources and analysis](https://nbviewer.jupyter.org/github/sebastienmascha/data-science-viz-streamlit-hr-analytics/blob/main/Python3_6_Notebook.ipynb)")
