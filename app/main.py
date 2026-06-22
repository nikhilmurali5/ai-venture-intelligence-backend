import json
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.schemas.idea import IdeaRequest
from app.core.database import engine, get_db
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user_email
)

from app.models.base import Base
from app.models.user import User

from app.schemas.user import UserCreate
from app.schemas.auth import LoginRequest
from app.agents.specialized.market_research import analyze_market
from app.agents.specialized.competition import analyze_competition
from app.agents.specialized.profitability import analyze_profitability
from app.agents.specialized.risk_analysis import analyze_risk
from app.agents.specialized.cost_estimation import estimate_cost
from app.agents.specialized.trend_forecaster import forecast_trends
from app.agents.specialized.viability_report import generate_viability_report
from app.agents.specialized.swot_analysis import analyze_swot
from app.agents.specialized.business_plan import generate_business_plan
from app.agents.specialized.pitch_deck import generate_pitch_deck
from app.agents.specialized.competitor_finder import find_competitors
#from app.agents.specialized.master_analysis import analyze_everything
from app.services.pdf_generator import generate_pdf
from app.models.analysis import Analysis
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware


import app.models

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-venture-intelligence-frontend.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "API Running"
    }


@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT 1")
        )

        return {
            "database": "connected",
            "result": result.scalar()
        }


@app.post("/create-user")
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if existing_user:
        return {
            "error": "Email already registered"
        }

    user = User(
        email=user_data.email,
        hashed_password=hash_password(
            user_data.password
        ),
        is_active=True
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "id": user.id,
        "email": user.email
    }


@app.post("/login")
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User)
        .filter(User.email == login_data.email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        login_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@app.get("/me")
def get_me(
    email: str = Depends(
        get_current_user_email
    )
):
    return {
        "email": email
    }

@app.post("/analyze-idea")
def analyze_idea(
    data: IdeaRequest,
    email: str = Depends(get_current_user_email),
    db: Session = Depends(get_db)
):
    print("START MARKET")
    market = analyze_market(data.idea)

    print("START COMPETITION")
    competition = analyze_competition(data.idea)

    print("START SWOT")
    swot = analyze_swot(data.idea)

    print("START BUSINESS PLAN")
    business_plan = generate_business_plan(data.idea)

    print("START PITCH DECK")
    pitch_deck = generate_pitch_deck(data.idea)

    print("START PROFITABILITY")
    profitability = analyze_profitability(data.idea)

    print("START RISK")
    risk = analyze_risk(data.idea)

    print("START COST")
    cost = estimate_cost(data.idea)

    print("START TREND")
    trend = forecast_trends(data.idea)

    print("START VIABILITY REPORT")
    viability_report = generate_viability_report(
        market,
        competition,
        profitability,
        risk,
        trend
    )

    print("ALL AGENTS COMPLETED")

    market = analyze_market(data.idea)

    competition = analyze_competition(data.idea)

    market = analyze_market(data.idea)

    competition = analyze_competition(data.idea)

    competition_score = (
            competition.get("competition_score")
            or competition.get("competition_analysis", {}).get("competition_score")
            or 70
    )

    swot = analyze_swot(data.idea)

    business_plan = generate_business_plan(data.idea)

    pitch_deck = generate_pitch_deck(data.idea)

    profitability = analyze_profitability(data.idea)

    risk = analyze_risk(data.idea)

    cost = estimate_cost(data.idea)

    trend = forecast_trends(data.idea)

    viability_report = generate_viability_report(
        market,
        competition,
        profitability,
        risk,
        trend
    )

    overall_score = round(
        (
                market["market_score"] * 0.30
                + profitability["profitability_score"] * 0.25
                + trend["trend_score"] * 0.20
                + competition_score * 0.15
                + (100 - risk["risk_score"]) * 0.10
        ),
        2
    )
    if overall_score >= 90:
        recommendation = "Excellent Opportunity"

    elif overall_score >= 80:
        recommendation = "Good Opportunity"

    elif overall_score >= 70:
        recommendation = "Moderate Opportunity"

    elif overall_score >= 60:
        recommendation = "Risky Opportunity"

    else:
        recommendation = "Not Recommended"
    analysis = Analysis(
        user_email=email,
        idea=data.idea,
        overall_score=overall_score,
        recommendation=recommendation,

        report=viability_report,

        swot_analysis=json.dumps(swot),
        business_plan=business_plan,

        pitch_deck=pitch_deck,

        viability_report=viability_report
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

    return {
        "id": analysis.id,

        "idea": data.idea,
        "market": market,
        "competition": competition,
        "profitability": profitability,
        "risk": risk,
        "cost_estimation": cost,
        "trend_forecast": trend,
        "swot_analysis": swot,
        "business_plan": business_plan,
        "pitch_deck": pitch_deck,
        "overall_score": overall_score,
        "recommendation": recommendation,
        "viability_report": viability_report
    }

@app.get("/my-analyses")
def my_analyses(
    email: str = Depends(get_current_user_email),
    db: Session = Depends(get_db)
):

    analyses = (
        db.query(Analysis)
        .filter(Analysis.user_email == email)
        .all()
    )

    return analyses
@app.get("/all-analyses")
def all_analyses(
    db: Session = Depends(get_db)
):
    return db.query(Analysis).all()
@app.get("/export-report/{analysis_id}")
def export_report(
    analysis_id: int,
    db: Session = Depends(get_db)
):

    analysis = (
        db.query(Analysis)
        .filter(Analysis.id == analysis_id)
        .first()
    )

    if not analysis:
        raise HTTPException(
            status_code=404,
            detail="Analysis not found"
        )

    filename = f"report_{analysis_id}.pdf"

    generate_pdf(
        filename,
        analysis
    )

    return FileResponse(
        filename,
        media_type="application/pdf",
        filename=filename
    )
@app.post("/pitch-deck")
def pitch_deck(data: IdeaRequest):

    deck = generate_pitch_deck(data.idea)

    return {
        "idea": data.idea,
        "pitch_deck": deck
    }
@app.post("/business-plan")
def business_plan(data: IdeaRequest):

    plan = generate_business_plan(data.idea)

    return {
        "idea": data.idea,
        "business_plan": plan
    }
@app.get("/dashboard-stats")
def dashboard_stats(
    db: Session = Depends(get_db)
):

    analyses = db.query(Analysis).all()

    total = len(analyses)

    avg_score = (
        sum(a.overall_score for a in analyses)
        / total
        if total > 0
        else 0
    )

    highest_score = (
        max(a.overall_score for a in analyses)
        if total > 0
        else 0
    )

    return {
        "total_analyses": total,
        "average_score": round(avg_score, 2),
        "highest_score": highest_score
    }
@app.get("/score-chart")
def score_chart(
    db: Session = Depends(get_db)
):
    analyses = db.query(Analysis).all()

    return [
        {
            "id": analysis.id,
            "score": analysis.overall_score
        }
        for analysis in analyses
    ]
@app.get("/recent-analyses")
def recent_analyses(
    db: Session = Depends(get_db)
):
    analyses = (
        db.query(Analysis)
        .order_by(Analysis.id.desc())
        .limit(10)
        .all()
    )

    return analyses
@app.post("/competitor-search")
def competitor_search(data: dict):

    idea = data["idea"]
    location = data["location"]

    competitors = find_competitors(
        idea,
        location
    )

    return competitors