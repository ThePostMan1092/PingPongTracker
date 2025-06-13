import streamlit as st
import pandas as pd

st.title("The Laz Summer Ping Pong Challenge Cup")
st.text("Welcome to the official home of The Laz Summer Ping Pong Challenge Cup — your one-stop scoreboard, stats tracker, and bragging rights central for the summer showdown of the century. Whether you’re a casual paddle-slinger or a spin-shot savant, this app is here to settle the debate once and for all: Who’s the best ping pong player at Laz? ")
st.text("Track match results, view player rankings, analyze game history, and follow the rise (or fall) of your office rivals in real time. Every point counts. Every match matters. Let the games begin.")
one, two, three = st.columns(3,border = False)
one.subheader("Play hard.")
two.subheader("Talk smack.")
three.subheader("Win Glory.")


players = pd.read_excel("PingPongData.xlsx")
matches = pd.read_excel("PingPongData.xlsx", sheet_name="Matches")
st.write(players)
st.write(matches)
