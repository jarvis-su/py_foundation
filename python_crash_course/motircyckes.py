motrocycles = ['honda','yamaha', 'suzuki']
print(motrocycles)

motrocycles = ['honda','yamaha', 'suzuki']
motrocycles[0] = 'ducati'
print(motrocycles)

motrocycles = ['honda','yamaha', 'suzuki']
motrocycles.append('ducati')
print(motrocycles)

motrocycles = ['honda','yamaha', 'suzuki']
motrocycles.insert(0,'ducati')
print(motrocycles)

motrocycles = ['honda','yamaha', 'suzuki']
del motrocycles[0]
print(motrocycles)

motrocycles = ['honda','yamaha', 'suzuki']
del motrocycles[1]
print(motrocycles)

motrocycles = ['honda','yamaha', 'suzuki']
motrocycles.pop()
print(motrocycles)

motrocycles = ['honda','yamaha', 'suzuki']
motrocycles.pop(1)
print(motrocycles)

motrocycles = ['honda','yamaha', 'suzuki']
first_owned = motrocycles.pop(1)
print(f"The first motorcycle I owned was a {first_owned.title()}")


motrocycles = ['honda','yamaha', 'suzuki','ducati' ,'adsfasdf','ducati']
motrocycles.remove('ducati')
print(motrocycles)
