import streamlit as slt
import pickle


model = pickle.load(open("model.pkl","rb"))



# model.fit(X_train, y_train)



slt.title("IRRIS CALSSIFY")
# slt.header(model.score(X_test, y_test))
slt.header('sepal length (cm)')

a = slt.number_input("Enter number ")


slt.header('sepal width (cm)')

b = slt.number_input("Enter num")
slt.header('petal length (cm)')

c = slt.number_input("Enter number")


slt.header('petal width (cm)')

d = slt.number_input("Enter Num")


if slt.button("predict"):
    result =model.predict([[a,b,c,d]])

    if result == [0]:
        slt.header('setosa')
        print("setosa")
    elif result == [1]:
        slt.header('versicolor')
        print("versicolor")
    else:
        slt.header('virginica')
        print("virginica")
