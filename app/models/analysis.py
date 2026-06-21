from sqlalchemy import Column, Integer, String, Float, Text
from app.models.base import Base


class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)

    user_email = Column(String)
    idea = Column(String)

    overall_score = Column(Float)
    recommendation = Column(String)

    report = Column(Text)

    swot_analysis = Column(Text)
    business_plan = Column(Text)
    pitch_deck = Column(Text)
    viability_report = Column(Text)