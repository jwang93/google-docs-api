from google_spreadsheet.api import SpreadsheetAPI


GOOGLE_SPREADSHEET_USER = 'db.gdocs.test@gmail.com'
GOOGLE_SPREADSHEET_PASSWORD = 'drawbridge'
GOOGLE_SPREADSHEET_SOURCE = 'https://docs.google.com/spreadsheets/d/1qaqBQhChaKYrX6FNz9lBh77yrQyfbk-Vj9Ex6uyJ8Xs/edit#gid=0'

api = SpreadsheetAPI(GOOGLE_SPREADSHEET_USER, GOOGLE_SPREADSHEET_PASSWORD, GOOGLE_SPREADSHEET_SOURCE)
spreadsheets = api.list_spreadsheets()

print spreadsheets


worksheets = api.list_worksheets(spreadsheets[0][1])
print worksheets

sheet = api.get_worksheet('1qaqBQhChaKYrX6FNz9lBh77yrQyfbk-Vj9Ex6uyJ8Xs', 'od6')
rows = sheet.get_rows()
print len(rows)


for row in rows:
	print row


row_to_insert = {}
row_to_insert['record2'] = 'fldjfkljsfs'
row_to_insert['record1'] = 'assfdswewqe'
row = sheet.insert_row(row_to_insert)
