# section_039.py

s_planet = {'수성','금성','지구','화성','목성','토성','천왕성','해왕성'}

print(s_planet)
print()

s_planet.discard('금성')
print(s_planet)
s_planet.remove('천왕성')
print(s_planet)
print()


s_planet.clear()
print(s_planet)