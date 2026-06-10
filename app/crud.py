from app.services.ai_service import generate_ai_insight
from sqlalchemy import text
import json
import os

CACHE_FILE = "app/cache/dashboard.json"

def get_cached_dashboard():

    if os.path.exists(CACHE_FILE):

        print("CACHE HIT")

        try:
            with open(CACHE_FILE, "r") as f:
                return json.load(f)

        except Exception:
            return None

    print("DATABASE HIT")
    return None

def save_dashboard_cache(data):

    os.makedirs("app/cache", exist_ok=True)

    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_total_admissions(db):

    query = text("""
        SELECT COUNT(*) AS total
        FROM "Adm_M_Student"
    """)

    return db.execute(query).scalar()

def get_year_wise(db):

    query = text("""
        SELECT
            b."ASMAY_Year" AS academic_year,
            COUNT(*) AS total
        FROM "Adm_M_Student" a
        JOIN "Adm_School_M_Academic_Year" b
            ON a."ASMAY_Id" = b."ASMAY_Id"
        GROUP BY b."ASMAY_Year"
        ORDER BY b."ASMAY_Year"
    """)

    rows = db.execute(query).fetchall()

    return [dict(row._mapping) for row in rows]

def get_class_wise(db):

    query = text("""
           SELECT
           b."ASMCL_ClassName" ,
            COUNT(*) AS total
        FROM "Adm_M_Student" a
        join "Adm_School_M_Class" b on a."ASMCL_Id" =b."ASMCL_Id"          
        GROUP BY "ASMCL_ClassName"
        order by "ASMCL_ClassName"
    """)

    rows = db.execute(query).fetchall()

    return [dict(row._mapping) for row in rows]


def get_funnel_analysis(db):

    query = text("""
         SELECT DISTINCT
             "PAMST_Status" AS status
         FROM "Preadmission_Master_Status"
         ORDER BY status
     """)

    rows = db.execute(query).fetchall()

    return [dict(row._mapping) for row in rows]


def get_historical_admissions(db):

    query = text("""
        SELECT
            b."ASMAY_Year" AS academic_year,
            COUNT(*) AS total
        FROM "Adm_M_Student" a
        JOIN "Adm_School_M_Academic_Year" b
            ON a."ASMAY_Id" = b."ASMAY_Id"
        GROUP BY b."ASMAY_Year"
        ORDER BY b."ASMAY_Year"
    """)

    rows = db.execute(query).fetchall()

    return [dict(row._mapping) for row in rows]

def get_dashboard_data(db):

    cached = get_cached_dashboard()

    print("cached =", cached)

    if cached:
        print("CACHE HIT")
        return cached

    print("AI EXECUTED")

    historical_data = get_historical_admissions(db)

    ai_prediction = "test"

    data = {
        "total_admissions": get_total_admissions(db),
        "year_wise": get_year_wise(db),
        "class_wise": get_class_wise(db),
        "historical_admissions": historical_data,
        "funnel_analysis": get_funnel_analysis(db),
        "ai_prediction": ai_prediction
    }

    #save_dashboard_cache(data)

    return data