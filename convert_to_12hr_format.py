def convert_to_12hr(hour,minute):
    if hour==0:
        hour_12=12
        period="AM"
    elif hour==12:
        hour_12=12
        period="PM"
    elif hour<12:
        hour_12=hour
        period="AM"
    else:
        hour_12=hour-12
        period="PM"
        
    minute=f"{minute:02}"
    return f"{hour_12}:{minute}{period}"
    
hour_24 = 12  # Try different values like 0, 11, 15, etc.
minute = 3
time_12hr = convert_to_12hr(hour_24, minute)
print(f"24-hour format: {hour_24}:{minute:02}")
print(f"12-hour format: {time_12hr}")