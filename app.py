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

slt.header('petal length (cm)')

c = slt.text_input("Enter number")

slt.header('petal width (cm)')

d = slt.text_input("Enter Num")


if slt.button("predict"):
    result =model.predict([[a,b,c,d]])

    if result == [0]:
        slt.header('setosa')
    elif result == [1]:
        slt.header('versicolor')
    else:
        slt.header('virginica')
