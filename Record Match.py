import streamlit as st
import pandas as pd

writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
players = pd.read_excel("PingPongData.xlsx", sheet_name = "Data")
matches = pd.read_excel("PingPongData.xlsx",sheet_name = "Matches")
st.title("Record a Match")
teams = st.container(border=True)
teams.subheader("Team Selection")
type = teams.radio("Match Type",["Singles","Doubles"])
s3 = 0
s4 = 0
s5 = 0
s6 = 0
with teams:
    team1, team2 = st.columns(2, border = True)
    player1 = team1.selectbox("Choose Player", players["Nickname"],placeholder="competitor")
    player2 = team1.selectbox("Choose Player ", players["Nickname"],disabled = (type != "Doubles"),placeholder="competitor")
    player3 = team2.selectbox("Choose Player  ", players["Nickname"],placeholder="competitor")
    player4 = team2.selectbox("Choose PLayer   ", players["Nickname"],disabled = (type != "Doubles"),placeholder="competitor")
round1 = st.container(border=True)
round1.subheader("Round 1")
score1,score2 = round1.columns(2,border=True)
s1 = score1.number_input("Team 1 Score",min_value=0)
s2 = score2.number_input("Team 2 Score",min_value=0)
round2button = round1.checkbox("Played more than 1?")
rounds = 1
if round2button:
    round2 = st.container(border=True)
    round2.subheader("Round 2")
    score3,score4 = round2.columns(2,border=True)
    s3 = score3.number_input("Team 1 Score ",min_value=0)
    s4 = score4.number_input("Team 2 Score ",min_value=0)
    round3button = round2.checkbox("Made it to overtime?")
    rounds = 2
    if round3button:
        round3 = st.container(border=True)
        round3.subheader("Round 3")
        score5,score6 = round3.columns(2,border=True)
        s5 = score5.number_input("Team 1 Score  ",min_value=0)
        s6 = score6.number_input("Team 2 Score  ",min_value=0)
        rounds = 3
if type == "Doubles":
    GameType = "D"
else:
    GameType = "S"
    player2 = ""
    player4 = ""
newmatch = pd.DataFrame({
    "GameID":[matches["GameID"].max() + 1],
    "GameType":[GameType],
    "Player1":[player1],
    "Player2":[player2],
    "Player3":[player3],
    "Player4":[player4],
    "T1Score":[s1+s3+s5],
    "T2Score":[s2+s4+s6],
    "Rounds":[rounds]
})
def updatePlayerInfo(name,win,single,selfpoint, otherpoint,rounds):
    players.loc[players["Nickname"]==name,"TotalR"] += rounds
    players.loc[players["Nickname"]==name,"TotalP"] += selfpoint
    players.loc[players["Nickname"] == name,"TotalP"]+=otherpoint
    if single:
        if win:
            players.loc[players["Nickname"]==name,"TotalW"]+=1
            players.loc[players["Nickname"]==name,"sWins"]+=1
        players.loc[players["Nickname"]==name,"sPoints"]+=selfpoint
        players.loc[players["Nickname"]==name,"sDiff"]+=selfpoint
        players.loc[players["Nickname"] == name,"sDiff"]-=otherpoint
        players.loc[players["Nickname"]==name,"sRounds"]+=rounds
    else:
        if win:
            players.loc[players["Nickname"]==name,"TotalW"]+=1
            players.loc[players["Nickname"]==name,"dWins"]+=1
        players.loc[players["Nickname"]==name,"dPoints"]+=selfpoint
        players.loc[players["Nickname"]==name,"dDiff"]+=selfpoint
        players.loc[players["Nickname"]==name,"dDiff"]-=otherpoint
        players.loc[players["Nickname"] == name,"dRounds"] += rounds
updatePlayerInfo(player1,[s1+s3+s5]>[s2+s4+s6],GameType=="S",[s1+s3+s5],[s2+s4+s6],rounds)
updatePlayerInfo(player3,[s1+s3+s5]>[s2+s4+s6],GameType=="S",[s1+s3+s5],[s2+s4+s6],rounds)
if GameType == "D":
    updatePlayerInfo(player2, [s1 + s3 + s5] > [s2 + s4 + s6], GameType == "S", [s1 + s3 + s5], [s2 + s4 + s6], rounds)
    updatePlayerInfo(player4, [s1 + s3 + s5] > [s2 + s4 + s6], GameType == "S", [s1 + s3 + s5], [s2 + s4 + s6], rounds)
if st.button("Add Match"):
    matches = pd.concat([matches,newmatch],ignore_index=True)
    with pd.ExcelWriter("PingPongData.xlsx", engine='xlsxwriter') as writer:
        players.to_excel(writer, sheet_name="Data", index=False)
        matches.to_excel(writer, sheet_name="Matches", index=False)

st.write(matches)