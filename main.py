from riotwatcher import RiotWatcher, ApiError



watcher = RiotWatcher('RGAPI-14f19f3d-34a1-4e08-abdc-4fac0d1efa3a')

my_region = 'euw1'

summonername = "Der KAX 59"

me = watcher.summoner.by_name(my_region , 'Der KAX 59')

#print(me)
#print()
#print(type(me))
accountId = me.get("accountId")
#print()
print(accountId)
print()
id = me.get("id")
print(id)
print()
#print(watcher.league.by_summoner(my_region,id))
leagueinfoall = watcher.league.by_summoner(my_region,id)
leagueinfosoloduo = leagueinfoall[0]
leagueinfoflex = leagueinfoall[1]
leagueinfotft = leagueinfoall[2]
print()
#print(leagueinfosoloduo)
#print(leagueinfoflex)
#print(leagueinfotft)
print()
#print(type(leagueinfosoloduo))
mydivisionsoloduo = leagueinfosoloduo.get("tier")
print(mydivisionsoloduo)
print()
myrank = leagueinfosoloduo.get("rank")
print(myrank)
print()
mylp = leagueinfosoloduo.get("leaguePoints")
print(mylp)
print()
mywinsthisseason = leagueinfosoloduo.get("wins")
print(mywinsthisseason)
print()
mylossesthisseason = leagueinfosoloduo.get("losses")
print(mylossesthisseason)


matchlist = watcher.match.matchlist_by_account(my_region, accountId)
print(matchlist)
#print(type(matchlist))
#print(len(matchlist))
matches = matchlist.get("matches")
#print(matches)
lastgame = matches[0]
#print(lastgame)
gameidlastgame = lastgame.get("gameId")
print(gameidlastgame)
mychamplastgame = lastgame.get("champion")
print(mychamplastgame)

normaldraftmatchlist = watcher.match.matchlist_by_account(my_region, accountId, 400)
print(normaldraftmatchlist)
normalblindmatchlist = watcher.match.matchlist_by_account(my_region, accountId, 430)
print(normalblindmatchlist)
rankedsoloduomatchlist = watcher.match.matchlist_by_account(my_region, accountId, 420)
print(rankedsoloduomatchlist)
rankedflex5vs5matchlist = watcher.match.matchlist_by_account(my_region, accountId, 440)
print(rankedflex5vs5matchlist)





matchinfo = watcher.match.by_id(my_region,gameidlastgame)
#print(matchinfo)
#print(type(matchinfo))

participantIdentities = matchinfo.get("participantIdentities")
#print(participantIdentities)
for i in participantIdentities:
	player = i.get("player")
	if summonername == player.get("summonerName"):
		mypartid = i.get("participantId")
participants = matchinfo.get("participants")
#print(participants)
#print(type(participants))a
myinfo = participants[mypartid-1]
#print(myinfo)
myteamidlastgame = myinfo.get("teamId")
print(myteamidlastgame)

teams = matchinfo.get("teams")
#print(teams)
for j in  teams:
	if myteamidlastgame == j.get("teamId"):
		winorloselastgame =j.get("win")
#print(winorloselastgame)
lastgameVictory = "Victory"
lastgameDefeat = "Defeat"
if winorloselastgame == "Win":
	winlastgame = 1
else:
	winlastgame = 0
if winlastgame == 1:
	print(lastgameVictory)
else:
	print(lastgameDefeat)
#print(type(myinfo))
mystatslastgame = myinfo.get("stats")
#print(mystatslastgame)
#print(type(mystatslastgame))
mykillslastgame = mystatslastgame.get("kills")
print(mykillslastgame)
mydeathslastgame = mystatslastgame.get("deaths")
print(mydeathslastgame)
myassistslastgame = mystatslastgame.get("assists")
print(myassistslastgame)
myvisionscorelastgame = mystatslastgame.get("visionScore")
print(myvisionscorelastgame)
minionskilledlastgame = (mystatslastgame.get("totalMinionsKilled"))+(mystatslastgame.get("neutralMinionsKilled"))
print(minionskilledlastgame)
print(type(lastgame))
mylanelastgame = lastgame.get("lane")
print(mylanelastgame)
print(type(participants))
for k in participants:
	timeline = k.get("timeline")
	if myteamidlastgame != k.get("teamId") and mylanelastgame == timeline.get("lane"):
		mylaneenemy = k.get("participantId")
print(mylaneenemy)

print(participants)

class game():
    def __init__(self,region,summname):
        self.region = region
        self.summname = summname
        self.me = watcher.summoner.by_name(self.region, self.summname)
        self.accountId = me.get("accountId")
        self.id = me.get("id")
    def getdivisionsoloduo(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfosoloduo = leagueinfoall[0]
        mydivisionsoloduo = leagueinfosoloduo.get("tier")
        return mydivisionsoloduo
    def getdivisiontft(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfotft = leagueinfoall[2]
        mydivisiontft = leagueinfotft.get("tier")
        return mydivisiontft
    def getdivisionflex5vs5(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfoflex = leagueinfoall[1]
        mydivisionflex5vs5 = leagueinfoflex.get("tier")
        return mydivisionflex5vs5
    def getranksoloduo(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfosoloduo = leagueinfoall[0]
        myranksoloduo = leagueinfosoloduo.get("rank")
        return myranksoloduo
    def getranktft(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfotft = leagueinfoall[2]
        myranktft = leagueinfotft.get("rank")
        return myranktft
    def getrankflex5vs5(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfoflex5vs5 = leagueinfoall[1]
        myrankflex5vs5 = leagueinfoflex5vs5.get("rank")
        return myrankflex5vs5
    def getlpsoloduo(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfosoloduo = leagueinfoall[0]
        mylpsoloduo = leagueinfosoloduo.get("leaguePoints")
        return mylpsoloduo
    def getlptft(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfotft = leagueinfoall[2]
        mylptft = leagueinfotft.get("leaguePoints")
        return mylptft
    def getlpflex5vs5(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfoflex = leagueinfoall[1]
        mylpflex5vs5 = leagueinfoflex.get("leaguePoints")
        return mylpflex5vs5
    def getwinssoloduo(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfosoloduo = leagueinfoall[0]
        mywinssoloduo = leagueinfosoloduo.get("wins")
        return mywinssoloduo
    def getwinstft(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfotft = leagueinfoall[2]
        mywinstft = leagueinfotft.get("wins")
        return mywinstft
    def getwinsflex5vs5(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfoflex = leagueinfoall[1]
        mywinsflex5vs5 = leagueinfoflex.get("wins")
        return mywinsflex5vs5
    def getlossessoloduo(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfosoloduo = leagueinfoall[0]
        mylossessoloduo = leagueinfosoloduo.get("losses")
        return mylossessoloduo
    def getlossestft(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfotft = leagueinfoall[2]
        mylossestft = leagueinfotft.get("losses")
        return mylossestft
    def getlossesflex5vs5(self):
        leagueinfoall = watcher.league.by_summoner(self.region, self.id)
        leagueinfoflex = leagueinfoall[1]
        mylossesflex5vs5 = leagueinfoflex.get("losses")
        return mylossesflex5vs5



meinletztesgame = game(my_region, summonername)
getdiv = meinletztesgame.getdivisionsoloduo()
getdivtft = meinletztesgame.getdivisiontft()
getdivflex5vs5 = meinletztesgame.getdivisionflex5vs5()
getranksoloduo = meinletztesgame.getranksoloduo()
getranktft = meinletztesgame.getranktft()
getrankflex5vs5 = meinletztesgame.getrankflex5vs5()
getlpsoloduo = meinletztesgame.getlpsoloduo()
getlptft = meinletztesgame.getlptft()
getlpflex5vs5 = meinletztesgame.getlpflex5vs5()
getwinssoloduo = meinletztesgame.getwinssoloduo()
getwinstft = meinletztesgame.getwinstft()
getwinsflex5vs5 = meinletztesgame.getwinsflex5vs5()
getlossessoloduo = meinletztesgame.getlossessoloduo()
getlossestft = meinletztesgame.getlossestft()
getlossesflex5vs5 = meinletztesgame.getlossesflex5vs5()





print(getdiv)
print(getdivtft)
print(getdivflex5vs5)
print(getranksoloduo)
print(getranktft)
print(getrankflex5vs5)
print(getlpsoloduo)
print(getlptft)
print(getlpflex5vs5)
print(getwinssoloduo)
print(getwinstft)
print(getwinsflex5vs5)
print(getlossessoloduo)
print(getlossestft)
print(getlossesflex5vs5)




