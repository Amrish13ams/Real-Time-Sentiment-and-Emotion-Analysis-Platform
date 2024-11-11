
# Real-Time Sentiment and Emotion Analysis Platform

This project combines Flask and Django to create a platform where users can analyze the sentiment of text and detect emotions in images or video streams. Django manages the web interface and user management, while Flask serves as a microservice to handle machine learning model inferences.

## Features
- Text Sentiment Analysis
- Emotion Detection in Images or Video
- Real-Time Analysis with AJAX
- Data Visualization Dashboard for Trends and Insights

## Technologies Used
- Django for the web framework
- Flask for serving model APIs
- TensorFlow/Keras for emotion detection models
- NLTK/TextBlob for sentiment analysis

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/username/RealTimeSentimentEmotionAnalysis.git
   cd RealTimeSentimentEmotionAnalysis
   ```

2. **Set up Django**
   ```bash
   cd django_app
   python3 -m venv env
   source env/bin/activate  # For Linux/Mac, use env\Scriptsctivate for Windows
   pip install -r ../requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

3. **Set up Flask**
   ```bash
   cd flask_app
   python3 -m venv env
   source env/bin/activate  # For Linux/Mac, use env\Scriptsctivate for Windows
   pip install -r requirements.txt
   python app.py
   ```
