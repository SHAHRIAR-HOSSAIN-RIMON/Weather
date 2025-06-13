

---

# 🌦️ Weather Detector

A simple Django-based web application that allows users to search for current weather conditions in any city using the OpenWeatherMap API.

---

## 🚀 Features

* 🌍 Search weather by **city name**
* 📍 Displays:

  * Country code
  * Coordinates (Longitude, Latitude)
  * Temperature (°C)
  * Atmospheric pressure
  * Humidity
* ❌ Error message shown in red if the city name is invalid

---

## 🛠️ Built With

* Python
* Django
* HTML & CSS
* OpenWeatherMap API

---

## 📦 Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/SHAHRIAR-HOSSAIN-RIMON/Weather.git
   cd Weather
   ```

2. **Install dependencies**

   ```bash
   pip install django
   ```

3. **Set your OpenWeatherMap API key**
   Open `views.py` and replace the placeholder API key with your actual one:

   ```python
   'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=YOUR_API_KEY'
   ```

4. **Run the development server**

   ```bash
   python manage.py runserver
   ```

5. **Open in your browser**
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ⚠️ Error Handling

If an invalid city name is entered, the app displays:

> **City doesn't exist. Please enter a valid city name.**

---





## 📸 Screenshots

<!-- Replace these URLs with your new image URLs -->
![weather3](https://github.com/user-attachments/assets/04c703fe-c8b4-4be8-8348-b792b3acc496)
![weather4](https://github.com/user-attachments/assets/95430660-89ee-46df-8cd0-7ff57df6fece)


![weather5](https://github.com/user-attachments/assets/c03c4767-1477-4612-83c9-599d57c61bfe)


---
## 🎯 Project Motivation

* Practice Django fundamentals
* Work with real-world APIs
* Build a useful weather app project

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to improve.

---




---



