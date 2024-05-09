import pickle
import numpy as np
import sys

# Load the model and dataframe
pipe = pickle.load(open('../Artifact/pipe.pkl', 'rb'))
df = pickle.load(open('../Artifact/df.pkl', 'rb'))

def predict_price(company, laptop_type, ram, weight, touchscreen, ips, screen_size, resolution, cpu, hdd, ssd, gpu, os):
    # Process inputs
    if touchscreen.lower() == 'yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips.lower() == 'yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size
    query = np.array([company, laptop_type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

    query = query.reshape(1, 12)
    # Predict price
    predicted_price = int(np.exp(pipe.predict(query)[0]))
    return predicted_price

if __name__ == "__main__":
    print("Please provide the following information:")
    company = input("Brand: ")
    laptop_type = input("Type: ")
    ram = int(input("RAM (in GB): "))
    weight = float(input("Weight: "))
    touchscreen = input("Touchscreen (Yes/No): ")
    ips = input("IPS (Yes/No): ")
    screen_size = float(input("Screen Size: "))
    resolution = input("Screen Resolution (e.g., 1920x1080): ")
    cpu = input("CPU: ")
    hdd = int(input("HDD (in GB): "))
    ssd = int(input("SSD (in GB): "))
    gpu = input("GPU: ")
    os = input("OS: ")

    predicted_price = predict_price(company, laptop_type, ram, weight, touchscreen, ips, screen_size, resolution, cpu, hdd, ssd, gpu, os)
    print("The predicted price of this configuration is:", predicted_price)
