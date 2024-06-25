import streamlit as st
import pandas as pd
import numpy as np
import snowflake.connector
import streamlit_option_menu
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home","Input Model","Customize your Model","History","About Us"],
    icons = ["house","upload","kanban","book","envelope"],
    menu_icon = "cast",
    default_index = 0,
    #orientation = "horizontal",
)
if selected == "Home":
    st.header('🚀 Welcome to ML Model Registry')

    st.markdown("""
    Harness the power of the Snowflake model registry with our comprehensive MLOps application. 
    Easily manage, deploy, and monitor machine learning models with advanced features designed for scalability and efficiency.
    """)

    st.subheader('Key Features:')

    st.markdown("""
    **Snowflake Model Registry Integration**: Seamlessly integrate with Snowflake's model registry for streamlined model versioning and management.
    
    **Model Effectiveness Measurement**: Evaluate the performance and accuracy of your models over time to ensure they meet business goals.
    
    **Model Drift Monitoring**: Detect changes in model behavior and performance to maintain reliability and effectiveness.
   
    **Data Drift Detection**: Monitor data input variations to proactively address changes in data distribution that affect model performance.
                
    **Customization Features**: Tailor the application to your specific needs with customizable dashboards, alerts, and reporting capabilities.
    """)
    st.subheader('Why Choose MLOps App')

    st.markdown("""Our application empowers data scientists and machine learning engineers to deploy models confidently, monitor their performance effectively, and adapt to changing data landscapes with ease. Whether you''re managing a single model or a complex deployment pipeline, MLOps App ensures your models deliver optimal results consistently.""")
    st.subheader('Get Started Today')
    st.markdown("""Transform your machine learning operations with MLOps App and Snowflake integration. Start optimizing your models and minimizing risks associated with drifts and inefficiencies. Contact us to schedule a demo or explore our trial version to experience the power of MLOps App firsthand.""")
        
    
if selected == "Warehouse":
    st.subheader(f"**You Have selected {selected}**")
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    # run a snowflake query and put it all in a var called my_catalog
    my_cur.execute("select * from SWEATSUITS")
    my_catalog = my_cur.fetchall()
    st.dataframe(my_catalog)
    q1 = st.text_input('Write your query','')
    st.button('Run Query')
    if not q1:
      st.error('Please write a query')
    else:
      my_cur.execute(q1)
      my_catalog = my_cur.fetchall()
      st.dataframe(my_catalog)

    
if selected == "Contact":
    st.subheader(f"**You Have selected {selected}**")

