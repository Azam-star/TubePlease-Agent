# Miuh AI 🎙️

**Miuh AI** is a voice-powered YouTube music assistant that lets you say a song name, searches YouTube, and displays the selected video directly inside the application.

## ✨ Features

* 🎙️ **Voice-controlled song search**
* 🔎 **Speech-to-text recognition**
* ▶️ **YouTube video search and playback**
* 🌑 **Modern black and red AI interface**
* 🔴 **Interactive glowing microphone**
* 📺 **YouTube player integrated into the UI**
* 📱 **Responsive design for different screen sizes**
* ⚡ **Flask backend with a simple frontend**

## 🧠 How It Works

```text
User speaks
     ↓
Browser Speech Recognition
     ↓
Song name extracted
     ↓
POST /youtube/play
     ↓
Flask backend
     ↓
YouTube search
     ↓
Video URL returned
     ↓
YouTube player displays the video
```

## 🛠️ Tech Stack

| Technology | Purpose                                  |
| ---------- | ---------------------------------------- |
| HTML5      | Frontend structure                       |
| CSS3       | UI, animations and styling               |
| JavaScript | Speech recognition and API communication |
| Python     | Backend logic                            |
| Flask      | Web framework                            |
| YouTube    | Music/video search and playback          |

## 📁 Project Structure

```text
Agent_ws2/
│
├── app/
│   ├── templates/
│   │   └── index.html
│   │
│   ├── youtube/
│   │   ├── __init__.py
│   │   └── player.py
│   │
│   └── __init__.py
│
├── requirements.txt
├── run.py
└── README.md
```

## 🚀 Run Locally

Clone the repository:

```bash
git clone https://github.com/Azam-star/Agent_ws2.git
cd Agent_ws2
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python run.py
```

Then open:

```text
http://127.0.0.1:5000
```

## 🎤 Example

Click the microphone and say:

```text
"Believer"
```

Miuh AI processes your voice, searches YouTube, and loads the matching video in the application.

## 🌐 Live Demo

**Live application:**
[https://agent-ws2.onrender.com](https://agent-ws2.onrender.com)

## 🎯 Project Goal

Miuh AI was created to demonstrate how **voice interaction, AI-style interfaces, Flask APIs, and YouTube search** can be combined into a simple music discovery experience.

## 👨‍💻 Author

**Mohammed Azam**

GitHub:
[https://github.com/Azam-star](https://github.com/Azam-star)

## ⭐ Support

If you find the project interesting, consider giving the repository a ⭐ on GitHub.
