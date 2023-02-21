while True:
    # I made it more realistic :)
    name = input("Name of Offender: ")  # offender name
    speed = int(input("Speed Over Speed Limit: "))  # speed over limit
    if speed >= 45:  # algorithm
        fine = 630
    elif speed >= 20:
        fine = (speed / 5) * 50 + 30
    elif speed < 10:
        fine = "why did you even bother pulling them over? but its 30"
    else:
        fine = 120
    print(f"##########\n"
          f"Offender Name: {name}\n"
          f"Speed Over Speedlimit: {speed}\n"
          f"Ticket Fee: {fine}\n"
          f"##########")
