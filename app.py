import streamlit as slt
import pickle


model = pickle.load(open("model.pkl","rb"))



# model.fit(X_train, y_train)



slt.title("IRRIS CALSSIFY")
# slt.header(model.score(X_test, y_test))
slt.header('sepal length (cm)')

a = slt.text_input("Enter number ")

slt.header('sepal width (cm)')

b = slt.text_input("Enter num")