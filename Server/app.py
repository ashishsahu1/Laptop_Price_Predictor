from flask import Flask
from test import predict_price
from flask import render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template('index.html')

@app.route("/specs", methods=['POST'])
def laptop_specs():
    if request.method == 'POST':
        brand = request.form['brand']
        ltype = request.form['ltype']
        lram = int(request.form['lram'])
        lwt = float(request.form['lwt'])
        ltouch_screen = request.form['ltouch_screen']
        ips = request.form['ips']
        lsize = float(request.form['lsize'])
        lresolution = request.form['lresolution']
        cpu = request.form['cpu']
        hdd = int(request.form['hdd'])
        ssd = int(request.form['ssd'])
        gpu = request.form['gpu']
        os = request.form['os']
        
        predicted_price = predict_price(brand, ltype, lram, lwt, ltouch_screen, ips, lsize, lresolution, cpu, hdd, ssd, gpu, os)
        return {
            "Laptop_predicted_price": predicted_price
        }

if __name__ == "__main__":
    app.run(debug=True)