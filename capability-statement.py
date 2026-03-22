#!/usr/bin/env python3
"""Generate K Auto Tech LLC Capability Statement PDF"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.enums import TA_LEFT, TA_CENTER

WIDTH, HEIGHT = letter
CORAL = HexColor('#E8604C')
CORAL_DARK = HexColor('#D4503E')
NAVY = HexColor('#0a1628')
NAVY_LIGHT = HexColor('#1a2a4a')
SLATE = HexColor('#475569')
GRAY_BG = HexColor('#f8fafc')
WHITE = white
BLACK = black

def draw_page(c):
    # === TOP BAR ===
    c.setFillColor(NAVY)
    c.rect(0, HEIGHT - 1.2*inch, WIDTH, 1.2*inch, fill=1, stroke=0)

    # Coral accent stripe
    c.setFillColor(CORAL)
    c.rect(0, HEIGHT - 1.2*inch, WIDTH, 4, fill=1, stroke=0)

    # Company name
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(0.75*inch, HEIGHT - 0.65*inch, "K Auto Tech LLC")

    # Descriptor
    c.setFont("Helvetica", 9)
    c.setFillColor(HexColor('#94a3b8'))
    c.drawString(0.75*inch, HEIGHT - 0.9*inch, "Automation, Software & Modernization Consulting")

    # "CAPABILITY STATEMENT" right-aligned
    c.setFillColor(CORAL)
    c.setFont("Helvetica-Bold", 10)
    c.drawRightString(WIDTH - 0.75*inch, HEIGHT - 0.65*inch, "CAPABILITY STATEMENT")
    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor('#94a3b8'))
    c.drawRightString(WIDTH - 0.75*inch, HEIGHT - 0.85*inch, "kautotech.com")

    y = HEIGHT - 1.65*inch
    left_col_x = 0.75*inch
    right_col_x = 4.5*inch
    left_col_w = 3.5*inch
    right_col_w = 3.35*inch

    # === COMPANY OVERVIEW ===
    c.setFillColor(CORAL)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left_col_x, y, "COMPANY OVERVIEW")
    c.setStrokeColor(CORAL)
    c.setLineWidth(1.5)
    c.line(left_col_x, y - 4, left_col_x + 1.8*inch, y - 4)
    y -= 20

    overview_text = (
        "K Auto Tech LLC is a technical consulting and software development firm "
        "specializing in workflow automation, custom software, and digital modernization "
        "for government agencies, public authorities, and operationally complex organizations. "
        "We operate as a focused, execution-oriented firm that understands operations and "
        "delivers practical systems that reduce administrative burden, improve visibility, "
        "and produce measurable results."
    )

    style = ParagraphStyle('overview', fontName='Helvetica', fontSize=8.5,
                           leading=12, textColor=SLATE)
    p = Paragraph(overview_text, style)
    w, h = p.wrap(left_col_w, 200)
    p.drawOn(c, left_col_x, y - h)
    y -= h + 18

    # === CORE COMPETENCIES ===
    c.setFillColor(CORAL)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left_col_x, y, "CORE COMPETENCIES")
    c.setStrokeColor(CORAL)
    c.line(left_col_x, y - 4, left_col_x + 1.8*inch, y - 4)
    y -= 18

    competencies = [
        "Workflow Automation & Process Digitization",
        "Custom Software Development (Web, Internal Tools, Portals)",
        "Data Dashboards & Operational Reporting",
        "Systems Integration & Interoperability",
        "Digital Modernization Strategy & Implementation",
        "AI-Enabled Process Improvement",
        "Legacy System Enhancement & Replacement",
        "Compliance-Aware Technical Consulting",
    ]

    c.setFont("Helvetica", 8.5)
    c.setFillColor(SLATE)
    for comp in competencies:
        # Coral bullet
        c.setFillColor(CORAL)
        c.circle(left_col_x + 4, y + 2.5, 2.5, fill=1, stroke=0)
        c.setFillColor(SLATE)
        c.drawString(left_col_x + 14, y, comp)
        y -= 14

    y -= 12

    # === DIFFERENTIATORS ===
    c.setFillColor(CORAL)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(left_col_x, y, "DIFFERENTIATORS")
    c.setStrokeColor(CORAL)
    c.line(left_col_x, y - 4, left_col_x + 1.5*inch, y - 4)
    y -= 18

    diffs = [
        ("Operations-First Approach", "We assess how your organization actually works before proposing any technology solution."),
        ("End-to-End Delivery", "Same team from assessment through deployment. No handoffs to third-party implementers."),
        ("Faster Than Enterprise Firms", "No six-month discovery phases. We scope quickly, build iteratively, deliver working systems."),
        ("Procurement-Ready", "We understand government procurement processes, documentation requirements, and compliance expectations."),
    ]

    for title, desc in diffs:
        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(NAVY)
        c.drawString(left_col_x, y, title)
        y -= 12
        c.setFont("Helvetica", 8)
        c.setFillColor(SLATE)
        p = Paragraph(desc, ParagraphStyle('diff', fontName='Helvetica', fontSize=8,
                                            leading=10.5, textColor=SLATE))
        w, h = p.wrap(left_col_w, 100)
        p.drawOn(c, left_col_x, y - h)
        y -= h + 10

    # ============ RIGHT COLUMN ============
    ry = HEIGHT - 1.65*inch

    # === NAICS CODES ===
    c.setFillColor(CORAL)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_col_x, ry, "NAICS CODES")
    c.setStrokeColor(CORAL)
    c.line(right_col_x, ry - 4, right_col_x + 1.3*inch, ry - 4)
    ry -= 18

    naics = [
        ("541511", "Custom Computer Programming Services"),
        ("541512", "Computer Systems Design Services"),
        ("541519", "Other Computer Related Services"),
        ("541611", "Admin & General Management Consulting"),
        ("541690", "Other Scientific & Technical Consulting"),
    ]

    for code, desc in naics:
        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(NAVY)
        c.drawString(right_col_x, ry, code)
        c.setFont("Helvetica", 8)
        c.setFillColor(SLATE)
        c.drawString(right_col_x + 50, ry, desc)
        ry -= 13

    ry -= 14

    # === TARGET AGENCIES & DEPARTMENTS ===
    c.setFillColor(CORAL)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_col_x, ry, "TARGET AGENCIES & SECTORS")
    c.setStrokeColor(CORAL)
    c.line(right_col_x, ry - 4, right_col_x + 2.2*inch, ry - 4)
    ry -= 18

    targets = [
        "Municipal & County Government",
        "State & Provincial Agencies",
        "Public Authorities & Utilities",
        "Transportation & Transit Agencies",
        "Permitting & Licensing Departments",
        "Procurement & Administration",
        "Infrastructure & Public Works",
        "Economic Development Agencies",
        "Regulated Private Sector",
    ]

    c.setFont("Helvetica", 8.5)
    for t in targets:
        c.setFillColor(CORAL)
        c.circle(right_col_x + 4, ry + 2.5, 2.5, fill=1, stroke=0)
        c.setFillColor(SLATE)
        c.drawString(right_col_x + 14, ry, t)
        ry -= 13

    ry -= 14

    # === MARKETS SERVED ===
    c.setFillColor(CORAL)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_col_x, ry, "MARKETS SERVED")
    c.setStrokeColor(CORAL)
    c.line(right_col_x, ry - 4, right_col_x + 1.5*inch, ry - 4)
    ry -= 18

    markets = [
        "United States (Federal, State, Local)",
        "Canada (Federal, Provincial, Municipal)",
        "Caribbean (Jamaica, Trinidad & Tobago,",
        "   Bahamas, Barbados, Guyana, Dominican",
        "   Republic, St. Lucia, and region-wide)",
    ]

    c.setFont("Helvetica", 8.5)
    c.setFillColor(SLATE)
    for m in markets:
        if m.startswith("   "):
            c.drawString(right_col_x + 14, ry, m.strip())
        else:
            c.setFillColor(CORAL)
            c.circle(right_col_x + 4, ry + 2.5, 2.5, fill=1, stroke=0)
            c.setFillColor(SLATE)
            c.drawString(right_col_x + 14, ry, m)
        ry -= 13

    ry -= 14

    # === CONTRACTING APPROACH ===
    c.setFillColor(CORAL)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_col_x, ry, "CONTRACTING APPROACH")
    c.setStrokeColor(CORAL)
    c.line(right_col_x, ry - 4, right_col_x + 2*inch, ry - 4)
    ry -= 18

    contracting = [
        "Project-based fixed-scope engagements",
        "Time & materials consulting",
        "Retainer arrangements",
        "Subcontracting / teaming support",
        "Staff augmentation",
    ]

    c.setFont("Helvetica", 8.5)
    for ct in contracting:
        c.setFillColor(CORAL)
        c.circle(right_col_x + 4, ry + 2.5, 2.5, fill=1, stroke=0)
        c.setFillColor(SLATE)
        c.drawString(right_col_x + 14, ry, ct)
        ry -= 13

    # === BOTTOM CONTACT BAR ===
    bar_h = 0.7*inch
    c.setFillColor(NAVY)
    c.rect(0, 0, WIDTH, bar_h, fill=1, stroke=0)

    # Coral accent on top of bar
    c.setFillColor(CORAL)
    c.rect(0, bar_h, WIDTH, 3, fill=1, stroke=0)

    # Contact info
    contact_y = 0.35*inch
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(0.75*inch, contact_y, "K Auto Tech LLC")

    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor('#94a3b8'))
    c.drawString(0.75*inch, contact_y - 14, "Houston, Texas  |  info@kautotech.com  |  kautotech.com")

    # Right side CTA
    c.setFillColor(CORAL)
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(WIDTH - 0.75*inch, contact_y, "Request a consultation at kautotech.com")
    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor('#94a3b8'))
    c.drawRightString(WIDTH - 0.75*inch, contact_y - 14, "Automation, Software & Modernization Consulting")


# Generate PDF
output_path = "/sessions/ecstatic-modest-johnson/mnt/outputs/autotech-consulting/K-Auto-Tech-Capability-Statement.pdf"
c = canvas.Canvas(output_path, pagesize=letter)
c.setTitle("K Auto Tech LLC - Capability Statement")
c.setAuthor("K Auto Tech LLC")
c.setSubject("Capability Statement - Automation, Software & Modernization Consulting")
draw_page(c)
c.save()
print(f"PDF created: {output_path}")
