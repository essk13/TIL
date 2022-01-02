record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
user_nick = {}

for i in range(len(record)):
    user = record[i].split()
    if user[0] == 'Enter' or user[0] == 'Change':
        user_nick.update({user[1]: user[2]})

ans = []
for j in range(len(record)):
    user = record[j].split()
    uid = user[1]
    if user[0] == 'Enter':
        ans.append('{}님이 들어왔습니다.'.format(user_nick[uid]))
    elif user[0] == 'Leave':
        ans.append('{}님이 나갔습니다.'.format(user_nick[uid]))

print(ans)
