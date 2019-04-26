from flask import Flask, jsonify, request
import queries
import datetime
from flask_mail import Mail, Message
from random import randint
import fitbit
import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='nerdherd.smartheart@gmail.com',
    MAIL_PASSWORD='NerdHerd1!'
)
mail = Mail(app)

CLIENT_ID = '22DDTT'
CLIENT_SECRET = 'd24e5f9ed8ff9d39a506b006c2e5ce85'


schema_list = [u'email', u'password', u'cigsda1_cigs_per_day_', u'aheight', u'aweightp', u'sex_1_Male', u'sex_2_Female',
               u'hispan_i_12_Not_Hispanic_Spanish_origin', u'racerpi2_01_White_only', u'racerpi2_02_Black_African_American_only', u'racerpi2_03_AIAN_only', u'racerpi2_04_Asian_only', u'racerpi2_06_Multiple_race',
               u'age_p_85_85__years', u'hypev_hypertension__1_Yes', u'hypev_hypertension__2_No', u'hypyr_hyper_for_a_year__1_Yes', u'hypyr_hyper_for_a_year__2_No',
               u'alctobyr_alcohol__1_Yes', u'alctobyr_alcohol__2_No', u'aovrwtyr_overweight__1_Yes', u'aovrwtyr_overweight__2_No',
               u'anxnwyr_anxiety__1_Yes', u'anxnwyr_anxiety__2_No', u'astresyr_stress__1_Yes', u'astresyr_stress__2_No',
               u'dibev_diabetes__1_Yes', u'dibev_diabetes__2_No', u'dibev_diabetes__3_Borderline', u'pregnow_1_Yes', u'pregnow_2_No',
               u'sad_1_ALL_of_the_time', u'sad_2_MOST_of_the_time', u'sad_3_SOME_of_the_time', u'sad_4_A_LITTLE_of_the_time',
               u'sad_5_NONE_of_the_time', u'nervous_1_ALL_of_the_time', u'nervous_2_MOST_of_the_time', u'nervous_3_SOME_of_the_time',
               u'nervous_4_A_LITTLE_of_the_time', u'nervous_5_NONE_of_the_time', u'restless_1_ALL_of_the_time', u'restless_2_MOST_of_the_time',
               u'restless_3_SOME_of_the_time', u'restless_4_A_LITTLE_of_the_time', u'restless_5_NONE_of_the_time', u'smknow_smoking_frequency__1_Every_day',
               u'smknow_smoking_frequency__2_Some_days', u'smknow_smoking_frequency__3_Not_at_all', u'modtp_light_activity__0_Never',
               u'modtp_light_activity__1_Per_day', u'modtp_light_activity__2_Per_week', u'modtp_light_activity__3_Per_month', u'modtp_light_activity__4_Per_year',
               u'modtp_light_activity__6_Unable_to_do_this_activity', u'alc5uptp_5__Drinks_Days_Time_Unit__0_Never_None',
               u'alc5uptp_5__Drinks_Days_Time_Unit__1_Per_week', u'alc5uptp_5__Drinks_Days_Time_Unit__2_Per_month', u'alc5uptp_5__Drinks_Days_Time_Unit__3_Per_year',
               u'cnkind28_thyroid_cancer__1_Mentioned', u'cnkind10_kidney_cancer__1_Mentioned', u'rhr', u'account_creation_date_time']


@app.route("/login", methods=["GET", "POST"])
def login():
    existing_user = request.get_json(force=True)  # ignore mimetype
    df = queries.client.query("""
    SELECT email, password FROM usr_data.usr_data_tbl
    """).to_dataframe()
    print(df.head())
    print(list(existing_user[u'email']))
    row = df[df[u'email'].str.match(str(existing_user[u'email']))]
    if str(row.iloc[0][u'password']) == str(existing_user[u'password']):
        return jsonify(valid=True)
    return jsonify(valid=False)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    new_user_json = request.get_json(force=True)  # ignore mimetype
    print(new_user_json)
    print(list(new_user_json.keys()))
    new_user_json[u'account_creation_date_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rows = [new_user_json]
    table = queries.client.get_table("nerdherd.usr_data.usr_data_tbl")
    queries.client.insert_rows_json(table, rows)
    return jsonify(new_user_json), 200


@app.route("/predict", methods=["GET", "POST"])
def hypertension_checker():
    json_dict = request.get_json(force=True)  # ignore mimetype
    values = []
    for col in schema_list:
        values.append(json_dict[col])
    print(values)
    values.pop(14)  # pop off prediction field
    values.pop(0)   # pop off email
    values.pop(0)   # pop off password
    values.pop()    # pop off account creation date
    print(values)
    y_pred = queries.run_lgr(queries.df, values)
    json_dict[u'hypev_hypertension__1_Yes'] = y_pred
    print(json_dict[u'hypev_hypertension__1_Yes'])
    json_dict[u'account_creation_date_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rows = [json_dict]
    table = queries.client.get_table("nerdherd.usr_data.usr_data_tbl")
    queries.client.insert_rows_json(table, rows)
    return jsonify(json_dict)


@app.route("/update", methods=["GET", "POST"])
def update_profile():
    existing_user = request.get_json(force=True)
    existing_user[u'account_creation_date_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rows = [existing_user]
    table = queries.client.get_table("nerdherd.usr_data.usr_data_tbl")
    queries.client.insert_rows_json(table, rows)
    return jsonify(existing_user)


@app.route("/sendcode", methods=["GET", "POST"])
def send_email():
    email = request.get_json(force=True)[u'email']
    print(str(email))
    code = randint(1000, 9999)
    body = 'Here is your verification code: ' + str(code)
    msg = Message("SmartHeart Verification Code", body=body, sender='nerdherd.smartheart@gmail.com', recipients=[str(email)])
    mail.send(msg)
    return jsonify(code=code)


@app.route("/fitbit", methods=["GET", "POST"])
def fitbit_data():
    tokens = request.get_json(force=True)
    access_token = str(tokens[u'access_token'])
    refresh_token = str(tokens[u'refresh_token'])
    auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=access_token,
                                 refresh_token=refresh_token)

    date_list = []
    val_list = []

    for delta in reversed(range(1, 31)):
        yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=delta)).strftime("%Y-%m-%d"))

        fit_statsHR = auth2_client.intraday_time_series('activities/heart', base_date=yesterday2, detail_level='1sec')

        for i in fit_statsHR['activities-heart']:
            try:
                val_list.append(i['value']['restingHeartRate'])
            except KeyError:
                val_list.append(np.nan)
            date_list.append(i['dateTime'])

    df = pd.DataFrame({'Heart Rate': val_list, 'Date': date_list})
    df = df.astype(object).where(pd.notnull(df), None)
    print(df.head())
    return jsonify(df.to_json(orient='records'))


if __name__ == "__main__":
    app.run(debug=True)

