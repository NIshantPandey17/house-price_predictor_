import pickle
import streamlit as st

model1=pickle.load(open("area.price.pkl","rb"))

def mydeploy():
    st.title("Area Price Prediction")
    area= st.number_input("Enter your area :")
    pred=st.button("Predict")

    if pred:
        x=model1.predict([[area]])
        st.write( "Price of area is :",x[0])


 
mydeploy()    