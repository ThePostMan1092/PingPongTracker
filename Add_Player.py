import streamlit as st
import pandas as pd

players = pd.read_excel("PingPongData.xlsx", sheet_name="Data")
matches = pd.read_excel("PingPongData.xlsx", sheet_name="Matches")
st.title("Welcome to the Challenge!")
info = st.container(border=True)
name = info.text_input("Enter your name:")
nickname = info.text_input("Enter a nickname (optional):")
if info.button("Enter", type="primary"):
    if not players["Name"].str.contains(name).any() and name!="":
        if nickname == "":
            info.write("See you at the Table!")
            newRow = pd.DataFrame({
                "PlayerID": [players["PlayerID"].max() + 1],
                "Rank": [players["Rank"].max() + 1],
                "Name": [name],
                "Nickname": [nickname],
                "TotalR": [0],
                "TotalW": [0],
                "TotalP": [0],
                "sRounds": [0],
                "sWins": [0],
                "sPoints": [0],
                "sDiff": [0],
                "dRounds": [0],
                "dWins": [0],
                "dPoints": [0],
                "dDiff": [0]
            })
            players = pd.concat([players, newRow], ignore_index=True)
        elif not players["Nickname"].str.contains(nickname).any():
            info.write("See you at the Table!")
            newRow = pd.DataFrame({
                "PlayerID": [players["PlayerID"].max() + 1],
                "Rank": [players["Rank"].max() + 1],
                "Name": [name],
                "Nickname": [nickname],
                "TotalR": [0],
                "TotalW": [0],
                "TotalP": [0],
                "sRounds": [0],
                "sWins": [0],
                "sPoints": [0],
                "sDiff": [0],
                "dRounds": [0],
                "dWins": [0],
                "dPoints": [0],
                "dDiff": [0]
            })
            players = pd.concat([players, newRow], ignore_index=True)
            with pd.ExcelWriter("PingPongData.xlsx",engine='xlsxwriter') as writer:
                players.to_excel(writer, sheet_name="Data", index=False)
                matches.to_excel(writer, sheet_name="Matches", index=False)
        else:
            info.write("Nickname already in use")
    else:
        info.write("Name already in use")
st.write(players)
