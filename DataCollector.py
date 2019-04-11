import fitbit
import gather_keys_oauth2 as Oauth2
import pandas as pd
import datetime
import numpy as np

CLIENT_ID = '22DDTT'
CLIENT_SECRET = 'd24e5f9ed8ff9d39a506b006c2e5ce85'

server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d"))
date_list = []
val_list = []

for delta in reversed(range(1, 31)):
    yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=delta)).strftime("%Y-%m-%d"))
    today = str(datetime.datetime.now().strftime("%Y%m%d"))

    fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=yesterday2, detail_level='1sec')
    print(fit_statsHR)

    for i in fit_statsHR['activities-heart']:
        try:
            val_list.append(i['value']['restingHeartRate'])
        except KeyError:
            val_list.append(np.nan)
        date_list.append(i['dateTime'])


df = pd.DataFrame({'Heart Rate': val_list, 'Date': date_list})

print(df)

fit_statsSl = auth2_client.sleep(date='2018-12-14')
print(fit_statsSl)
stime_list = []
sval_list = []
for i in fit_statsSl['sleep']:
    stime_list.append(i['dateTime'])
    sval_list.append(i['value'])
sleepdf = pd.DataFrame({'State':sval_list,
                     'Time':stime_list})
sleepdf['Interpreted'] = sleepdf['State'].map({'2':'Awake','3':'Very Awake','1':'Asleep'})

print(sleepdf)
