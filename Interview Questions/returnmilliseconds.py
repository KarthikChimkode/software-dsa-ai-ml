def past(h, m, s):
    # Good Luck!
    seconds = (h * 3600 + m * 60 + s)
    milliseconds = seconds * 1000
    return milliseconds

h = int(input("Enter the number of hours: "))
m = int(input("Enter the number of minutes: "))
s = int(input("Enter the number of seconds: "))


# Clock shows h hours, m minutes and s seconds after midnight.

# Your task is to write a function which returns the time since midnight in milliseconds.

# why use 3600 and 60 and 1000


# ChatGPT said:
# Great question! Here's the why behind using 3600, 60, and 1000 when converting time (hours, minutes, seconds) into milliseconds:

# 🔢 Breakdown of Time Units
# Unit	Equivalent in Seconds	Equivalent in Milliseconds
# 1 hour	3600 seconds	3600 * 1000 = 3,600,000 ms
# 1 minute	60 seconds	60 * 1000 = 60,000 ms
# 1 second	—	1000 milliseconds

# ✅ So Why Use:
# 3600 → because 1 hour = 60 minutes × 60 seconds = 3600 seconds

# 60 → because 1 minute = 60 seconds

# 1000 → because 1 second = 1000 milliseconds

