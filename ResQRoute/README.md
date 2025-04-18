
# 🚨 ResQRoute – Intelligent Emergency Response System

ResQRoute is a real-time emergency response coordination platform that connects emergency vehicles, control rooms, and citizens. It aims to streamline the movement of emergency services by integrating smart routing, live signal mapping, and real-time notifications.

---

## 🔧 Features

### 👨‍💻 Citizen App
- Raise emergency requests (Medical, Fire, Accident, Crime, Rescue)
- Auto-detects current location via browser
- Notifies nearby emergency vehicles in real time
- Real-time status tracking of requests

### 🚑 Driver Dashboard
- View assigned emergency tasks
- See live emergency route map with signal points
- Receive navigation instructions to pickup/drop locations
- Update task status (en route, arrived, completed)

### 🧠 Control Room Dashboard
- Assign nearest vehicle based on location and availability
- Override traffic signals for emergency vehicle movement
- Live analytics on request types, average response time, and vehicle statuses

---

## 🗃️ Tech Stack

- **Frontend**: Streamlit (for Citizen App & Dashboards)
- **Backend**: Python
- **Database**: MySQL
- **Mapping**: Folium / Leaflet (Live Route & Signal Map)
- **Charting**: Plotly, Streamlit charts

---

## 🏗️ Project Structure

ResQRoute/
│
├── backend/
│   ├── database.py               # MySQL connection and query handlers
│   ├── emergency_utils.py        # Emergency finder and ETA logic
│   └── signal_control.py         # Smart signal override logic
│
├── citizen_app/
│   └── app.py                    # Citizen web interface
│
├── driver_dashboard/
│   └── app.py                    # Emergency vehicle dashboard
│
├── admin_dashboard/
│   └── app.py                    # Admin analytics dashboard
│
├── assets/                       # Custom icons, images, logos
│
├── data/                         # Sample CSVs if any fallback data is needed
│
├── requirements.txt              # All dependencies
└── README.md                     # You're here :)

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ResQRoute.git
cd ResQRoute
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure MySQL Database

Open `backend/database.py` and update the credentials:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'database': 'resqroute_db'
}
```

Then Create the following Tables:

+---------------------+
| Tables_in_resqroute |
+---------------------+
| citizens            |
| drivers             |
| emergencies         |
| signal_logs         |
| signals             |
| tasks               |
| vehicles            |
+---------------------+

1)citizens

+--------------+--------------+------+-----+-------------------+-------------------+
| Field        | Type         | Null | Key | Default           | Extra             |
+--------------+--------------+------+-----+-------------------+-------------------+
| id           | int          | NO   | PRI | NULL              | auto_increment    |
| name         | varchar(255) | NO   |     | NULL              |                   |
| phone        | varchar(15)  | YES  |     | NULL              |                   |
| location_lat | double       | YES  |     | NULL              |                   |
| location_lon | double       | YES  |     | NULL              |                   |
| timestamp    | timestamp    | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+--------------+--------------+------+-----+-------------------+-------------------+

2)drivers

+------------+--------------+------+-----+---------+----------------+
| Field      | Type         | Null | Key | Default | Extra          |
+------------+--------------+------+-----+---------+----------------+
| id         | int          | NO   | PRI | NULL    | auto_increment |
| name       | varchar(255) | NO   |     | NULL    |                |
| vehicle_id | int          | YES  | MUL | NULL    |                |
+------------+--------------+------+-----+---------+----------------+

3)emergencies

+-------------------+-------------+------+-----+-------------------+-------------------+
| Field             | Type        | Null | Key | Default           | Extra             |
+-------------------+-------------+------+-----+-------------------+-------------------+
| id                | int         | NO   | PRI | NULL              | auto_increment    |
| citizen_id        | int         | YES  | MUL | NULL              |                   |
| emergency_type    | varchar(50) | YES  |     | NULL              |                   |
| requested_vehicle | varchar(50) | YES  |     | NULL              |                   |
| location_lat      | double      | YES  |     | NULL              |                   |
| location_lon      | double      | YES  |     | NULL              |                   |
| timestamp         | timestamp   | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| status            | varchar(50) | YES  |     | Pending           |                   |
+-------------------+-------------+------+-----+-------------------+-------------------+

4)signal_logs

+---------------+--------------+------+-----+-------------------+-------------------+
| Field         | Type         | Null | Key | Default           | Extra             |
+---------------+--------------+------+-----+-------------------+-------------------+
| id            | int          | NO   | PRI | NULL              | auto_increment    |
| signal_id     | int          | YES  | MUL | NULL              |                   |
| override_time | timestamp    | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| new_state     | varchar(10)  | YES  |     | NULL              |                   |
| overridden_by | varchar(100) | YES  |     | NULL              |                   |
+---------------+--------------+------+-----+-------------------+-------------------+

5)signals

+-----------------+-------------+------+-----+---------+----------------+
| Field           | Type        | Null | Key | Default | Extra          |
+-----------------+-------------+------+-----+---------+----------------+
| id              | int         | NO   | PRI | NULL    | auto_increment |
| signal_code     | varchar(50) | NO   |     | NULL    |                |
| location_lat    | double      | YES  |     | NULL    |                |
| location_lon    | double      | YES  |     | NULL    |                |
| current_state   | varchar(10) | YES  |     | RED     |                |
| green_duration  | int         | YES  |     | 60      |                |
| yellow_duration | int         | YES  |     | 5       |                |
| red_duration    | int         | YES  |     | 55      |                |
| last_override   | timestamp   | YES  |     | NULL    |                |
+-----------------+-------------+------+-----+---------+----------------+

6)tasks

+--------------+-------------+------+-----+-------------------+-------------------+
| Field        | Type        | Null | Key | Default           | Extra             |
+--------------+-------------+------+-----+-------------------+-------------------+
| id           | int         | NO   | PRI | NULL              | auto_increment    |
| emergency_id | int         | YES  | MUL | NULL              |                   |
| driver_id    | int         | YES  | MUL | NULL              |                   |
| assigned_at  | timestamp   | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| status       | varchar(50) | YES  |     | Assigned          |                   |
+--------------+-------------+------+-----+-------------------+-------------------+

7)vehicles

+--------------+-------------+------+-----+-----------+----------------+
| Field        | Type        | Null | Key | Default   | Extra          |
+--------------+-------------+------+-----+-----------+----------------+
| id           | int         | NO   | PRI | NULL      | auto_increment |
| vehicle_id   | varchar(50) | NO   |     | NULL      |                |
| vehicle_type | varchar(50) | NO   |     | NULL      |                |
| status       | varchar(50) | YES  |     | Available |                |
| location_lat | double      | YES  |     | NULL      |                |
| location_lon | double      | YES  |     | NULL      |                |
+--------------+-------------+------+-----+-----------+----------------+


## 🚀 Run Apps

### 1. Citizen App

[Live Demo](https://resqroute-citizen.onrender.com/)


### 2. Driver Dashboard

[Live Demo](https://resqroute-driverdashboard.onrender.com/)


### 3. Admin Dashboard

[Live Demo](https://resqroute-admindashboard.onrender.com/)


### 4. Control Room Dashboard

[Live Demo](https://resqroute-controlroom.onrender.com/)

## 📊 Admin Dashboard Analytics

- Pie Chart of Emergency Types
- Total Vehicles vs On Duty/Available
- Smart Alerts for system errors
- Real-time dashboard with task metrics and statuses

---

## 📦 Python Dependencies

streamlit
mysql-connector-python
pandas
folium
geopy
plotly
numpy
requests
streamlit-folium
```

---

## 💡 Future Improvements

- Integration with Google Maps for more accurate routing
- SMS/Email alerts to users
- Mobile app version for drivers
- Machine learning-based response prediction

---

## 👨‍🎓 Developed By

**ResQRoute**  
Member 1:
Name: Tanmay Kumar Singh
[LinkedIn](https://github.com/Soultk1977)  
Email: soultk1977@gmail.com  
Class: 12
School: Rajkiya Pratibha Vikas Vidyalaya, Link Road, Karol Bagh, New Delhi

Member 2:
Name: Saubhagya Kumar Singh
[LinkedIn](https://github.com/SirSaubhagya)
Email: soulck1977@gmail.com
Class: 9
School: Rana Pratap (Sindhi) Sarvodaya Vidyalaya, R-Block , New Rajendra Nagar, New Delhi

---
