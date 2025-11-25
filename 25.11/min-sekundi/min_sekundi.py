time1 = int(input("whats the time of the first sportist: "))
time2 = int(input("whats the time of the second sportist: "))
time3 = int(input("whats the time of the third sportist: "))

Overall_Time = time1+time2+time3

Mins = Overall_Time//60

Secs = Overall_Time%60

if Secs < 10:
    print(f"Subbed time is {Mins}:{Secs:02d}")
else:
    print(f"Subbed time is {Mins}:{Secs}")