# code for integrating with Google Calendar API 

# calendar_utils.py

from __future__ import print_function
import os.path
import datetime
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# If modifying these SCOPES, delete token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_available_slots(duration_minutes=60, day='Tuesday', time_pref='afternoon'):
    """Returns a list of free time slots based on Google Calendar events."""

    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow()
    start_of_day = now.replace(hour=12, minute=0, second=0) if time_pref == 'afternoon' else now.replace(hour=9, minute=0, second=0)
    end_of_day = now.replace(hour=18, minute=0, second=0)

    events_result = service.events().list(
        calendarId='primary', timeMin=start_of_day.isoformat() + 'Z',
        timeMax=end_of_day.isoformat() + 'Z', singleEvents=True,
        orderBy='startTime').execute()
    
    events = events_result.get('items', [])

    free_slots = []
    current = start_of_day
    for event in events:
        start = datetime.datetime.fromisoformat(event['start']['dateTime'].replace('Z', '+00:00'))
        if (start - current).total_seconds() >= duration_minutes * 60:
            free_slots.append(current.strftime('%I:%M %p'))
        end = datetime.datetime.fromisoformat(event['end']['dateTime'].replace('Z', '+00:00'))
        current = max(current, end)

    if (end_of_day - current).total_seconds() >= duration_minutes * 60:
        free_slots.append(current.strftime('%I:%M %p'))

    return free_slots or ["No available slots"]
