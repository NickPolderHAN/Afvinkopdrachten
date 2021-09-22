# opdracht 1 bug collector
bugs_collected = 0
days = 0

while days <= 4:
    bugs_collected += int(input("How many bugs were collected?"))
    days += 1
else:
    print("The total amount of bugs collected is: " + str(bugs_collected))

# opdracht 3 lap time
lap_times = []
laps_ran = int(input("How many laps did you run?"))
counter_num = 1
lap_time_printed = 1
total_time = 0.0

while counter_num < laps_ran + 1:
    lap_time_hold = float(input("What was your time for lap " + str(counter_num) + "?"))
    counter_num += 1
    lap_times.append(str(lap_time_hold))
    total_time += lap_time_hold

while lap_time_printed < counter_num:
    index_printed = lap_time_printed - 1
    print("Lap " + str(lap_time_printed) + ": " + lap_times[index_printed])
    lap_time_printed += 1
else:
    lap_times.sort()
    print("Your fastest lap was: " + str(lap_times[0]))
    print("Your average lap was: " + str(total_time / counter_num))
    print("Your slowest lap was: " + str(lap_times[len(lap_times) - 1]))

# opdracht 12 Calculating the Factorial of a Number
getal = int(input("Vul een heel getal in, "))
total = 1

for i in range(getal):
    total *= (i + 1)

print(f"{getal} = {total}")
