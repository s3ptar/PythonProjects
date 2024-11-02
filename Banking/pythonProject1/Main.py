import json
import os
import datetime
from datetime import timedelta
import time
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from datetime import datetime
import csv
import influxdb_client
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import pandas as pd
"""*********************************************************************
*! \fn          main
*  \brief       start code
*  \param       none
*  \exception   none
*  \return      none
*********************************************************************"""

"""*********************************************************************
                Constant
*********************************************************************"""

bl_data_section_activ = 0
"""*********************************************************************
                mantis
*********************************************************************"""


"""*********************************************************************
*! \fn          read_csv(file_path)
*  \brief       read csv content
*  \param       file_path - file to csv
*  \exception   none
*  \return      none
*********************************************************************"""
def read_csv(file_path):

    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if bl_data_section_activ:
                    print(row[0])
                    timestamp = datetime.strptime(row[0], '%d.%m.%y')
                    print(timestamp)
                    print(timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"))
                if (bl_data_section_activ == 0) & (row[0] == 'Buchungsdatum'):
                    bl_data_section_activ = 1
                if bl_data_section_activ:
                    print(row)
    except FileNotFoundError:
        print("Oops! It seems the file doesn't exist. Double-check the file path.")


__name__ == '__main__'

print("lets start")

# pick file
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

#read config file
with open("config.json", 'r') as config_file:
    json_content = json.load(config_file)
print(json_content['url'])
write_client = influxdb_client.InfluxDBClient(url=json_content['url'], token=json_content['token'],
                                              org=json_content['org'], debug=True)
write_api = write_client.write_api(write_options=SYNCHRONOUS)


#read file

with (open(filename, mode='r') as file):
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if bl_data_section_activ:
            #print(row[0])
            timestamp = datetime.strptime(row[0], '%d.%m.%y')
            print(timestamp)
            epoch_time = int(timestamp.timestamp())
            print(epoch_time)
            print(time.time())
            #print(timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"))
            point = (
                Point("financial")
                .tag("Buchungszeit", timestamp)
                #.time(epoch_time*1000)
                .tag("Verwendungszweck", row[5])
                .tag("Zahlungspflichtiger", row[3])
                .tag("Zahlungsempfänger", row[4])
                .tag("Umsatztyp", row[6])
                .field("Betrag", float((row[8].replace(".","")).replace(",",".")))
            )
                #.time(timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"))
                #.tag("Zahlungspflichtiger", row[4])
                #.tag("Zahlungsempfänger", row[5])

            write_api.write(bucket=json_content['bucket'], record=point, time_precision='ms')
            time.sleep(1)  # separate points by 1 second
        if (bl_data_section_activ == 0) & (row[0] == 'Buchungsdatum'):
            bl_data_section_activ = 1
        if bl_data_section_activ:
            print(row)



