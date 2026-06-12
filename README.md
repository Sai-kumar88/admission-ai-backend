
# 🎓 Admission Analytics Dashboard Backend

## 📌 Project Description

Admission Analytics Dashboard is a FastAPI-based backend application developed to help educational institutions analyze admission data, monitor admission trends, visualize class-wise distribution, track admission funnel stages, and generate Machine Learning-based admission forecasts with AI-generated business insights.

The system retrieves admission data from PostgreSQL, performs data cleaning, predicts future admissions using Linear Regression, generates AI insights using Groq LLM, and exposes analytical data through REST APIs for dashboard visualization.

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

### 6. Machine Learning Prediction

Uses Linear Regression to:

* Analyze historical admissions
* Predict next year's admissions
* Generate admission growth trends

### 7. AI-Powered Business Insight

Uses Groq LLM to:

* Interpret ML prediction results
* Generate business-friendly admission insights
* Provide understandable summaries for end users

### 8. JSON Response Caching

Stores generated dashboard data in a local JSON file to:

* Reduce database load
* Improve API response time
* Minimize repeated AI requests

---

## 🏗️ System Architecture

```text
PostgreSQL Database
        │
        ▼
Data Cleaning
        │
        ▼
Linear Regression (ML)
        │
        ▼
Predicted Admissions
        │
        ▼
Growth Trend
        │
        ▼
Groq LLM
        │
        ▼
AI Insight
        │
        ▼
FastAPI Backend
        │
        ▼
Frontend Dashboard
```

---

## 🛠️ Technology Stack

| Technology        | Purpose                  |
| ----------------- | ------------------------ |
| Python            | Backend Development      |
| FastAPI           | REST API Framework       |
| SQLAlchemy        | Database Access          |
| PostgreSQL        | Data Storage             |
| Scikit-Learn      | Machine Learning         |
| Linear Regression | Admission Prediction     |
| NumPy             | Data Processing          |
| Groq API          | AI Insight Generation    |
| JSON Cache        | Performance Optimization |

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
│   │   ├── ml_service.py
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
GROQ_API_KEY=your_groq_api_key
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

### Response Includes

* Total Admissions
* Academic Year Analysis
* Class-wise Analysis
* Historical Admission Trends
* Admission Funnel Analysis
* Predicted Admissions
* Growth Trend
* AI Insight

---

## 📈 Performance Optimization

The dashboard data is cached in:

```text
app/cache/dashboard.json
```

Benefits:

* Faster API responses
* Reduced database queries
* Reduced AI requests
* Improved scalability

---

## 🎯 Business Benefits

* Faster admission analysis
* Data-driven decision making
* Admission trend monitoring
* Capacity planning support
* Historical trend visualization
* Machine Learning-based forecasting
* AI-powered business insights
* Better admission planning

---

## 🔮 Future Enhancements

* Multi-school analytics
* Advanced forecasting models
* Admission forecasting by class
* PDF/Excel report exports
* Real-time dashboard updates
* Comparative admission analysis