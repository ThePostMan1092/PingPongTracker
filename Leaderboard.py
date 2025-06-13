import streamlit as st
import pandas as pd

players = pd.read_excel("PingPongData.xlsx", sheet_name="Data")
st.title("Leaderboard")
leaderdf = players.sort_values(by="Rank")
leaderdf.set_index("Rank", inplace = True)
leaderdf.drop(columns=["PlayerID"], axis=1, inplace=True)
st.write(leaderdf)
Name, wins, rounds = st.columns(3,border =True)
if leaderdf.iloc[0]["Nickname"] != "":
    Name.metric("Current Leader",leaderdf.iloc[0]["Nickname"])
else:
    Name.metric("Current Leader", leaderdf.iloc[0]["Name"])
if leaderdf.iloc[0]["sWins"] > leaderdf.iloc[0]["dWins"]:
    wins.metric("Singles Wins",leaderdf.iloc[0]["sWins"])
else:
    wins.metric("Doubles Wins", leaderdf.iloc[0]["dWins"])
rounds.metric("Total Rounds Played",leaderdf.iloc[0]["TotalR"])
