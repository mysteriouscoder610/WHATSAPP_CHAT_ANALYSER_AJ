import re
import pandas as pd

def preprocess(data):
    # Regular expression to identify the date and time pattern in WhatsApp messages
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    # Split the raw data into individual messages and dates based on the pattern
    messages = re.split(pattern, data)[1:]  # Extract messages
    dates = re.findall(pattern, data)       # Extract corresponding dates

    # Create a DataFrame with messages and dates
    df = pd.DataFrame({'user_message': messages, 'message_date': dates})

    # Convert 'message_date' column to datetime format for further processing
    df['message_date'] = pd.to_datetime(df['message_date'], format='%m/%d/%y, %H:%M - ')

    # Rename 'message_date' column to 'date' for better readability
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Initialize lists to store extracted users and messages
    users = []
    messages = []

    # Iterate over each message to separate user and message content
    for message in df['user_message']:
        # Split the message into user and message components based on the first colon
        entry = re.split(r'([^:]+):\s', message)
        if entry[1:]:  # If a user is present
            users.append(entry[1])  # Append the user
            messages.append(entry[2])  # Append the message content
        else:
            # For system messages (e.g., "group_notification"), no user is present
            users.append('group_notification')
            messages.append(entry[0])

    # Add the extracted users and messages as new columns in the DataFrame
    df['user'] = users
    df['message'] = messages

    # Remove the original 'user_message' column as it's no longer needed
    df.drop(columns=['user_message'], inplace=True)

    # Extract additional date-related features from the 'date' column
    df['only_date'] = df['date'].dt.date  # Extract only the date
    df['year'] = df['date'].dt.year       # Extract the year
    df['month_num'] = df['date'].dt.month # Extract the month as a number
    df['month'] = df['date'].dt.month_name() # Extract the month as a name
    df['day'] = df['date'].dt.day         # Extract the day of the month
    df['day_name'] = df['date'].dt.day_name() # Extract the name of the day

    # Extract time-related features from the 'date' column
    df['hour'] = df['date'].dt.hour       # Extract the hour
    df['minute'] = df['date'].dt.minute   # Extract the minute

    # Create a new column 'period' to group messages into hourly intervals
    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:  # For the hour 23, the period is "23-00"
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0: # For the hour 0, the period is "00-01"
            period.append(str('00') + "-" + str(hour + 1))
        else:           # For all other hours, create intervals like "14-15"
            period.append(str(hour) + "-" + str(hour + 1))

    # Add the 'period' column to the DataFrame
    df['period'] = period

    # Return the processed DataFrame
    return df
