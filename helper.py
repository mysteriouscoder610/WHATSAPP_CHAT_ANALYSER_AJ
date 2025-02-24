# Import necessary libraries
from urlextract import URLExtract  # For extracting URLs from text
from wordcloud import WordCloud  # For generating word clouds
import pandas as pd  # For data manipulation and analysis
from collections import Counter  # For counting elements in lists or iterables
import emoji  # For handling emojis in messages

# Create an instance of URLExtract to find URLs in text
extract = URLExtract()

# Function to fetch statistics for the selected user
def fetch_stats(selected_user, df):
    # Filter data for the selected user, if not "Overall"
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Number of messages
    num_messages = df.shape[0]

    # Total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())  # Split each message into words and add to the list

    # Number of media messages (e.g., images, videos)
    num_media_msgs = df[df['message'] == '<Media omitted>\n'].shape[0]

    # Number of links shared
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))  # Extract URLs from each message

    return num_messages, len(words), num_media_msgs, len(links)

# Function to find the most active users in the group
def most_busy_users(df):
    x = df['user'].value_counts().head()  # Get the top users by message count
    # Calculate percentage contribution for each user
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'user': 'name', 'count': 'percent'})
    return x, df

# Function to create a word cloud for the selected user's messages
def create_wordcloud(selected_user, df):
    # Load a custom list of stop words
    f = open('D:\project\WHATSAPP-CHAT-ANALYSIS\pythonProject\stop_hinglish.txt', 'r')
    stop_words = f.read()

    # Filter data for the selected user, if not "Overall"
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Exclude system-generated notifications and media messages
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    # Function to remove stop words from a message
    def remove_stop_words(message):
        y = [word for word in message.lower().split() if word not in stop_words]
        return " ".join(y)

    # Apply stop word removal and generate the word cloud
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='White')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))  # Combine all messages into a single string
    return df_wc

# Function to find the most common words used
def most_common_words(selected_user, df):
    # Load the stop words list
    f = open('D:\project\WHATSAPP-CHAT-ANALYSIS\pythonProject\stop_hinglish.txt', 'r')
    stop_words = f.read()

    # Filter data for the selected user, if not "Overall"
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Exclude system-generated notifications and media messages
    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []

    # Collect all words except stop words
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    # Return the 20 most common words as a DataFrame
    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

# Function to analyze emojis used in messages
def emoji_helper(selected_user, df):
    # Filter data for the selected user, if not "Overall"
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []

    # Extract emojis from messages
    for message in df['message']:
        emojis.extend([c for c in message if emoji.is_emoji(c)])  # Check if character is an emoji

    # Create a DataFrame with emoji counts
    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emoji_df

# Function to create a monthly timeline of messages
def monthly_timeline(selected_user, df):
    # Filter data for the selected user, if not "Overall"
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Group messages by year and month
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    # Combine month and year for display
    time = [timeline['month'][i] + "-" + str(timeline['year'][i]) for i in range(timeline.shape[0])]
    timeline['time'] = time

    return timeline

# Function to create a daily timeline of messages
def daily_timeline(selected_user, df):
    # Filter data for the selected user, if not "Overall"
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Group messages by date
    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    return daily_timeline

# Function to analyze the busiest days of the week
def week_activity_map(selected_user, df):
    # Filter data for the selected user, if not "Overall"
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

# Function to analyze the busiest months
def month_activity_map(selected_user, df):
    # Filter data for the selected user, if not "Overall"
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

# Function to create a heatmap of activity based on day and time periods
def activity_heatmap(selected_user, df):
    # Filter data for the selected user, if not "Overall"
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Create a pivot table with day names and time periods
    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)
    return user_heatmap
