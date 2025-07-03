# 📱 WhatsApp Chat Analyzer

A comprehensive and visually stunning web application built with Streamlit that analyzes WhatsApp chat exports to provide detailed insights into messaging patterns, user behavior, and conversation dynamics.

## 🎯 Project Overview

The WhatsApp Chat Analyzer is designed to transform your exported WhatsApp chat data into meaningful visualizations and statistics. With an elegant animated interface and comprehensive analytics, this tool helps you understand communication patterns, identify trends, and gain insights from your chat history.

## ✨ Features

### 📊 **Top Statistics**
- **Total Messages**: Count of all messages exchanged
- **Total Words**: Complete word count analysis
- **Media Shared**: Number of images, videos, and other media files
- **Links Shared**: Count of URLs shared in conversations

### 📈 **Timeline Analysis**
- **Monthly Timeline**: Message frequency trends over months
- **Daily Timeline**: Day-by-day messaging patterns
- Interactive line charts with temporal insights

### 🗺️ **Activity Mapping**
- **Busiest Days**: Identify which days of the week are most active
- **Busiest Months**: Discover seasonal messaging patterns
- Color-coded bar charts for easy visualization

### 🔥 **Weekly Heatmap**
- Interactive heatmap showing activity by day and hour
- Identify peak communication times
- Visual representation of messaging habits

### ☁️ **Word Cloud Generation**
- Beautiful word clouds highlighting frequently used terms
- Intelligent filtering of stop words (supports Hinglish)
- Customizable appearance with clean styling

### 😂 **Emoji Analysis**
- Comprehensive emoji usage statistics
- Interactive pie charts showing emoji distribution
- Identify most popular emojis in conversations

### 📝 **Most Common Words**
- Top 20 most frequently used words
- Filtered analysis excluding common stop words
- Bar chart visualization for easy comparison

## 🎨 User Interface

The application features a modern, animated interface with:
- **Smooth animations** and hover effects
- **Responsive design** with sliding card animations
- **Professional color scheme** with Times New Roman typography
- **Tabbed interface** for organized content presentation
- **Interactive elements** with smooth transitions

## 🚀 Getting Started

### Prerequisites

```bash
pip install streamlit
pip install pandas
pip install matplotlib
pip install seaborn
pip install wordcloud
pip install urlextract
pip install emoji
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/WHATSAPP_CHAT_ANALYSER_AJ.git
   cd WHATSAPP_CHAT_ANALYSER_AJ
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📱 How to Export WhatsApp Chat

1. **Open WhatsApp** on your mobile device
2. **Go to the chat** you want to analyze
3. **Tap the three dots** (menu) in the top right corner
4. **Select "More"** → **"Export Chat"**
5. **Choose "Without Media"** for faster processing
6. **Save the .txt file** to your device

## 🔧 Usage

1. **Launch the application** using `streamlit run app.py`
2. **Upload your exported chat file** using the file uploader in the sidebar
3. **Select analysis scope**:
   - **"Overall"**: Analyze the entire group chat
   - **Individual User**: Focus on a specific participant
4. **Click "Show Analysis"** to generate comprehensive insights
5. **Navigate through tabs** to explore different analytics

## 📁 Project Structure

```
WHATSAPP_CHAT_ANALYSER_AJ/
├── app.py                 # Main Streamlit application
├── preprocessor.py        # Data preprocessing and cleaning
├── helper.py             # Analytics and visualization functions
├── stop_hinglish.txt     # Stop words for text filtering
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## 🛠️ Technical Details

### **Data Processing**
- **Regex-based parsing** for message extraction
- **DateTime handling** for temporal analysis
- **Text preprocessing** with stop word removal
- **Emoji detection** and analysis

### **Visualization Libraries**
- **Matplotlib**: Core plotting functionality
- **Seaborn**: Statistical visualizations and heatmaps
- **WordCloud**: Text visualization
- **Streamlit**: Interactive web interface

### **Key Components**
- **preprocessor.py**: Handles chat data parsing and cleaning
- **helper.py**: Contains all analytics and visualization functions
- **app.py**: Main application with UI and user interactions

## 🎭 Supported Languages

The analyzer supports **Hinglish** (Hindi + English) text analysis with:
- Comprehensive stop word filtering
- Unicode emoji support
- Multi-language word cloud generation

## 📸 Screenshots

<!-- Add your screenshot here -->
![WhatsApp Chat Analyzer Interface](path/to/your/screenshot.png)

*Screenshot showing the main interface with animated statistics cards and timeline analysis*

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

## 📈 Future Enhancements

- [ ] **Sentiment Analysis** integration
- [ ] **User comparison** charts
- [ ] **Export functionality** for generated reports
- [ ] **Dark mode** toggle
- [ ] **Advanced filtering** options
- [ ] **Machine learning** insights

## 🐛 Known Issues

- Large chat files may take longer to process
- Some emoji characters might not display correctly on all systems
- Media analysis is limited to count only (actual media files not processed)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**AJ** - [GitHub Profile](https://github.com/yourusername)

## 🙏 Acknowledgments

- **Streamlit** team for the amazing framework
- **Python community** for excellent data science libraries
- **Contributors** who helped improve this project

## 📞 Support

If you encounter any issues or have suggestions:
- **Open an issue** on GitHub
- **Star the repository** if you find it useful
- **Share with friends** who might benefit from this tool

---

<div align="center">
  <strong>Made with ❤️ and Python</strong>
</div>

---

### 🔗 Quick Links

- [Installation Guide](#-getting-started)
- [Usage Instructions](#-usage)
- [Technical Documentation](#-technical-details)
- [Contributing Guidelines](#-contributing)
