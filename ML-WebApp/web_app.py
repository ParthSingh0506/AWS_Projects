import joblib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from numpy import outer

model = joblib.load('cancer.pkl')


def web_app():

    st.write("""
    # Breast Cancer Predictor Web App
    ## This app predicts whether cancer is Benign or Malignant.
   """)

    st.header("User Details")
    st.subheader("Kindely Enter The following Details in order to make a prediction")

    cell_shape = st.number_input("Uniformity of Cell Shape",0,10)
    clump_thickness = st.number_input("Clump Thickness",0,10)
    cell_size = st.number_input("Uniformity of Cell Size",0,10)
    marginal_adheasian = st.number_input("Marginal Adeasion",0,10)
    single_epithelial_cell_size = st.number_input("Single Epithelial Cell Size",0,10)
    bare_nuclei = st.number_input("Bare Nuclei",0,10)
    bland_chromatin = st.number_input("Bland Chromatin",0,10)
    normal_nucleoli = st.number_input("Normal Nuceloi",0,10)
    mitosis = st.number_input("Mitosis",0,10)
    
    if st.button("Press here to make Prediction"):
        
        result = model.predict([[cell_shape,clump_thickness,cell_size,marginal_adheasian,
                                single_epithelial_cell_size,bare_nuclei,bland_chromatin,
                                normal_nucleoli,mitosis]])
        if result == 2:
            result = "Benign"
        else: 
            result = "Malignant"
        
        st.text_area(label='Cancer is:- ',value=result , height= 100)
         
    
    
run = web_app()