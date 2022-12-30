import streamlit as st
from multiapp import MultiApp
from apps import home,twitter_sentiment

app = MultiApp()

st.markdown(""" #Inteligencia de negocios - Equipo A """)

# Add all your application here

app.add_app("Home", home.app)

app.add_app("Twitter Sentiment Analysis",twitter_sentiment.app)



# The main app
app.run()