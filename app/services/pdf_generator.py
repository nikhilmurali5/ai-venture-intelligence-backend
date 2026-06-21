from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
import json


def add_formatted_text(content, text, styles):

    if not text:
        return

    lines = str(text).split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        line = line.replace("**", "")

        # Headings
        if (
            "Executive Summary" in line
            or "Company Description" in line
            or "Market Analysis" in line
            or "Product and Services" in line
            or "Marketing Strategy" in line
            or "Operational Plan" in line
            or "Revenue Model" in line
            or "Financial Plan" in line
            or "Growth Strategy" in line
            or "Slide" in line
            or "Problem" in line
            or "Solution" in line
            or "Market Size" in line
            or "Competition" in line
            or "Go-To-Market" in line
            or "Investment Opportunity" in line
            or "Final Recommendation" in line
        ):

            content.append(
                Spacer(1, 8)
            )

            content.append(
                Paragraph(
                    f"<b>{line}</b>",
                    styles["Heading2"]
                )
            )

            content.append(
                Spacer(1, 4)
            )

        # Bullet points
        elif line.startswith("-") or line.startswith("•"):

            content.append(
                Paragraph(
                    f"• {line.replace('-', '').replace('•', '').strip()}",
                    styles["BodyText"]
                )
            )

        else:

            content.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

            content.append(
                Spacer(1, 2)
            )


def generate_pdf(filename, analysis):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    # ==========================
    # COVER PAGE
    # ==========================

    content.append(
        Paragraph(
            "AI Venture Intelligence Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"<b>Business Idea:</b> {analysis.idea}",
            styles["Heading2"]
        )
    )

    content.append(Spacer(1, 10))

    content.append(
        Paragraph(
            f"<b>Overall Score:</b> {analysis.overall_score}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Recommendation:</b> {analysis.recommendation}",
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # ==========================
    # SWOT ANALYSIS
    # ==========================

    content.append(
        Paragraph(
            "SWOT Analysis",
            styles["Heading1"]
        )
    )

    try:

        swot = json.loads(
            analysis.swot_analysis
        )

        content.append(
            Paragraph(
                "Strengths",
                styles["Heading2"]
            )
        )

        for item in swot.get("strengths", []):
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["BodyText"]
                )
            )

        content.append(Spacer(1, 10))

        content.append(
            Paragraph(
                "Weaknesses",
                styles["Heading2"]
            )
        )

        for item in swot.get("weaknesses", []):
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["BodyText"]
                )
            )

        content.append(Spacer(1, 10))

        content.append(
            Paragraph(
                "Opportunities",
                styles["Heading2"]
            )
        )

        for item in swot.get("opportunities", []):
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["BodyText"]
                )
            )

        content.append(Spacer(1, 10))

        content.append(
            Paragraph(
                "Threats",
                styles["Heading2"]
            )
        )

        for item in swot.get("threats", []):
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["BodyText"]
                )
            )

    except Exception:

        content.append(
            Paragraph(
                str(analysis.swot_analysis),
                styles["BodyText"]
            )
        )

    content.append(PageBreak())

    # ==========================
    # BUSINESS PLAN
    # ==========================

    content.append(
        Paragraph(
            "Business Plan",
            styles["Heading1"]
        )
    )

    add_formatted_text(
        content,
        analysis.business_plan,
        styles
    )

    content.append(PageBreak())

    # ==========================
    # PITCH DECK
    # ==========================

    content.append(
        Paragraph(
            "Pitch Deck",
            styles["Heading1"]
        )
    )

    add_formatted_text(
        content,
        analysis.pitch_deck,
        styles
    )

    content.append(PageBreak())

    # ==========================
    # VIABILITY REPORT
    # ==========================

    content.append(
        Paragraph(
            "Viability Report",
            styles["Heading1"]
        )
    )

    add_formatted_text(
        content,
        analysis.viability_report,
        styles
    )

    doc.build(content)