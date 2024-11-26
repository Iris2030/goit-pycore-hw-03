from datetime import datetime

def get_days_from_today(date_str):
    try:
        # Validate and parse the date string
        formatted_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        # Return an error message if the date is not valid
        print("Invalid date format. Please use 'YYYY-MM-DD'.")
        return
    
    # Get today's date
    today_date = datetime.today().date()
    
    # Calculate the difference in days
    difference = today_date - formatted_date
    
    # Return the number of days
    print(difference.days)
    return difference.days

# Test with a valid date
get_days_from_today('2026-11-11')  # Should calculate days until this future date

# Test with an invalid date
get_days_from_today('invalid-date')  # Should return an error message