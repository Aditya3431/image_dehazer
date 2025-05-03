from flask import Flask, render_template
import streamlit as st

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


import streamlit as st

st.set_page_config(page_title="Home Page", layout="centered")

st.title("Home Page")
st.write("Welcome to the home page!")

if st.button("About"):
    st.subheader("About")
    st.write("This is the about page.")

if __name__ == "__main__":
    app.run(debug=True)