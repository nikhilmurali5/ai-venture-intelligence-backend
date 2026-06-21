from app.services.llm_service import ask_llm


def generate_pitch_deck(idea: str):
    prompt = f"""
    Create an INVESTOR-READY STARTUP PITCH DECK for:

    {idea}

    IMPORTANT RULES:

    1. Return ONLY Markdown.
    2. Use proper headings.
    3. Use bullet points.
    4. Leave blank lines between sections.
    5. DO NOT return JSON.
    6. DO NOT write everything in one paragraph.
    7. Make it presentation-ready.
    8. Include realistic business assumptions and numbers.

    FORMAT:

    # Slide 1: Introduction

    ## Startup Name

    Create a professional startup name.

    ## Tagline

    Create a memorable tagline.

    ## Vision

    Brief vision statement.

    ---

    # Slide 2: Problem

    Describe the major problems customers face.

    * Problem 1
    * Problem 2
    * Problem 3

    ---

    # Slide 3: Solution

    Explain how the startup solves the problem.

    * Solution 1
    * Solution 2
    * Solution 3

    ---

    # Slide 4: Market Opportunity

    Include:

    * Total Addressable Market (TAM)
    * Serviceable Available Market (SAM)
    * Serviceable Obtainable Market (SOM)

    Provide realistic estimates.

    ---

    # Slide 5: Business Model

    Explain:

    * Revenue model
    * Pricing model
    * Customer segments

    ---

    # Slide 6: Revenue Streams

    Include:

    * Primary revenue source
    * Secondary revenue source
    * Additional revenue opportunities

    ---

    # Slide 7: Competitive Advantage

    Compare against competitors.

    Include:

    * Unique Selling Proposition
    * Competitive strengths
    * Market positioning

    ---

    # Slide 8: Go-To-Market Strategy

    Include:

    * Social media strategy
    * Digital marketing
    * Partnerships
    * Customer acquisition strategy

    ---

    # Slide 9: Financial Projections

    Include:

    * Startup cost
    * Year 1 revenue
    * Year 2 revenue
    * Year 3 revenue
    * Estimated profit

    Use realistic projections.

    ---

    # Slide 10: Investment Opportunity

    Include:

    * Funding required
    * Equity offered
    * Use of funds
    * Expected ROI

    ---

    # Final Investor Summary

    Provide a compelling investment conclusion.

    Generate a detailed professional pitch deck in markdown format.
    """

    return ask_llm(prompt)