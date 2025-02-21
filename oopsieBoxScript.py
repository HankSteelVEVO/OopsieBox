##importing required libraries
import serial
import time
import asyncio
from desktop_notifier import DesktopNotifier
import gspread
from oauth2client.service_account import ServiceAccountCredentials

##Set-up for serial communication
port = 'COM8'
baud_rate = 9600
arduino = serial.Serial(port, baud_rate, timeout=1)

notifier = DesktopNotifier()

##Set up for Google Sheets API and Google Sheet
scope = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/drive.file"
]
clientKey = 'client_key.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(clientKey, scope)
client = gspread.authorize(credentials)
sheet = client.open('Oopsie Counter').sheet1


while True:
    data = arduino.readline().decode().strip()
    ##Formatting data for multiple inputs
    
    if data:  ##if the computer receives input from the Arduino
        edit = 0
        data = int(data)
        if data > 100: ##negation button is held, decrement
            edit = -1
            data = (data - 255) * -1
        else:  ##negation button not held, increment
            edit = 1
        
        print("Pin number: " + str(data))
        cellData = int(sheet.cell(data,2).value)
        print("Before: " + str(cellData))
        sheet.update_cell(data, 2, cellData + edit)
        newCellData = sheet.cell(data, 2).value
        name = sheet.cell(data, 1).value
        print("After: " + newCellData)
        async def message():
            if (int(newCellData) - int(cellData)) != int(edit):
                await notifier.send(title="Alex's Oopsie Box", message="ERROR: Value not updated correctly.")
            elif edit == 1:
                await notifier.send(title="Alex's Oopsie Box", message=name + " said an oopsie!\nCurrent count: " + str(newCellData))
            elif edit == -1:
                await notifier.send(title="Alex's Oopsie Box", message="My bad, my bad. Drop the count for " + name + " by one.\nCurrent count: " + str(newCellData))
        asyncio.run(message())
