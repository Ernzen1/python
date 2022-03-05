import time

sec = 0
minu = 0
hour = 0

while True:
    if hour < 24 and minu < 60 and sec < 60:
        print(f"{hour}:{minu}:{sec}")
        sec += 1
        time.sleep(1)
        continue
    elif hour < 24 and minu < 60:
        sec = 0
        minu += 1
        continue
    elif hour < 24:
        minu = 0
        hour += 1
        continue
    else:
        hour = 0
        minu = 0
        sec = 0
        break
