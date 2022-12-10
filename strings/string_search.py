# find, index, rfind

message = 'The quick brown fox jumped over the lazy dog.'
idx  = message.find('own')
if idx != -1:
  print(f'Found"own" at index{idx}')
else:
  print('Not found "own"')
idx = message.find('owl')
if idx != -1:
  print(f'Found"owl" at index{idx}')
else:
  print('Not found "owl"')

idx = message.find('jumped',21)
print(idx)


message = 'The dog was running on the road behind the car.'
idx =message.find('ing')
if idx != -1:
  print(f'found "ing" at index{idx}')
else:
  print('Not found "ing"')
idx =message.find('rod')
if idx != -1:
  print(f'found "rod" at index{idx}')
else:
  print('Not found "rod"')