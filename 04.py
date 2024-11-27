from datetime import datetime, timedelta

users = [
    {"name": "Jared Padalecki", "birthday": "1982.07.19"},
    {"name": "Misha Collins", "birthday": "1974.08.20"},
    {"name": "Coco Fleur Fortuna Smile", "birthday": "2018.09.13"},
    {"name": "Luna Black", "birthday": "2024.11.29"},
    {"name": "Poli Best", "birthday": "2024.12.01"}
]

def get_upcoming_birthdays():
    
    today_date = datetime.today().date()
    next_week_date = today_date + timedelta(days=7)
    birthday_list = []
    
    for user in users:
        # Convert the user's birthday to a date object
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Calculate the user's birthday in the current year
        user_birthday_this_year = user_birthday.replace(year=today_date.year)
        
        # If the birthday already passed this year, move it to the next year
        if user_birthday_this_year < today_date:
            user_birthday_this_year = user_birthday.replace(year=today_date.year + 1)
        
        # Check if the birthday is within the next 7 days
        if today_date <= user_birthday_this_year <= next_week_date:
            # If the birthday is on a weekend, move it to the following Monday
            if user_birthday_this_year.weekday() == 5:  # Saturday
                congratulation_date = user_birthday_this_year + timedelta(days=2)  
            elif user_birthday_this_year.weekday() == 6:  # Sunday
                congratulation_date = user_birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = user_birthday_this_year  # Not a weekend
            

            birthday_list.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%d-%m-%Y")
            })

    return birthday_list
    
print(get_upcoming_birthdays())