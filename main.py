


import math
import requests
from OpMySql import OpMySql


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

counter=17

#126227
total=0
for x in range(counter):
    mysql = OpMySql()

    url = 'https://api.ehkaam.sa/api/app/adsAppServices/adsList?skipCount='+str(total)+'&maxResultCount=1000'
    total = total + 1000
    resp = requests.get(url=url)
    json = resp.json()

    for y in json["items"] :



        #https://api.ehkaam.sa/api/app/realEstateOwnershipRequest/downloadArealReportAttachment/77960






        if len(mysql.get_row("ehkaam_main", ["requestId"], [y["requestId"]])) == 0:
            print(str(total) + ">>" + str(y["requestId"]))
            arr_main_name = ['requestId', 'area', 'realEstateType', 'cityName', 'regionName', 'publishingDate',
                             'adsEndDate', 'remainingTime', 'remainingDays', 'latitude', 'longitude', 'ownerName']
            arr_main_value = [y["requestId"], y["area"], y["realEstateType"], y["cityName"], y["regionName"],
                              y["publishingDate"], y["adsEndDate"], y["remainingTime"], y["remainingDays"],
                              y["latitude"], y["longitude"], y["ownerName"]]
            Id_main = mysql.add_row_single("ehkaam_main", arr_main_name, arr_main_value)




print(counter)
