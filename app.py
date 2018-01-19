#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import requests, os
mysql = MySQL()
app = Flask(__name__)
app._static_folder = os.path.abspath("static/")
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '7087'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/tokens')
def token():
    return render_template('tokens.html')

@app.route('/operations')
def operations():
    return render_template('operations.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/', methods=['POST','GET'])
def sendMessage():
    _name = request.form['name']
    _phone = request.form['phone']
    _comments = request.form['comments']
    text = """
    Имя: %s
Телефон: %s
Комментарий: %s
    """ % (_name, _phone, _comments)
    if _name or _phone or _comments:
        url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=167315364&text=%s" % (text)
        requests.post(url)   
        url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=70025022&text=%s" % (text)
        requests.post(url)   
        url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=65472004&text=%s" % (text)
        requests.post(url)   
        url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=-263564659&text=%s" % (text)
        requests.post(url)   
    return render_template('index.html')
    # conn = mysql.connect()
    # cursor = conn.cursor()
    # try:
    #     _name = request.form['inputName']
    #     _email = request.form['inputEmail']
    #     _password = request.form['inputPassword']

    #     # validate the received values
    #     if _name and _email and _password:
            
    #         # All Good, let's call MySQL
            
    #         _hashed_password = generate_password_hash(_password)
    #         cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
    #         data = cursor.fetchall()

    #         if len(data) is 0:
    #             conn.commit()
    #             return json.dumps({'message':'User created successfully !'})
    #         else:
    #             return json.dumps({'error':str(data[0])})
    #     else:
    #         return json.dumps({'html':'<span>Enter the required fields</span>'})

    # except Exception as e:
    #     return json.dumps({'error':str(e)})
    # finally:
    #     cursor.close() 
    #     conn.close()




if __name__ == "__main__":
    app.run(host='http://tokendl.com', port=80)
