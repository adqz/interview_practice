w10_start, w10_end = 1, 10
w60_start, w60_end = 1, 60
w10_co = 0

for time, count in bind_d.items():
    w10_window += count
    if time == w10_end:
        