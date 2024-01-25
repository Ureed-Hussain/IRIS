import streamlit as slt
import pickle


model = pickle.load(open("model.pkl","rb"))



# model.fit(X_train, y_train)



slt.title("IRRIS CALSSIFY")
# slt.header(model.score(X_test, y_test))
slt.header('sepal length (cm)')

a = slt.text_input("Enter number ")

a = int(a)

slt.header('sepal width (cm)')

b = slt.text_input("Enter num")
b = int(b)
slt.header('petal length (cm)')

c = slt.text_input("Enter number")
c=int(c)

slt.header('petal width (cm)')

d = slt.text_input("Enter Num")
d=int(d)

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
