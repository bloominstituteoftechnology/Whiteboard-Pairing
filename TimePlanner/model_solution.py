def time_planner(a, b, duration):
  a_count = 0
  b_count = 0

  while a_count < len(a) and b_count < len(b):
    start = max(a[a_count][0], b[b_count][0])
    end = min(a[a_count][1], b[b_count][1])

    if start + duration <= end:
      return (start, start + duration)

    if a[a_count][1] < b[b_count][1]:
      a_count += 1
    else:
      b_count += 1
  
  return ()


# Some simple print tests
print(time_planner(
  [(10, 50), (60, 120), (140, 210)],
  [(0, 15), (60, 70)],
  8
))  # should print (60, 68)

print(time_planner(
  [(10, 50), (60, 120), (140, 210)],
  [(0, 15), (60, 72)],
  12
))  # should print (60, 72)

print(time_planner(
  [(10, 50), (60, 120), (140, 210)],
  [(0, 15), (60, 70)],
  12
))  # should print ()

print(time_planner(
  [(0, 5), (50, 70), (120, 125)],
  [(0, 50)],
  8
))  # should print ()