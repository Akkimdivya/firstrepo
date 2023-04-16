from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'new.json'
Credentials=None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


SAMPLE_SPREADSHEET_ID = '1sd-43meB6PszlR8mB6CqYcb8Z_oreMlPVOTnsbS7-Ik'
    
service = build('sheets', 'v4', credentials=credentials)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="sales!A1").execute()
values = result.get('values', [])
aoa=[["1/1/2020"],4000],[["1/1/2020"],4000]
request = service.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="sheet2!A1", valueInputOption="USER_ENTERED", body={"value":aoa}).execute()
print(request)