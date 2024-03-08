import tkinter as tk
from tkinter import messagebox
import requests

def get_weather_data(city):
    api_key = "aa55725dc8728c05fa248cbc0c8b7098"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        messagebox.showerror("Error", f"Error: {data['message']}")
        return None

def display_weather_info(city_name):
    weather_data = get_weather_data(city_name)

    if weather_data:
        info_str = (
            f"City: {weather_data['name']}\n"
            f"Temperature: {weather_data['main']['temp']}°C\n"
            f"Weather: {weather_data['weather'][0]['description']}\n"
            f"Humidity: {weather_data['main']['humidity']}%\n"
            f"Wind Speed: {weather_data['wind']['speed']} m/s"
        )
        messagebox.showinfo("Climate Information", info_str)
    else:
        messagebox.showwarning("Warning", "Unable to fetch weather data.")

def on_submit():
    city_name = entry.get()
    display_weather_info(city_name)

app = tk.Tk()
app.title("Weathering with You")

label = tk.Label(app, text="Enter a Country or City:")
entry = tk.Entry(app)
submit_button = tk.Button(app, text="Get Weather", command=on_submit)

label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
submit_button.grid(row=1, column=0, columnspan=2, pady=10)

app.mainloop()
