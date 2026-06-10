# 🎓 Admission Analytics Dashboard Backend

## 📌 Project Description

Admission Analytics Dashboard is a FastAPI-based backend application developed to help educational institutions analyze admission data, monitor admission trends, visualize class-wise distribution, track admission funnel stages, and generate AI-powered admission forecasts.

The system retrieves admission data from PostgreSQL, processes analytical insights, and exposes them through REST APIs for dashboard visualization.

---

## 🚀 Key Features

### 1. Total Admissions

Displays the total number of admissions available in the system.

### 2. Academic Year Analysis

Provides admission counts grouped by academic year to identify long-term trends.

### 3. Class-wise Analysis

Shows admission distribution across different classes.

### 4. Historical Admission Trends

Tracks admission growth and decline across academic years.

### 5. Admission Funnel Analysis

Displays admission statuses such as:

* Confirm
* In Progress
* Waiting
* Rejected
* Selected

### 6. AI-Powered Prediction

Uses historical admission data to predict future admission trends and provide business insights.

### 7. JSON Response Caching

Stores generated dashboard data in a local JSON file to:

* Reduce database load
* Improve API response time
* Minimize repeated AI requests

---

## 🏗️ System Architecture

```text
Frontend Dashboard
        │
        ▼
FastAPI Backend
        │
 ┌──────┴──────┐
 │             │
 ▼             ▼
PostgreSQL     AI Prediction Service
Database
        │
        ▼
JSON Cache Layer
```

---

## 🛠️ Technology Stack

| Technology | Purpose                  |
| ---------- | ------------------------ |
| Python     | Backend Development      |
| FastAPI    | REST API Framework       |
| SQLAlchemy | Database Access          |
| PostgreSQL | Data Storage             |
| OpenAI API | AI Prediction            |
| JSON Cache | Performance Optimization |

---

## 📂 Project Structure

```text
dashboard-backend/
│
├── app/
│   ├── cache/
│   │   └── dashboard.json
│   │
│   ├── routers/
│   │   └── trends.py
│   │
│   ├── services/
│   │   └── ai_service.py
│   │
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd dashboard-backend
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 Environment Variables

Create a `.env` file:

```env
DATABASE_URL=your_postgresql_connection_string
GROQ_API_KEY=your_GROQ_API_KEY
```

---

## ▶️ Run Application

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoint

### Dashboard Analytics

```http
GET /dashboard
```

### Sample Response

Returns:

* Total Admissions
* Academic Year Analysis
* Class-wise Analysis
* Historical Trends
* Funnel Analysis
* AI Prediction

---

## 📈 Performance Optimization

The dashboard data is cached in:

```text
app/cache/dashboard.json
```

Benefits:

* Faster response time
* Reduced database queries
* Reduced AI API calls
* Improved scalability

---

## 🎯 Business Benefits

* Faster admission analysis
* Data-driven decision making
* Admission trend monitoring
* Capacity planning support
* Improved visibility of admission pipeline
* Predictive admission forecasting

---


