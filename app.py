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

def sad():
    a = sorted(index().items(), key=lambda x: x[0])
    tokensholder = []
    for item in a:
        s = int(item[0])
        q = item[1]['balans']
        if s != 1:
            tokensholder.append((s, q))
    return tokensholder


@app.route('/')
def main():
    return render_template('index.html', users = len(sad()) - 1, koll = sad()[0][1] - 9607)

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/tokens')
def token():
    return render_template('tokens.html', posts = sad())

@app.route('/operations')
def operations():
    return render_template('operations.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/offer')
def offer():
    return render_template('offer.html')

@app.route('/entity')
def entity():
    return render_template('entity.html')

@app.route('/individual')
def individual():
    return render_template('individual.html')


@app.route('/individual', methods=['POST','GET'])
def sendMessageind():
    _1 = request.form['_1']
    _2 = request.form['_2']
    _3 = request.form['_3']
    _4 = request.form['_4']
    _5 = request.form['_5']
    _6 = request.form['_6']
    _7 = request.form['_7']
    _8 = request.form['_8']
    _9 = request.form['_9']
    _10 = request.form['_10']
    _11 = request.form['_11']
    text = """
Физическое лицо

Серия и номер паспорта РФ: %s
Кем выдан: %s
Когда выдан: %s
Код подразделения: %s
Адрес регистрации: %s
Адрес проживания: %s
Email: %s
Номер телефона 1: %s
Номер телефона 2: %s
Токены: %s
Сумма инвестирования: %s
    """ %(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10, _11)
    if _1 or _2 or _3 or _4 or _5 or _6 or _7 or _8 or _9 or _10 or _11:
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




@app.route('/entity', methods=['POST','GET'])
def sendMessageyr():
    _1 = request.form['_1']
    _2 = request.form['_2']
    _3 = request.form['_3']
    _4 = request.form['_4']
    _5 = request.form['_5']
    _6 = request.form['_6']
    _7 = request.form['_7']
    _8 = request.form['_8']
    _9 = request.form['_9']
    _10 = request.form['_10']
    _11 = request.form['_11']
    text = """
Юридическое лицо

Серия и номер паспорта РФ: %s
Кем выдан: %s
Когда выдан: %s
Код подразделения: %s
Адрес регистрации: %s
Адрес проживания: %s
Email: %s
Номер телефона 1: %s
Номер телефона 2: %s
Токены: %s
Сумма инвестирования: %s
    """ %(_1, _2, _3, _4, _5, _6, _7, _8, _9, _10, _11)
    if _1 or _2 or _3 or _4 or _5 or _6 or _7 or _8 or _9 or _10 or _11:
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



@app.route('/tokens', methods=['POST','GET'])
def sendMessagetkn():
    _name = request.form['name']
    _phone = request.form['phone']
    _comments = request.form['comments']
    _tokens = request.form['tokens']
    _email = request.form['email']
    text = """
    Имя: %s
Телефон: %s
Комментарий: %s
Количество токенов: %s
Email: %s
    """ % (_name, _phone, _comments, _tokens, _email)
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


@app.route('/', methods=['POST','GET'])
def sendMessage():
    _name = request.form['name']
    _phone = request.form['phone']
    _comments = request.form['comments']
    _tokens = request.form['tokens']
    _email = request.form['email']
    text = """
    Имя: %s
Телефон: %s
Комментарий: %s
Количество токенов: %s
Email: %s
    """ % (_name, _phone, _comments, _tokens, _email)
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



app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == "__main__":
    app.run(host='tokendl.com', port=80)
