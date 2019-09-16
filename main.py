from riotwatcher import RiotWatcher, ApiError



watcher = RiotWatcher('RGAPI-6afbce6a-761d-4116-b2f2-089a6b8f8798')

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
mylosesthisseason = leagueinfosoloduo.get("losses")
print(mylosesthisseason)


matchlist = watcher.match.matchlist_by_account(my_region,accountId)
#print(matchlist)
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
		mydivisiontft = leagueinfoflex.get("tier")
		return mydivisiontft

meinletztesgame = game(my_region, summonername)
getdiv = meinletztesgame.getdivisionssoloduo()
getdivtft = meinletztesgame.getdivisiontft
print(getdiv)




