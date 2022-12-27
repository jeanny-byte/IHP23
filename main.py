import openpyxl
import requests

# Read the data from the Excel workbook
workbook = openpyxl.load_workbook('C:\\Users\\anyone\\Downloads\\updated names.xlsx')
sheet = workbook.active

# Read the values from the first row of the sheet
values = []
for cell in sheet[1]:
    values.append(cell.value)

# Define the message with placeholders for the values
message = "The values are: {value1}, {value2}, {value3}"

# Replace the placeholders with the actual values
formatted_message = message.format(value1=values[1], value2=values[2], value3=values[3])
receipt_address = values[0]

# Send the message using the MNOTIFY API
url = "https://apps.mnotify.net/smsapi?"
payload = {
    "key": "pX88BJbnvGDH5PlAuVi70IuFE",
    "to": receipt_address,
    "msg": formatted_message,
    "sender_id": "IHP23"
}
response = requests.post(url, data=payload)
stcode = response.status_code
print(response.status_code)

if stcode == 1000:
    print('message to {value0} {value1} {value2} was successful')
elif stcode == 1002:
    print('message to {value0} {value1} {value2} was failed')
elif stcode == 1003:
    print('message to {value0} {value1} {value2} was not successful, Insufficient balance')
elif stcode == 1004:
    print('Invalid API Key')
elif stcode == 1005:
    print('Invalid Phone Number')
elif stcode == 1006:
    print('Invalid Sender ID')
elif stcode == 1007:
    print('Message scheduled for later delivery')
elif stcode == 1008:
    print('empty message')
elif stcode == 1009:
    print(' Empty from date and to date')
elif stcode == 1010:
    print('No mesages has been sent on the specified dates using the specified api key')
elif stcode == 1011:
    print('Numeric Sender IDs are not allowed')
elif stcode == 1012:
    print(' Sender ID is not registered. Please contact our support team via senderids@mnotify.com or call 0541509394 for assistance')

def CheckBalance():
    url = 'https://apps.mnotify.net/smsapi/balance?key=pX88BJbnvGDH5PlAuVi70IuFE'
    Balanceresponse = requests.post(url)
    print(Balanceresponse)
