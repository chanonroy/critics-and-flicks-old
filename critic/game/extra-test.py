import random

l = [{'url1': 'youtube link 1', 'real': 'Gods of Egypt', 'real_u': 'youtube link 2',
      'url3': 'youtube link 3', 'sim3': 'Deadpool', 'sim1': 'Steve Jobs',
      'url4': 'youtube link 4', 'sim4': '300'}]
l = l[0]

new = {l['real']: l['real_u'], l['sim1']: l['url1'], l['sim3']: l['url3'], l['sim4']: l['url4']}

print(l)
print(new)



# create list of five, shuffle, add 3 in
# add in real, shuffle list again