from flask import Flask
from test import predict_price
from flask import render_template, request

app = Flask(__name__)

company = "Asus"
laptop_type = "Notebook"
ram = 8
weight = 1.86
touchscreen = "Yes"
ips = "Yes"
screen_size = 15.6
resolution = "1920x1080"
cpu = "Intel Core i5"
hdd = 1000
ssd = 256
gpu = "Intel"
os = "Windows"

@app.route("/")
def index_page():
    return render_template('index.html')

@app.route("/specs", methods=['POST'])
def laptop_specs():
    if request.method == 'POST':
        brand = request.form['brand']
        ltype = request.form['ltype']
        lram = request.form['lram']
        lwt = request.form['lwt']
        ldisplay = request.form['ldisplay']
        lscreen = request.form['lscreen']
        lsize = request.form['lsize']
        lresolution = request.form['lresolution']
        cpu = request.form['cpu']
        hdd = request.form['hdd']
        ssd = request.form['ssd']
        gpu = request.form['gpu']
        os = request.form['os']
        
        predicted_price = predict_price(company, laptop_type, ram, weight, touchscreen, ips, screen_size, resolution, cpu, hdd, ssd, gpu, os)
        return {
            "Laptop_predicted_price": predicted_price
        }

if __name__ == "__main__":
    app.run(debug=True)