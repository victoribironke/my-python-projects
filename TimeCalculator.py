seconds = int(input("Enter number of seconds: "))

if seconds < 60:
    print(f"{seconds} seconds.")
elif 60 <= seconds < 3600:
    mins = seconds // 60
    secs = seconds % 60
    print(f"{mins} minute(s) {secs} second(s)")
elif 3600 <= seconds < 86400:
    hrs = seconds // 3600
    seconds = seconds % 3600
    mins = seconds // 60
    secs = seconds % 60
    print(f"{hrs} hour(s) {mins} minute(s) {secs} second(s)")
elif seconds >= 86400:
    days = seconds // 86400
    seconds = seconds % 86400
    hrs = seconds // 3600
    seconds = seconds % 3600
    mins = seconds // 60
    secs = seconds % 60
    print(f"{days} day(s) {hrs} hour(s) {mins} minute(s) {secs} second(s)")
