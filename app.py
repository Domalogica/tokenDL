#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from werkzeug.contrib.fixers import ProxyFix
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

def index():
    response = requests.get('http://dl.kaspsoft.com/?r=api/get-balans&authCod=lkfghfghljIFyDOP')
    response = json.loads(response.content.decode("utf-8"))
    return response

a = sorted(index().items(), key=lambda x: x[0])

tokensholder = {}

for item in a:
    print(type(item[0]))
    print(type(item))
    # tokensholder[item[0]].update({item[1]})

print(tokensholder)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/tokens')
def token():
    return render_template('tokens.html', posts = index())

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
    _email = request.form['email']
    text = """
    Имя: %s
Телефон: %s
Комментарий: %s
Email: %s
    """ % (_name, _phone, _comments, _email)
    print(text)
    if _name or _phone or _comments:
        url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=167315364&text=%s" % (text)
        requests.post(url)   
        url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=70025022&text=%s" % (text)
        requests.post(url)   
        url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=65472004&text=%s" % (text)
        requests.post(url)   
        url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=-303230127&text=%s" % (text)
        requests.post(url)   
        url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=34436430&text=%s" % (text)
        requests.post(url)   
        url = "https://api.telegram.org/bot527562365:AAFDyCml1bgH7D5mvng6KcxKI-dTvAN6Ybc/sendMessage?chat_id=27390261&text=%s" % (text)
        requests.post(url) 
    return render_template('ok.html')
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



app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    app.run(host='tokendl.com', port=80)
