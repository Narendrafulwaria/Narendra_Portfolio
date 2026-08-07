# =============================================================================
# utils/data.py — Single source of truth for all portfolio content
# Update this file to change any text on the site. No hardcoding in sections.
# =============================================================================

# -----------------------------------------------------------------------------
# Personal Info
# -----------------------------------------------------------------------------
PERSONAL_INFO = {
    "name": "Narendra Madanlal Fulwaria",
    "tagline": "Data Analyst | AI Automation | Business Analytics",
    "location": "Mumbai, Maharashtra",
    "phone": "9833607051",
    "email": "narendrafulwaria111@gmail.com",
    "github_url": "https://github.com/Narendrafulwaria",
    "linkedin_url": "https://www.linkedin.com/in/narendrafulwaria/",
    "bio": (
        "Electronics & Telecommunication Engineering graduate with 6+ years of "
        "business operations and retail management experience. Currently transitioning "
        "into Data Analytics, Business Analytics, AI Automation and Generative AI. "
        "Skilled in Python, SQL, Excel, Tableau, Power BI, Data Analysis and workflow "
        "automation using n8n. Proven track record of driving business growth, managing "
        "teams, optimizing inventory, analyzing business data and implementing customer "
        "retention strategies."
    ),
    "traits": ["🧠 Analytical Thinker", "🔧 Problem Solver", "📚 Self-Learner"],
}

# -----------------------------------------------------------------------------
# Technical Skills
# -----------------------------------------------------------------------------
SKILLS = {
    "Programming": ["Python", "SQL", "MySQL"],
    "Analytics": ["Pandas", "NumPy", "Data Cleaning", "Data Visualization"],
    "BI Tools": ["Excel", "Tableau", "Power BI"],
    "Automation": ["n8n", "Webhooks", "AI Workflow Automation"],
    "Other": ["GitHub", "Business Analytics", "Inventory Analytics", "CRM", "Team Management"],
}

SKILL_PROFICIENCY = {
    "Python": 75,
    "SQL": 80,
    "Data Analytics": 78,
    "BI Tools": 72,
    "AI Automation": 85,
    "Business Operations": 95,
}

# -----------------------------------------------------------------------------
# Projects
# -----------------------------------------------------------------------------
PROJECTS = [
    {
        "title": "AI Resume Analyzer Workflow",
        "description": (
            "Built an AI-powered resume analysis workflow using n8n, webhooks and "
            "database integration. Automated resume parsing, ATS analysis and "
            "recommendation generation."
        ),
        "tech": ["n8n", "Webhooks", "Database", "AI"],
        "url": "https://github.com/Narendrafulwaria/N8N_project_Resume_analyzer_Webhook",
    },
    {
        "title": "Leave Management Automation System",
        "description": (
            "Developed an automated leave management workflow integrating Telegram, "
            "Google Sheets and Gmail. Automated leave request processing and "
            "notification management."
        ),
        "tech": ["n8n", "Telegram", "Google Sheets", "Gmail"],
        "url": "https://github.com/Narendrafulwaria/N8N_leave_management_Telegram_sheets_gmail",
    },
    {
        "title": "AI Leave Management Chatbot",
        "description": (
            "Designed a chatbot-based HR automation solution to streamline employee "
            "leave applications and workflow management."
        ),
        "tech": ["n8n", "Chatbot", "HR Automation", "AI"],
        "url": "https://github.com/Narendrafulwaria/N8N_project_Leave_management_chatbot_based",
    },
    {
        "title": "Python Analytics Portfolio",
        "description": (
            "Built Python projects covering data structures, business analytics, "
            "inventory management, functions, modules and analytical problem solving."
        ),
        "tech": ["Python", "Pandas", "NumPy", "Data Analysis"],
        "url": "https://github.com/Narendrafulwaria/-Python-Projects",
    },
    {
        "title": "SQL Analytics Portfolio",
        "description": (
            "Developed SQL solutions using joins, subqueries, CTEs, aggregations and "
            "window functions to solve business reporting and analytics problems."
        ),
        "tech": ["SQL", "MySQL", "CTEs", "Window Functions"],
        "url": "https://github.com/Narendrafulwaria/MySql_Queries",
    },
]

# -----------------------------------------------------------------------------
# Professional Experience
# -----------------------------------------------------------------------------
EXPERIENCE = [
    {
        "role": "Business Operations Manager",
        "company": "Bhawani Supermart",
        "period": "2020 – Present",
        "bullets": [
            "Built and scaled a family-owned retail grocery business from inception.",
            "Increased daily customer footfall from 250 to 400 through targeted promotional campaigns.",
            "Achieved approximately 75% growth in daily sales through customer retention and loyalty initiatives.",
            "Managed procurement, inventory control, merchandising and replenishment operations.",
            "Led and supervised a team of 5 employees across customer service and store operations.",
            "Implemented data-driven pricing, seasonal promotions and stock optimization strategies.",
        ],
    },
    {
        "role": "Fresh Fruits & Vegetables Operations",
        "company": "Bhawani Supermart",
        "period": "2023 – Present",
        "bullets": [
            "Established and managed a dedicated fruits and vegetables department.",
            "Tracked shelf life, spoilage rates and inventory turnover to reduce waste.",
            "Maintained fresh inventory availability while optimizing procurement costs.",
            "Improved visual merchandising and customer purchasing experience.",
        ],
    },
]

# -----------------------------------------------------------------------------
# Education
# -----------------------------------------------------------------------------
EDUCATION = [
    {
        "degree": "Bachelor of Engineering (Electronics & Telecommunication)",
        "institution": "Ramrao Adik Institute of Technology, Mumbai University",
        "year": "2019",
    },
    {
        "degree": "Higher Secondary Certificate (HSC)",
        "institution": "Swami Vivekanand High School",
        "year": "2015",
    },
    {
        "degree": "Secondary School Certificate (SSC)",
        "institution": "Adarsha Vidyalaya School",
        "year": "2013",
    },
]

# -----------------------------------------------------------------------------
# Certifications
# -----------------------------------------------------------------------------
CERTIFICATIONS = [
    {"name": "AI Fundamentals & Ecosystem Mastery", "issuer": "Be10X", "status": "Completed"},
    {"name": "AI Product Building, Storytelling & Marketing", "issuer": "Be10X", "status": "Completed"},
    {"name": "AI Agents & Autonomous Systems", "issuer": "Be10X", "status": "Completed"},
    {"name": "Career Readiness Using AI", "issuer": "Be10X", "status": "Completed"},
    {
        "name": "AI Career Accelerator Program (6 Months)",
        "issuer": "Be10X — Certificate of Mastery",
        "status": "Completed",
    },
    {
        "name": "Capstone Project — AI Career Accelerator Program",
        "issuer": "Be10X — Certificate of Mastery",
        "status": "Completed",
    },
    {
        "name": "Cricket Analytics Advanced Masterclass",
        "issuer": "Mad About Sports & Rajasthan Royals (May 2023)",
        "status": "Completed",
    },
    {
        "name": "Data Analytics with AI & Generative AI",
        "issuer": "IIT Roorkee & Masai",
        "status": "In Progress",
    },
]

# -----------------------------------------------------------------------------
# Key Achievements
# -----------------------------------------------------------------------------
ACHIEVEMENTS = [
    {
        "icon": "📈",
        "value": "75%",
        "label": "Growth in Daily Sales",
        "detail": "Through customer retention and loyalty initiatives at Bhawani Supermart.",
    },
    {
        "icon": "👥",
        "value": "400+",
        "label": "Daily Customer Footfall",
        "detail": "Increased from 250 through targeted promotional campaigns.",
    },
    {
        "icon": "💼",
        "value": "6+ Years",
        "label": "Retail Operations",
        "detail": "End-to-end management of retail operations from inception.",
    },
    {
        "icon": "🔄",
        "value": "Career",
        "label": "Transition to Data & AI",
        "detail": (
            "Successfully transitioned from business operations into Data Analytics "
            "and AI upskilling with multiple GitHub projects."
        ),
    },
]

# -----------------------------------------------------------------------------
# Blog Posts (placeholders — replace with real article links)
# -----------------------------------------------------------------------------
BLOG_POSTS = [
    {
        "title": "What I Learned Building an AI Resume Analyzer",
        "excerpt": (
            "A deep dive into building an n8n-powered resume analysis workflow — "
            "from webhook triggers to ATS scoring and recommendation generation."
        ),
        "date": "July 2025",
        "url": "https://www.linkedin.com/in/narendrafulwaria",  # Replace with actual article URL
    },
    {
        "title": "How n8n Changed the Way I Think About Automation",
        "excerpt": (
            "Exploring how low-code AI workflow automation with n8n can replace "
            "manual processes and save hours every week."
        ),
        "date": "June 2025",
        "url": "https://www.linkedin.com/in/narendrafulwaria",  # Replace with actual article URL
    },
    {
        "title": "From Retail Manager to Data Analyst – My Transition Story",
        "excerpt": (
            "How 6+ years of business operations experience became my biggest advantage "
            "while transitioning into Data Analytics and AI."
        ),
        "date": "May 2025",
        "url": "https://www.linkedin.com/in/narendrafulwaria",  # Replace with actual article URL
    },
]

# -----------------------------------------------------------------------------
# Static FAQ — Chatbot fallback when no GROQ_API_KEY is configured
# -----------------------------------------------------------------------------
CHATBOT_FAQ = {
    "projects": (
        "Narendra has built 5 projects: AI Resume Analyzer Workflow, Leave Management "
        "Automation System, AI Leave Management Chatbot, Python Analytics Portfolio, "
        "and SQL Analytics Portfolio. All are available on his GitHub."
    ),
    "skills": (
        "Narendra is skilled in Python, SQL, MySQL, Pandas, NumPy, Excel, Tableau, "
        "Power BI, n8n automation, and AI workflow design."
    ),
    "experience": (
        "Narendra has 6+ years of experience as Business Operations Manager at "
        "Bhawani Supermart, managing inventory, procurement, team leadership, and "
        "data-driven strategy."
    ),
    "certifications": (
        "Narendra holds Be10X certifications in AI Fundamentals, AI Agents & Autonomous "
        "Systems, AI Product Building, Career Readiness Using AI, and the AI Career "
        "Accelerator Program (including Capstone). He also completed the Cricket Analytics "
        "Advanced Masterclass with Mad About Sports & Rajasthan Royals, and is pursuing "
        "Data Analytics with AI & Generative AI from IIT Roorkee & Masai."
    ),
    "availability": (
        "Narendra is actively looking for opportunities in Data Analytics, Business "
        "Analytics, and AI Automation. Feel free to reach out via the Contact section."
    ),
    "default": (
        "I'm Narendra's portfolio assistant. You can ask me about his skills, projects, "
        "experience, certifications, or availability. For detailed queries, please use "
        "the Contact section to reach out directly."
    ),
}

# -----------------------------------------------------------------------------
# Resume Text — flat string used by ATS scorer and chatbot system prompt
# -----------------------------------------------------------------------------
RESUME_TEXT = """
Narendra Madanlal Fulwaria
Mumbai, Maharashtra | Phone: 9833607051
GitHub: https://github.com/Narendrafulwaria

PROFESSIONAL SUMMARY
Electronics & Telecommunication Engineering graduate with 6+ years of business
operations and retail management experience. Currently transitioning into Data Analytics,
Business Analytics, AI Automation and Generative AI. Skilled in Python, SQL, Excel,
Tableau, Power BI, Data Analysis and workflow automation using n8n. Proven track record
of driving business growth, managing teams, optimizing inventory, analyzing business
data and implementing customer retention strategies.

TECHNICAL SKILLS
Programming: Python, SQL, MySQL
Analytics: Pandas, NumPy, Data Cleaning, Data Visualization
BI Tools: Excel, Tableau, Power BI
Automation: n8n, Webhooks, AI Workflow Automation
Other: GitHub, Business Analytics, Inventory Analytics, CRM, Team Management

PROJECTS
AI Resume Analyzer Workflow
Built an AI-powered resume analysis workflow using n8n, webhooks and database integration.
Automated resume parsing, ATS analysis and recommendation generation.

Leave Management Automation System
Developed an automated leave management workflow integrating Telegram, Google Sheets and Gmail.
Automated leave request processing and notification management.

AI Leave Management Chatbot
Designed a chatbot-based HR automation solution to streamline employee leave applications
and workflow management.

Python Analytics Portfolio
Built Python projects covering data structures, business analytics, inventory management,
functions, modules and analytical problem solving.

SQL Analytics Portfolio
Developed SQL solutions using joins, subqueries, CTEs, aggregations and window functions
to solve business reporting and analytics problems.

PROFESSIONAL EXPERIENCE
Business Operations Manager | Bhawani Supermart | 2020 – Present
- Built and scaled a family-owned retail grocery business from inception.
- Increased daily customer footfall from 250 to 400 through targeted promotional campaigns.
- Achieved approximately 75% growth in daily sales through customer retention and loyalty initiatives.
- Managed procurement, inventory control, merchandising and replenishment operations.
- Led and supervised a team of 5 employees across customer service and store operations.
- Implemented data-driven pricing, seasonal promotions and stock optimization strategies.

Fresh Fruits & Vegetables Operations | 2023 – Present
- Established and managed a dedicated fruits and vegetables department.
- Tracked shelf life, spoilage rates and inventory turnover to reduce waste.
- Maintained fresh inventory availability while optimizing procurement costs.
- Improved visual merchandising and customer purchasing experience.

EDUCATION
Bachelor of Engineering (Electronics & Telecommunication)
Ramrao Adik Institute of Technology, Mumbai University (2019)
Higher Secondary Certificate (HSC) – Swami Vivekanand High School (2015)
Secondary School Certificate (SSC) – Adarsha Vidyalaya School (2013)

CERTIFICATIONS
AI Fundamentals & Ecosystem Mastery – Be10X
AI Product Building, Storytelling & Marketing – Be10X
AI Agents & Autonomous Systems – Be10X
Career Readiness Using AI – Be10X
AI Career Accelerator Program (6 Months) – Be10X (Certificate of Mastery)
Capstone Project – AI Career Accelerator Program – Be10X (Certificate of Mastery)
Cricket Analytics Advanced Masterclass – Mad About Sports & Rajasthan Royals (May 2023)
Data Analytics with AI & Generative AI – IIT Roorkee & Masai (In Progress)

KEY ACHIEVEMENTS
Successfully transitioned from business operations into Data Analytics and AI upskilling.
Built multiple GitHub projects demonstrating analytics, automation and SQL capabilities.
Managed end-to-end retail operations for over six years.
Led business growth initiatives that significantly improved customer acquisition and revenue.
"""
