from app.services.llm_service import ask_llm


def generate_business_plan(idea: str):
    prompt = f"""
You are an expert business consultant and venture capital analyst. Your task is to generate a comprehensive, highly detailed, and PROFESSIONAL INVESTOR-READY BUSINESS PLAN based on the provided business idea, executive summary, or notes.

BUSINESS IDEA / INPUT:
{idea}

CRITICAL FORMATTING RULES:
1. Return ONLY valid Markdown. Do not wrap the response in markdown code blocks (e.g., do not use ```markdown ... ```).
2. Use a single "#" for main headings (e.g., # Executive Summary). Always leave a single space after the "#" character.
3. Use a horizontal rule "---" on its own line to visually separate every major section.
4. Leave exactly one blank line before and after every heading, bullet point, and horizontal rule.
5. For sections containing lists, use clean bullet points ("* "). Bold the key phrase at the beginning of the bullet point, followed by a colon, and then write a detailed description (e.g., "* **Business Concept:** Detailed explanation...").
6. NEVER use tables or JSON.
7. Avoid dense walls of text. Ensure a clear, scannable hierarchy optimized for both dashboard displays and PDF generation.

STRUCTURE AND CONTENT TO GENERATE:

# Executive Summary

Write 2-4 highly detailed, professional paragraphs outlining the business value proposition, market fit, and overarching strategy. Ensure there is a blank line between each paragraph.

---

# Company Description

Provide a detailed bulleted list covering:
* **Business Concept:** [Detailed explanation]
* **Vision:** [Detailed explanation]
* **Mission:** [Detailed explanation]
* **Target Customers:** [Detailed explanation]

---

# Market Analysis

Provide a detailed bulleted list covering:
* **Industry Overview:** [Detailed explanation]
* **Market Size:** [Detailed explanation]
* **Target Audience:** [Detailed explanation]
* **Customer Demand:** [Detailed explanation]

---

# Products and Services

Provide a detailed bulleted list covering:
* **Core Offering:** [Detailed explanation]
* **Premium Offerings:** [Detailed explanation]
* **Unique Selling Proposition:** [Detailed explanation]

---

# Marketing Strategy

Provide a detailed bulleted list covering:
* **Social Media Strategy:** [Detailed explanation]
* **Digital Marketing:** [Detailed explanation]
* **Offline Marketing:** [Detailed explanation]
* **Customer Acquisition:** [Detailed explanation]

---

# Operational Plan

Provide a detailed bulleted list covering:
* **Daily Operations:** [Detailed explanation]
* **Staffing Requirements:** [Detailed explanation]
* **Technology Requirements:** [Detailed explanation]
* **Supply Chain Requirements:** [Detailed explanation]

---

# Revenue Model

Provide a detailed bulleted list covering:
* **Primary Revenue Streams:** [Detailed explanation]
* **Secondary Revenue Streams:** [Detailed explanation]
* **Pricing Strategy:** [Detailed explanation]

---

# Financial Plan

Provide a detailed bulleted list covering:
* **Startup Costs:** [Detailed explanation]
* **Monthly Expenses:** [Detailed explanation]
* **Revenue Projections:** [Detailed explanation]
* **Break-Even Estimate:** [Detailed explanation]

---

# Growth Strategy

Provide a detailed bulleted list covering:
* **Expansion Opportunities:** [Detailed explanation]
* **Partnerships:** [Detailed explanation]
* **Scaling Strategy:** [Detailed explanation]

---

# Risk Assessment

Provide a detailed bulleted list covering:
* **Key Risks:** [Detailed explanation]
* **Mitigation Strategies:** [Detailed explanation]

---

# Conclusion

Write a final, authoritative business recommendation paragraph summarizing why this venture is a viable and lucrative opportunity for investors.
"""

    return ask_llm(prompt)