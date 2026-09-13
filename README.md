<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:020617,45:45000f,100:ff1744&height=230&section=header&text=TubePlease%20Agent&fontSize=52&fontColor=ffffff&animation=twinkling&fontAlignY=38&desc=AI-Powered%20YouTube%20%26%20Gmail%20Assistant&descAlignY=62&descSize=18" width="100%"/>

<br>

# 🎬 TubePlease Agent

### Your command. Your content. Your assistant.

An intelligent Flask-based assistant that turns natural-language commands into **YouTube playback actions** and **AI-generated Gmail drafts**.

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.1-000000?style=for-the-badge\&logo=flask\&logoColor=white)
![Gemini](https://img.shields.io/badge/Google%20Gemini-AI-4285F4?style=for-the-badge\&logo=google\&logoColor=white)
![YouTube](https://img.shields.io/badge/YouTube-Integration-FF0000?style=for-the-badge\&logo=youtube\&logoColor=white)
![Gmail](https://img.shields.io/badge/Gmail-Integration-EA4335?style=for-the-badge\&logo=gmail\&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-Production-499848?style=for-the-badge\&logo=gunicorn\&logoColor=white)

<br>

[![GitHub](https://img.shields.io/badge/View%20Repository-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/Azam-star/TubePlease-Agent)

</div>

---

## 🧠 What is TubePlease Agent?

**TubePlease Agent** is a lightweight AI assistant backend designed to understand everyday commands and convert them into useful actions.

Instead of navigating multiple services manually, a user can give commands such as:

```text
Play Believer by Imagine Dragons
```

or:

```text
Write an email to professor@example.com asking for tomorrow's meeting.
```

The agent determines the requested action and routes it to the appropriate service.

### 🎯 Core capabilities

| Capability         | Description                                                 |
| ------------------ | ----------------------------------------------------------- |
| 🎬 YouTube Agent   | Searches YouTube and generates an embeddable playback URL   |
| 📧 Gmail Agent     | Converts natural-language commands into professional emails |
| 🤖 Gemini AI       | Generates concise email subject + body content              |
| 🔗 Gmail Compose   | Creates a pre-filled Gmail compose URL                      |
| 🌐 REST API        | Exposes clean Flask endpoints for external clients          |
| ❤️ Health Check    | Provides a simple service health endpoint                   |
| ⚡ Production Ready | Includes WSGI + Gunicorn configuration                      |

---

# ✨ Features

## 🎬 YouTube Playback Agent

The YouTube module accepts commands such as:

```text
play song Believer
play music Shape of You
play youtube Perfect
play Blinding Lights
```

The system:

```text
User Command
      ↓
Command Parsing
      ↓
YouTube Search
      ↓
Extract Video ID
      ↓
Generate Embed URL
      ↓
Return JSON Response
```

The search implementation retrieves the first matching YouTube video ID and generates an autoplay embed URL.

---

## 📧 AI Gmail Agent

TubePlease Agent can transform natural-language instructions into professional emails.

Example:

```text
Write an email to teacher@example.com
asking for permission to attend the workshop.
```

The backend:

```text
Natural Language Command
          ↓
Email Command Detection
          ↓
Recipient Extraction
          ↓
Gemini AI Generation
          ↓
Subject + Email Body
          ↓
Gmail Compose URL
```

The Gemini integration is designed to generate concise emails with an appropriate greeting and closing without inventing unsupported facts.

---

# 🤖 AI Email Generation

The project uses Google's Gemini API for email generation.

The model is configurable through an environment variable:

```bash
GEMINI_MODEL
```

The API key is read from:

```bash
Gemini_API_Key
```

> ⚠️ Never commit your Gemini API key directly into the repository.

The application validates the API response and extracts:

```text
SUBJECT
BODY
```

before returning the generated email.

---

# 🏗️ System Architecture

```text
                         ┌─────────────────────┐
                         │       USER          │
                         │ Natural Language    │
                         │      Command        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Flask Server     │
                         │      API Layer      │
                         └──────────┬──────────┘
                                    │
                       ┌────────────┴────────────┐
                       │                         │
                       ▼                         ▼
              ┌─────────────────┐      ┌─────────────────┐
              │ YouTube Agent   │      │  Gmail Agent    │
              │                 │      │                 │
              │ Command Parser  │      │ Email Detector  │
              │       ↓         │      │       ↓         │
              │ YouTube Search  │      │ Email Extractor │
              │       ↓         │      │       ↓         │
              │ Video ID        │      │ Gemini AI       │
              └────────┬────────┘      │       ↓         │
                       │               │ Email Draft     │
                       ▼               └────────┬────────┘
              ┌─────────────────┐               │
              │ YouTube Embed   │               ▼
              │      URL        │      ┌─────────────────┐
              └─────────────────┘      │ Gmail Compose   │
                                       │      URL        │
                                       └─────────────────┘
```

---

# ⚙️ Technology Stack

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| 🐍 Python        | Core programming language |
| 🌐 Flask         | Backend web framework     |
| 🤖 Google Gemini | AI email generation       |
| ▶️ YouTube       | Video search and playback |
| 📧 Gmail         | Email composition         |
| 🔗 Flask-CORS    | Cross-origin API access   |
| 🦄 Gunicorn      | Production WSGI server    |

The repository's dependencies include Flask, Flask-CORS, and Gunicorn.

---

# 📁 Project Structure

```text
TubePlease-Agent/
│
├── app/
│   │
│   ├── __init__.py
│   │
│   ├── gmail/
│   │   ├── __init__.py
│   │   ├── gmail_gen.py
│   │   └── gmail_write.py
│   │
│   ├── youtube/
│   │   ├── __init__.py
│   │   └── player.py
│   │
│   └── templates/
│       └── index.html
│
├── requirements.txt
├── wsgi.py
└── README.md
```

The Flask application registers the YouTube blueprint, serves the HTML interface, exposes `/health`, and provides the `/agent` Gmail endpoint.

---

# 🔌 API Endpoints

## 🏠 Home

```http
GET /
```

Returns the main web interface.

---

## 🌐 HTML Interface

```http
GET /html
```

Serves the project's HTML interface.

---

## ❤️ Health Check

```http
GET /health
```

Example response:

```json
{
  "status": "ok",
  "service": "Miuh AI Agent"
}
```

---

# 📧 Gmail API

```http
POST /agent
```

### Request

```json
{
  "command": "Write an email to professor@example.com asking for a meeting tomorrow"
}
```

### Response

```json
{
  "success": true,
  "type": "email",
  "email_generated": true,
  "recipient": "professor@example.com",
  "subject": "Request for a Meeting",
  "body": "Dear Professor,...",
  "gmail_url": "https://mail.google.com/..."
}
```

The endpoint validates the command, extracts the recipient, generates the email through Gemini, and constructs a Gmail compose URL.

---

# ▶️ YouTube API

```http
POST /youtube/play
```

### Request

```json
{
  "command": "play Believer"
}
```

### Response

```json
{
  "success": true,
  "type": "youtube",
  "query": "play Believer",
  "url": "https://www.youtube.com/embed/..."
}
```

The YouTube blueprint exposes `/youtube/play` and returns an embed URL when a matching video is found.

---

# 🚀 Getting Started

## 1️⃣ Clone the repository

```bash
git clone https://github.com/Azam-star/TubePlease-Agent.git
```

```bash
cd TubePlease-Agent
```

---

## 2️⃣ Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

The current project requirements include Flask, Flask-CORS and Gunicorn.

---

# 🔐 Configure Gemini

Set your Gemini API key as an environment variable.

### Windows PowerShell

```powershell
$env:Gemini_API_Key="YOUR_API_KEY"
```

### macOS / Linux

```bash
export Gemini_API_Key="YOUR_API_KEY"
```

Optional model configuration:

```bash
export GEMINI_MODEL="gemini-3.6-flash"
```

> Keep API keys out of GitHub, screenshots, commits, and frontend code.

---

# ▶️ Run Locally

The WSGI entry point creates the Flask application:

```python
from app import create_app

app = create_app()
```

For development, you can run the application through Flask/Gunicorn according to your local setup.

### Gunicorn

```bash
gunicorn wsgi:app
```

---

# 🧪 Example Commands

### YouTube

```text
play Believer
```

```text
play music Perfect
```

```text
play youtube Shape of You
```

```text
play Blinding Lights
```

### Gmail

```text
Write an email to teacher@example.com asking for leave tomorrow.
```

```text
Draft an email to manager@example.com about the project update.
```

```text
Compose mail to friend@example.com wishing them happy birthday.
```

---

# 🔄 Request Flow

## YouTube

```text
POST /youtube/play
       │
       ▼
Read command
       │
       ▼
Extract search query
       │
       ▼
Search YouTube
       │
       ▼
Extract videoId
       │
       ▼
Generate embed URL
       │
       ▼
Return JSON
```

## Gmail

```text
POST /agent
       │
       ▼
Read command
       │
       ▼
Detect email intent
       │
       ▼
Extract recipient
       │
       ▼
Gemini API
       │
       ▼
Generate subject/body
       │
       ▼
Create Gmail compose URL
       │
       ▼
Return JSON
```

---

# 🛡️ Error Handling

The application handles several common failure cases.

### Missing command

```json
{
  "success": false,
  "message": "Command is required"
}
```

### Invalid Gmail command

```json
{
  "success": false,
  "message": "Please give a Gmail command."
}
```

### YouTube video not found

```json
{
  "success": false,
  "message": "Could not find the song on YouTube"
}
```

### Gemini API failure

The Gemini module retries failed requests and specifically handles rate-limit responses before returning an error.

---

# 🎨 Interface

The project includes a custom HTML interface designed around a dark, futuristic assistant aesthetic.

The interface includes dedicated visual sections for:

```text
        ▶ YouTube

            MIUH AI

                  ✉ Gmail
```

The frontend is served through Flask's template system from:

```text
app/templates/index.html
```

---

# 🔐 Security Notes

For production deployment:

* Store API keys in environment variables.
* Never commit `.env` files containing secrets.
* Restrict CORS origins instead of allowing every origin.
* Add authentication before exposing sensitive endpoints publicly.
* Validate and sanitize user input.
* Add request rate limiting.
* Avoid exposing raw exception messages in production responses.

---

# 🚀 Future Roadmap

Possible improvements for the next version:

* [ ] 🎙️ Real-time voice input
* [ ] 🧠 Multi-command intent detection
* [ ] 🎵 Spotify integration
* [ ] 📧 Direct Gmail API sending
* [ ] 🗣️ Text-to-speech responses
* [ ] 🔐 User authentication
* [ ] 🧾 Conversation history
* [ ] 🧠 Long-term assistant memory
* [ ] 📊 Usage analytics
* [ ] ⚡ Async API processing
* [ ] 🐳 Docker support
* [ ] ☁️ Cloud deployment
* [ ] 🔒 API authentication
* [ ] 🚦 Rate limiting
* [ ] 🧪 Automated tests
* [ ] 🔄 CI/CD pipeline

---

# 💡 What This Project Demonstrates

TubePlease Agent is more than a simple API project.

It demonstrates how multiple services can be connected behind a single intelligent interface.

### Concepts demonstrated

```text
Natural Language Processing
          +
Intent Detection
          +
API Design
          +
AI Integration
          +
External Service Integration
          +
Backend Architecture
          +
REST APIs
          +
Production Deployment
```

This makes the project a strong example of combining **AI + backend engineering + API integration** into one practical application.

---

# 👨‍💻 Author

<div align="center">

## Shaik Abdullah Azam

### B.Tech Artificial Intelligence Student

Building intelligent systems, AI applications and practical software projects.

<br>

<a href="https://github.com/Azam-star">
<img src="https://img.shields.io/badge/GitHub-Azam--star-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>

</div>

---

# ⭐ Support

If you find this project interesting:

⭐ Star the repository
🍴 Fork the project
🐛 Open an issue
💡 Suggest an improvement
🤝 Contribute to the project

---

<div align="center">

### Built with 🧠 AI + 🐍 Python + ⚡ Flask

<br>

**From a simple command to a real-world action.**

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff1744,50:45000f,100:020617&height=120&section=footer"/>

</div>
