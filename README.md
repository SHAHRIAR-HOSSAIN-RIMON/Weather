# Weather


````markdown
# 🌦️ Weather Detector

A simple Django-based web application that lets users search for the current weather in any city using the OpenWeatherMap API.

---

## 🚀 Features

- 🌍 Search weather by **city name**
- 📍 Displays:
  - Country code
  - Coordinates (Longitude, Latitude)
  - Temperature (°C)
  - Atmospheric pressure
  - Humidity
- ❌ Shows a clear red error message for invalid city input

---

## 🛠️ Built With

- Python  
- Django (Backend Framework)  
- HTML & CSS  
- OpenWeatherMap API  

---

## 📦 Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/SHAHRIAR-HOSSAIN-RIMON/Weather.git
cd Weather
````

2. **Install dependencies**

```bash
pip install django
```

3. **Set your OpenWeatherMap API key**

In `views.py`, replace `YOUR_API_KEY` with your actual API key:

```python
'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=5be464c2e0141838a8ec254ffbb4608f'
```

4. **Run the development server**

```bash
python manage.py runserver
```

5. **Open the app in your browser**

```
http://127.0.0.1:8000/
```

---

## ⚠️ Error Handling

If the city name entered is invalid, the app displays:

> **City doesn't exist. Please enter a valid city name.**

---

## 🎯 Project Motivation

This project was created to:

* Practice using Django framework
* Work with real-world REST APIs
* Build a practical weather app

---

## 📸 Screenshots

<!-- Replace these URLs with your new image URLs -->
![weather3](https://github.com/user-attachments/assets/04c703fe-c8b4-4be8-8348-b792b3acc496)
![weather4](https://github.com/user-attachments/assets/95430660-89ee-46df-8cd0-7ff57df6fece)


![weather5](https://github.com/user-attachments/assets/c03c4767-1477-4612-83c9-599d57c61bfe)


---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you want to improve.

---



