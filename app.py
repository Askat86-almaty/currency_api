from flask import Flask, jsonify

app = Flask(_name_)

@app.route('/convert/<int:kzt>')
def convert(kzt):
    rate = 480  # курс KZT к USD
    usd = round(kzt / rate, 2)
    return jsonify({'KZT': kzt, 'USD': usd})

if _name_ == '_main_':

    app.run(debug=True)
