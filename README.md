![Python](https://img.shields.io/badge/python-3.9-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

# SmartScheduler AI Agent

An intelligent voice-based assistant that helps users schedule meetings by integrating Google Calendar with Google Gemini LLM, powered by local speech recognition and synthesis — **100% free, local-first, and API-secure**.

---

## Features

-  Natural conversation using **Google Gemini**
-  Google Calendar API integration (real-time slots)
-  Voice input (Speech-to-Text) &  Voice output (Text-to-Speech)
-  Intelligent fallback and clarifying questions
-  Works entirely free with open-source and Google tools

---

## Project Structure
```bash
SmartScheduler_AI/
├── test_agent.py
├── scheduler_agent.py
├── calendar_utils.py
├── credentials.json   # ←  DO NOT UPLOAD in GitHub
├── token.json         # ←  DO NOT UPLOAD in GitHub
├── .env               # ←  DO NOT UPLOAD in GitHub
├── requirements.txt
└── README.md
```

---

##  Setup Instructions

### 1. Clone & Create Virtual Environment

```bash
git clone https://github.com/your-username/SmartScheduler_AI.git
cd SmartScheduler_AI
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Create a .env file and add:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```
Get a free Gemini API key from https://aistudio.google.com/app/apikey

### 4️. Add Google Calendar API Credentials
Go to Google Cloud Console

Enable Google Calendar API

Create OAuth Client ID credentials

Download credentials.json and place it in the root folder

---
## Running the Agent
In a new terminal, Run
```bash
python test_agent.py
```
Then speak:
```bash
🎙️ "I want to schedule a meeting"
```
Or ask anything else:

---
## Tech Stack
• Gemini 1.5 Flash (google.generativeai)

• Google Calendar API (v3)

• speech_recognition, pyttsx3 for voice

• Python 3.10+ & CLI-based interface 

---
## Notes
DO NOT commit credentials.json or token.json to GitHub

Works offline for voice. Internet required only for:

• Calendar access
• Gemini response

---
## Author

**Samartha**  
B.Tech student at Vellore Institute of Technology 
 
 MySQL • AI/ML • Data Science •  NLP • Google Cloud 
 
 [LinkedIn](https://www.linkedin.com/in/samartha-b0154a293) | [GitHub](https://github.com/Samartha21BRS1698)

---
## License
 MIT License © 2025 Samartha
 ![License](https://img.shields.io/badge/license-MIT-green.svg)