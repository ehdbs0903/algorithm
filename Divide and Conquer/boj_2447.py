def draw_stars(m):
  if m == 1:
    return ['*']

  stars=draw_stars(m // 3)
  li = []

  for star in stars:
    li.append(star * 3)
  for star in stars:
    li.append(star + ' ' * (m // 3) + star)
  for star in stars:
    li.append(star * 3)

  return li

n = int(input())
print('\n'.join(draw_stars(n)))
