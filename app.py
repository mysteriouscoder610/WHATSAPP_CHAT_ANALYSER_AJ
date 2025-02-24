import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns

# Add custom CSS for styling and animations
st.markdown("""
    <style>
        /* General styling for the app */
        body {
            font-family: "Times New Roman", Serif;
            background-color:rgb(81, 201, 248);
        }
        h1,h2,h3,h4,h5,h6{
            font-family: "Times New Roman", Serif;
            color:rgb(81, 201, 248);
            font-weight: bold;
        }
        .css-1pdp6u2{  /* Sidebar title */
            font-family:"Times New Roman", Serif;
            font-size:20px;
            font-weight:bold;
        }
        .stButton>button{
            font-family:"Times New Roman", Serif;
            background-color:rgb(107, 201, 255);
            color:white;
            border-radius:5px;
            padding:10px;
            transition:all 0.3s ease;
        }
        .stButton>button:hover {
            background-color:rgb(81, 201, 248);
            transform:scale(1.1);
        }
        /* Card styles for statistics */
        .stat-card{
            font-family:"Times New Roman", Serif;
            background-color:rgb(82, 192, 255);
            border:2px solid #00CED1;
            border-radius:10px;
            padding:15px;
            text-align:center;
            margin:10px;
            transition:all 1s ease; /* Smooth transition for animation */
        }
        .stat-card:hover{
            transform:scale(1.1);
            box-shadow:0 5px 15px rgba(0, 0, 0, 0.2);
        }
        /* Animations */
        @keyframes fadeIn{
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .fade-in {
            font-family: "Times New Roman", Serif;
            animation: fadeIn 2s ease;
        }
        .fade-in-delayed {
            font-family: "Times New Roman", Serif;
            animation: fadeIn 2s ease 1s;
        }
        .slide-in {
            animation: fadeIn 2s ease, slideIn 2s ease;
        }
        @keyframes slideIn {
            from { transform: translateY(50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        @keyframes slideInLeft {
            from { transform: translateX(-100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        @keyframes slideInRight {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }

        .stat-card-1 {  animation: slideInLeft 1s ease-out forwards; }
        .stat-card-2 {  animation: slideInRight 1s ease-out forwards; }
        .stat-card-3 {  animation: slideInLeft 1s ease-out forwards; }
        .stat-card-4 {  animation: slideInRight 1s ease-out forwards; }
    </style>
""", unsafe_allow_html=True)

# Sidebar setup
st.sidebar.title("Whatsapp Chat Analyzer")

# File uploader
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    user_name_list = df['user'].unique().tolist()
    user_name_list.remove('group_notification')
    user_name_list.sort()
    user_name_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis with respect to", user_name_list)

    if st.sidebar.button("Show Analysis"):
        # Top Statistics Section
        num_messages, words, num_media_msgs, num_links = helper.fetch_stats(selected_user, df)
        st.markdown("<h1 class='fade-in'>WhatsApp Chat Analyzer</h1>", unsafe_allow_html=True)

        # Creating Tabs
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
            "📊 Top Statistics", 
            "📅 Timeline Analysis", 
            "🗺️ Activity Map", 
            "🔥 Weekly Heatmap", 
            "☁️ Word Cloud", 
            "😂 Emoji Analysis", 
            "📝 Most Common Words"
        ])

        # 🔹 Tab 1: Top Statistics
        with tab1:
            st.markdown("<h2 class='slide-in'>TOP STATISTICS</h2>", unsafe_allow_html=True)
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown(f"<div class='stat-card stat-card-1'><h2>Total Messages</h2><p>{num_messages}</p></div>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"<div class='stat-card stat-card-2'><h2>Total Words</h2><p>{words}</p></div>", unsafe_allow_html=True)
            with col3:
                st.markdown(f"<div class='stat-card stat-card-3'><h2>Media Shared</h2><p>{num_media_msgs}</p></div>", unsafe_allow_html=True)
            with col4:
                st.markdown(f"<div class='stat-card stat-card-4'><h2>Links Shared</h2><p>{num_links}</p></div>", unsafe_allow_html=True)

        # 🔹 Tab 2: Timeline Analysis
        with tab2:
            st.markdown("<h2 class='slide-in'>MONTHLY TIMELINE</h2>", unsafe_allow_html=True)
            timeline = helper.monthly_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(timeline['time'], timeline['message'], color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

            st.markdown("<h2 class='slide-in'>DAILY TIMELINE</h2>", unsafe_allow_html=True)
            daily_timeline = helper.daily_timeline(selected_user, df)
            fig, ax = plt.subplots()
            ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # 🔹 Tab 3: Activity Map
        with tab3:
            st.markdown("<h2 class='slide-in'>ACTIVITY MAP</h2>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.header("Most Busy Day")
                busy_day = helper.week_activity_map(selected_user, df)
                fig, ax = plt.subplots()
                ax.bar(busy_day.index, busy_day.values)
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.header("Most Busy Month")
                busy_month = helper.month_activity_map(selected_user, df)
                fig, ax = plt.subplots()
                ax.bar(busy_month.index, busy_month.values, color='orange')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

        # 🔹 Tab 4: Weekly Heatmap
        with tab4:
            st.markdown("<h2 class='slide-in'>WEEKLY ACTIVITY MAP</h2>", unsafe_allow_html=True)
            user_heatmap = helper.activity_heatmap(selected_user, df)
            fig, ax = plt.subplots()
            sns.heatmap(user_heatmap, ax=ax)
            st.pyplot(fig)

        # 🔹 Tab 5: Word Cloud
        with tab5:
            st.markdown("<h2 class='slide-in'>WORD CLOUD</h2>", unsafe_allow_html=True)
            df_wc = helper.create_wordcloud(selected_user, df)
            fig, ax = plt.subplots()
            plt.imshow(df_wc)
            plt.axis("off")
            st.pyplot(fig)

        # 🔹 Tab 6: Emoji Analysis
        with tab6:
            emoji_df = helper.emoji_helper(selected_user, df)
            st.write("Emoji DataFrame columns:", emoji_df.columns.tolist())  # Debug line
            st.markdown("<h2 class='fade-in'>EMOJI ANALYSIS</h2>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.dataframe(emoji_df)
            with col2:
                # Fix the line below based on actual column names
                if not emoji_df.empty:
                    fig, ax = plt.subplots()
                    ax.pie(emoji_df.iloc[:, 1].head(), labels=emoji_df.iloc[:, 0].head(), autopct="%0.2f")
                    st.pyplot(fig)
                else:
                    st.write("No emoji data to display")

        # 🔹 Tab 7: Most Common Words
        with tab7:
            most_common_df = helper.most_common_words(selected_user, df)
            st.markdown("<h2 class='slide-in'>MOST COMMON WORDS</h2>", unsafe_allow_html=True)
            fig, ax = plt.subplots()
            ax.bar(most_common_df[0], most_common_df[1])
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
