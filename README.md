# Weatherbot

Weatherbot is a voice-activated weather assistant that provides current weather information and forecasts based on user queries. The project consists of a frontend built with React and Vite, and a backend built with FastAPI.

## Project Structure
```
backend/
├── app/
│   ├── main.py
│   └── requirements.txt
frontend/
├── .gitignore
├── eslint.config.js
├── index.html
├── package.json
├── src/
│   ├── App.css
│   ├── App.jsx
│   ├── components/
│   │   └── VoiceAssistant.jsx
│   └── main.jsx
├── vite.config.js
└── README.md
```



## Frontend

### Installation

1. Navigate to the `frontend` directory:
    Run the command: 
        "cd frontend"

2. Install the dependencies:
    Run the command:
        "npm install"


### Running the Frontend

1. To start the development server, run:
    Run the command:
        "npm run dev"


# Usage
    1. Open the application in your browser.
    2. Press the "🎤 Speak" button to activate the voice assistant.
    3. Speak clearly and loud enough to recognize the audio. Only city names are taken as audio input.


# Debugging
1. Ensure your microphone is working and set to the default system microphone if any issues arise.
2. Check the browser console for any errors.



# Backend

## Installation
1. Navigate to the app directory:
    Run the command:
        "cd backend/app"

2. Install the dependencies:
    Run the command:
        "pip install -r requirements.txt"

3. Running the Backend
    To start the FastAPI server, run:
        "python -m uvicorn app.main:app --reload"


# Notes
1. Ensure you have a valid OpenWeatherMap API key and update the API_KEY variable in main.py.
2. Check the localhost URL for frontend and backend integration.


# Integration
The frontend and backend are integrated via API calls. The frontend sends requests to the backend to fetch weather data based on user queries.