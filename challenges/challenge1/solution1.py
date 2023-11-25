# inputs = hour range(1-12), minute range(0-59), period range(am/pm)
# outputs = four digit string that encodes that time in 24hr format
# noon is 12:00 pm and midnight is 12:00 am
# in 24hr after midnight is 00:00



def change_time_format(time_string):
    # Split the input string into parts (time and period)
    split_string = time_string.split()
    
    # Split the time part into hour and minute
    time_parts = split_string[0].split(":")
    hour = int(time_parts[0])
    minute = int(time_parts[1])

    # Get the period and convert it to uppercase for consistency
    period = split_string[1].upper()

    # Convert to 24-hour format
    if period == "PM" and hour != 12:
        # If it's PM and not 12 PM, add 12 to the hour
        hour += 12
    elif period == "AM" and hour == 12:
        # If it's AM and 12 AM (midnight), set hour to 0
        hour = 00

    # Format the result as a string in the "HH:MM:AM/PM" format
    result = f"{hour:02d}:{minute:02d} {period}"

    # Return the formatted result
    return result

# Example usage
time_string = "1:00 PM"
print(change_time_format(time_string))
