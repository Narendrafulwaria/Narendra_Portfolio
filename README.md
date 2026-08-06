# Narendra Fulwaria | Portfolio Website

A modern, interactive portfolio website built with Streamlit showcasing Narendra Fulwaria's journey from Business Operations to Data Analytics, AI Automation, and Generative AI.

## 🚀 Features

- **Hero Section**: Eye-catching landing with 3D profile photo effect and call-to-action buttons
- **About Me**: Professional bio highlighting the transition from business operations to tech
- **Technical Skills**: Animated skill visualization with progress bars and radar charts
- **Projects Showcase**: Interactive cards displaying key projects with GitHub links
- **Professional Experience**: Timeline of 6+ years in business operations and retail management
- **Education**: Academic background in Electronics & Telecommunication Engineering
- **Certifications**: AI and Data Analytics certifications from Be10X and IIT Roorkee
- **Key Achievements**: Highlighted metrics and career milestones
- **GitHub Stats Dashboard**: Live GitHub profile stats and repository insights
- **LinkedIn Integration**: Professional networking connection
- **Blog Section**: Thought pieces and learnings from the tech journey
- **AI Chatbot**: "Ask Narendra" - Interactive chatbot trained on resume content
- **Resume ATS Widget**: Live demo of AI Resume Analyzer project

## 🛠️ Tech Stack

- **Frontend Framework**: Streamlit 1.60.0
- **Visualization**: Plotly 6.9.0
- **Machine Learning**: scikit-learn 1.5.0
- **AI/ML**: Groq 0.9.0
- **Additional Libraries**:
  - streamlit-option-menu
  - streamlit-lottie
  - streamlit-extras
  - requests
  - Pillow

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Narendrafulwaria/Narendra_Portfolio.git
   cd Narendra_Portfolio
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables** (optional)
   - Create a `.streamlit/secrets.toml` file for API keys
   - Add your OpenAI/Groq API key for the chatbot feature

## 🎯 Usage

Run the portfolio locally:

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
Narendra_Portfolio/
├── app.py                 # Main application entry point
├── requirements.txt       # Python dependencies
├── .streamlit/           # Streamlit configuration
├── assets/               # Static assets (images, fonts)
├── components/           # Reusable UI components
│   └── nav.py            # Navigation component
├── sections/             # Page sections
│   ├── hero.py          # Landing section
│   ├── about.py         # About me section
│   ├── skills.py        # Skills visualization
│   ├── projects.py      # Projects showcase
│   ├── experience.py    # Work experience
│   ├── education.py     # Education background
│   ├── certifications.py
│   ├── achievements.py
│   ├── github_stats.py  # GitHub integration
│   ├── linkedin.py
│   ├── blog.py
│   ├── chatbot.py       # AI chatbot
│   ├── ats_widget.py    # Resume analyzer demo
│   ├── contact.py
│   └── footer.py
└── utils/               # Utility functions
    └── styles.py        # Custom CSS styling
```

## 🌐 Deployment

This portfolio is deployed on **Streamlit Community Cloud** and connected to the GitHub repository. Any push to the main branch triggers automatic deployment.

- **Live URL**: [Add your Streamlit app URL here]
- **Repository**: https://github.com/Narendrafulwaria/Narendra_Portfolio

## 👤 About Narendra

Narendra Fulwaria is an Electronics & Telecommunication Engineering graduate with 6+ years of business operations experience, currently transitioning into Data Analytics, AI Automation, and Generative AI. He combines analytical thinking with practical business acumen to solve complex problems.

### Key Skills
- **Programming**: Python, SQL, MySQL
- **Analytics**: Pandas, NumPy, Data Visualization
- **BI Tools**: Excel, Tableau, Power BI
- **Automation**: n8n, Webhooks, AI Workflow Automation
- **Business**: Inventory Analytics, CRM, Team Management

## 📞 Contact

- **GitHub**: [Narendrafulwaria](https://github.com/Narendrafulwaria)
- **LinkedIn**: [Add LinkedIn profile URL]
- **Email**: [Add email address]
- **Location**: Mumbai, Maharashtra

## 📄 License

This project is open source and available for personal and commercial use.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

Built with ❤️ using Streamlit