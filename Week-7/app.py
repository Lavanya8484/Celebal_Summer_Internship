# app.py

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load model and data
model = joblib.load("iris_model.pkl")
iris = load_iris()

st.title("🌸 Iris Flower Prediction App")
st.write("Provide flower measurements to predict the species.")

# Sidebar - Input features
st.sidebar.header("User Input Features")

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length (cm)', 4.0, 8.0, 5.4)
    sepal_width  = st.sidebar.slider('Sepal width (cm)', 2.0, 4.5, 3.4)
    petal_length = st.sidebar.slider('Petal length (cm)', 1.0, 7.0, 1.3)
    petal_width  = st.sidebar.slider('Petal width (cm)', 0.1, 2.5, 0.2)

    data = {
        'sepal length (cm)': sepal_length,
        'sepal width (cm)': sepal_width,
        'petal length (cm)': petal_length,
        'petal width (cm)': petal_width
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# Display user input
st.subheader("User Input")
st.write(input_df)

# Make prediction
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

st.subheader("Prediction")
st.write(f"Predicted Species: **{iris.target_names[prediction[0]]}**")

st.subheader("Prediction Probabilities")
st.write(pd.DataFrame(prediction_proba, columns=iris.target_names))

# Visualize dataset + input
st.subheader("Iris Dataset Visualization")
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

fig, ax = plt.subplots()
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)',
                hue=iris.target_names[df['target']], data=df, ax=ax)
ax.scatter(input_df['sepal length (cm)'], input_df['sepal width (cm)'],
           color='red', s=100, label='Your Input')
ax.legend()
st.pyplot(fig)
