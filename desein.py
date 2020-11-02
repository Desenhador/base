from datetime import datetime
import git

def isint(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

repo = git.Repo(".")
origin = repo.remote(name='origin')
origin.pull()

day_a = datetime.utcnow()
f = open("date", "r")
day_r = f.read().split()
f.close()

if (day_a.day==int(day_r[0])) and (day_a.month==int(day_r[1])) and (day_a.year==int(day_r[2])):
    print('aloha')
    exit()

f = open("date", "w")
f.write(str(day_a.day)+' '+str(day_a.month)+' '+str(day_a.year))
f.close()
repo.index.add("date")

f = open("pic", "r")
pic = list(f.read())
f.close()

for ii in range(len(pic)):
    if isint(pic[ii]):
        nat=int(ii)
        pos=ii
        break

for ii in range(nat):
    pic[pos]=str(int(pic[pos])-1)
    f = open("pic", "w")
    f.write("".join(pic))
    f.close()
    repo.index.add("pic")
    repo.index.commit("JM"+str(day_a.day)+str(ii))
    origin.push()

pic[pos]="E"
f = open("pic", "w")
f.write("".join(pic))
f.close()
repo.index.add("pic")
repo.index.commit("JM"+str(day_a.day)+'E')
origin.push()

