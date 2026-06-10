from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "adm_m_student"

    admno = Column(String, primary_key=True)
    class_name = Column("class", String)
    academic_year = Column(String)
    admission_date = Column(Date)
    section = Column(String)
    application_status = Column(String)