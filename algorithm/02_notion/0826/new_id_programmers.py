new_id = input()
new_id = new_id.lower()
non_alpha = ['-', '_', '.']
delete = []

for i in range(len(new_id)):
    if not (ord('0') <= ord(new_id[i]) <= ord('9')):
        if ord('a') > ord(new_id[i]) or ord('z') < ord(new_id[i]):
            if new_id[i] not in non_alpha and not new_id[i] in delete:
                delete.append(new_id[i])

for j in range(len(delete)):
    new_id = new_id.replace(delete[j], '')

new_id = list(new_id)
front = 0
while front < len(new_id) - 1:
    if new_id[front] == '.' and new_id[front + 1] == '.':
        new_id.pop(front)
        continue
    front += 1

if len(new_id) != 0:
    if new_id[0] == '.':
        new_id.pop(0)
    if len(new_id) != 0:
        if new_id[len(new_id)-1] == '.':
            new_id.pop(len(new_id)-1)

while len(new_id) > 15:
    new_id.pop()

if len(new_id) != 0:
    if new_id[0] == '.':
        new_id.pop(0)
    if len(new_id) != 0:
        if new_id[len(new_id)-1] == '.':
            new_id.pop(len(new_id)-1)

if not new_id:
    new_id.append('a')

if len(new_id) < 3:
    while len(new_id) < 3:
        new_id.append(new_id[-1])

ans = ''.join(new_id)
