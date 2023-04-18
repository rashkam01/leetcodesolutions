friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 5, 7, 9]

long_timers = {friends[i]: time_since_seen[i] 
               for i in range(len(time_since_seen))
               }

print(long_timers)