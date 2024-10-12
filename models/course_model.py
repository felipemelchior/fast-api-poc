from core.configs import settings

from sqlalchemy import Column, Integer, String

class CourseModel(settings.DB_BASE_MODEL):
    __tablename__ = 'courses'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(100))
    classes: int = Column(Integer)
    hours: int = Column(Integer) 