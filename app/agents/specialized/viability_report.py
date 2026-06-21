import json
from app.services.llm_service import ask_llm

def generate_viability_report(
    market,
    competition,
    profitability,
    risk,
    trend
):
    prompt = f"""
    Based on the following business analysis:

    # Market Analysis

    {market}

    # Competition Analysis

    {competition}

    # Profitability Analysis

    {profitability}

    # Risk Analysis

    {risk}

    # Trend Forecast

    {trend}

    IMPORTANT RULES:

    1. Return ONLY Markdown.
    2. Use proper headings.
    3. Use bullet points.
    4. Leave blank lines between sections.
    5. Do NOT return JSON.
    6. Do NOT write everything in one paragraph.
    7. Make it suitable for investors and business founders.
    8. Provide actionable insights.

    FORMAT:

    # Executive Summary

    Provide a detailed summary of the business opportunity.

    ---

    # Market Potential

    Include:

    * Market size
    * Demand outlook
    * Customer opportunity
    * Growth potential

    ---

    # Competitive Analysis

    Include:

    * Main competitors
    * Competitive strengths
    * Competitive weaknesses
    * Market positioning

    ---

    # Profitability Assessment

    Include:

    * Revenue potential
    * Profit margin outlook
    * Monetization opportunities

    ---

    # Risk Assessment

    Include:

    * Operational risks
    * Financial risks
    * Market risks

    For each risk provide mitigation strategies.

    ---

    # Industry Trends

    Include:

    * Current trends
    * Emerging opportunities
    * Future outlook

    ---

    # Strengths

    * Strength 1
    * Strength 2
    * Strength 3

    ---

    # Weaknesses

    * Weakness 1
    * Weakness 2
    * Weakness 3

    ---

    # Opportunities

    * Opportunity 1
    * Opportunity 2
    * Opportunity 3

    ---

    # Threats

    * Threat 1
    * Threat 2
    * Threat 3

    ---

    # Final Recommendation

    Provide:

    * Overall viability score explanation
    * Investment attractiveness
    * Recommended next steps
    * Final conclusion

    Generate a professional investor-grade viability report in markdown format.
    """

    return ask_llm(prompt)