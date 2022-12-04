# find, index, rfind

message = 'The quick brown fox jumped over the lazy dog.'
idx = message.find('own')
if idx != -1:
  print(f'Found"own" at index {idx}')
else:
    print('Not found"own"')
idx = message.find('owl')
if idx != -1:
  print =(f'Found"owl"at index{idx}')
else:
    print('Not found"owl"')

idx = message.find('brown',10)
print(idx)