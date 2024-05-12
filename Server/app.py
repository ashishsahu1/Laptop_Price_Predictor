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
        brand = request.form.get('brand')
        ltype = request.form.get('ltype')
        lram = int(request.form.get('lram'))
        lwt = float(request.form.get('lwt'))
        ltouch_screen = request.form.get('ltouch_screen')
        ips = request.form.get('ips')
        lsize = float(request.form.get('lsize'))
        lresolution = request.form.get('lresolution')
        cpu = request.form.get('cpu')
        hdd = int(request.form.get('hdd'))
        ssd = int(request.form.get('ssd'))
        gpu = request.form.get('gpu')
        os = request.form.get('os')
        
        predicted_price = predict_price(brand, ltype, lram, lwt, ltouch_screen, ips, lsize, lresolution, cpu, hdd, ssd, gpu, os)
        print("predicted_price", predicted_price)
        return {
            "Laptop_predicted_price": predicted_price
        }

if __name__ == "__main__":
    app.run(debug=True)