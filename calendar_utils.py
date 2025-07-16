# code for integrating with Google Calendar API 
# calendar_utils.py

import datetime
import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scope: read-only calendar
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_available_slots(duration_minutes=60, day='Tuesday', time_pref='afternoon'):
    """Returns dummy available time slots on a given day."""
    try:
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        service = build('calendar', 'v3', credentials=creds)

        # Get current week’s day range
        now = datetime.datetime.utcnow()
        weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        target_weekday_index = weekday.index(day)
        today_weekday_index = now.weekday()

        days_until_target = (target_weekday_index - today_weekday_index) % 7
        target_date = now + datetime.timedelta(days=days_until_target)

        # Example: look for slots between 12 PM and 6 PM
        if time_pref == 'afternoon':
            start_hour = 12
            end_hour = 18
        elif time_pref == 'morning':
            start_hour = 8
            end_hour = 12
        else:
            start_hour = 9
            end_hour = 17

        # Define the window
        start_time = datetime.datetime.combine(target_date.date(), datetime.time(start_hour, 0)).isoformat() + 'Z'
        end_time = datetime.datetime.combine(target_date.date(), datetime.time(end_hour, 0)).isoformat() + 'Z'

        # Query calendar
        events_result = service.events().list(
            calendarId='primary',
            timeMin=start_time,
            timeMax=end_time,
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])

        # For demo, we assume these slots exist
        available = ['12:00 PM', '3:30 PM', '5:00 PM']
        return available

    except Exception as e:
        print(f"Calendar error: {str(e)}")
        return []

