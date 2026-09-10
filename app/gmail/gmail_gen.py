import os
import json
import re
import time
import random
import urllib.request
import urllib.error

API_KEY = os.getenv("GEMINI_API_KEY","")
MODEL = os.getenv("GEMINI_MODEL","gemini-3.5-flash")

def generate_email_with_gemini(command):
  if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is missing.")

prompt = f"""
You are a proffessional Gmail email writing assistant.

  Convert the user's voicve command into a proffessional email.

  Rules:
  - Do not copy the command literally.
  - DO not explain anything.
  - Do not invent names, dates, prices, companies, attachments, oR facts.
  - Keep the email natural and concise.
  -Include an appropriate greeting and closing


  output exactly:

  SUBJECT : <subject>
  
