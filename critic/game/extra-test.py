import random

l = [{'url1': 'youtube link 1', 'real': 'Gods of Egypt', 'real_u': 'youtube link 2',
      'url3': 'youtube link 3', 'sim3': 'Deadpool', 'sim1': 'Steve Jobs',
      'url4': 'youtube link 4', 'sim4': '300'}]
l = l[0]

new = {l['real']: (l['real_u'], 'blank'), l['sim1']: (l['url1'], 'blank'),
       l['sim3']: (l['url3'], 'blank'), l['sim4']: (l['url4'], 'blank')}

for key, value in new.items():
      print("{} {} {}".format(key, value[0], value[1]))

