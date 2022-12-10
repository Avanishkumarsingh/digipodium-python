movies = ['bahubali','kantara','avatar','one man army','jabtak hai jaan','pk','pad man']
stars = ['⭐⭐⭐⭐⭐','⭐⭐⭐','⭐⭐⭐⭐','⭐⭐⭐','⭐⭐⭐','⭐⭐','⭐⭐⭐⭐']

for movie,star in zip(movies,stars):
    print(f'{movie:<18} {star}')