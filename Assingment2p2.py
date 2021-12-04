
caffeine_mg = float(input())
half_life1 = caffeine_mg / 2
half_life2 = half_life1 / 2
half_life3 = half_life2 / 4
print('After 6 hours: {:.2f} mg'.format(half_life1))
print('After 12 hours: {:.2f} mg'.format(half_life2))
print('After 24 hours: {:.2f} mg'.format(half_life3))
