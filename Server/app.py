from flask import Flask, render_template, url_for, request, redirect
from test import predict_price

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
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
        isDone = True
        print("predicted_price", predicted_price)
        print("Inside Post")
        return render_template('index.html', predicted_price = predicted_price, isDone = isDone)
    
    else:
        print("Inside Get")
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)