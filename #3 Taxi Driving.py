import datetime


def time_getter():
    hours = datetime.datetime.now().strftime("%H")
    minutes = datetime.datetime.now().strftime("%M")
    return [int(hours), int(minutes)]


def ride_calculator(entry_o, exit_k):
    hours = exit_k[0] - entry_o[0]
    minutes = exit_k[1] - entry_o[1]
    if hours < 0:
        hours += 24
    if minutes < 0:
        minutes += 60
    hours *= 60
    return hours + minutes


driverFullName = input("What is your full name: ")
day_total = []
minutes_driven = 0

while True:
    pipis = input("Type 1 to continue or 2 to stop day")
    if pipis == "1":
        start_time = time_getter()
        input("click enter to end ride!")
        stop_time = time_getter()
        day_total.append(ride_calculator(start_time, stop_time))
    elif pipis == "2":
        for i in range(len(day_total)):
            minutes_driven += day_total[i]
        print(f"Driver: {driverFullName}\n"
              f"Total Time Driven: {minutes_driven}\n"
              f"Average Time Driven: {minutes_driven/len(day_total)}\n"
              f"Total Income before 'TAX': {minutes_driven * 2 + 10}\n"
              f"Average Cost of All Trips: {minutes_driven * 2 + 10/len(day_total)}\n"
              f"Total Money Received: ${(minutes_driven * 2 + 10) * 0.4}")

