# 📁 Repository Setup Guide

## Step 1: Create Your Profile README

1. Create a new repository named **exactly** `[your-username]` (same as your GitHub username)
   - Example: If your username is `swatisahai`, create repo named `swatisahai`
2. Make it **public**
3. Initialize with README
4. Copy the content from `PROFILE_README.md` into that README
5. Replace placeholders:
   - `[your-linkedin-url]` with your actual LinkedIn
   - Add your portfolio URL once live

**Result:** Your profile README will display on your GitHub homepage automatically!

---

## Step 2: Create Your Project Repository

### Repository Name
`expense-justification-generator` 
(or `ai-expense-assistant` - keep it descriptive)

### Repository Structure
```
expense-justification-generator/
│
├── README.md                   # Main project documentation (use PROJECT_README.md)
├── .gitignore                  # Python, env files
├── requirements.txt            # Python dependencies
├── .env.example                # Template for environment variables
│
├── app.py                      # Main Streamlit application
│
├── src/
│   ├── __init__.py
│   ├── prompt_templates.py    # LLM prompt engineering
│   ├── expense_processor.py   # Input validation & processing
│   ├── email_generator.py     # Email formatting logic
│   └── config.py              # Configuration constants
│
├── docs/
│   ├── architecture.md        # Technical architecture details
│   ├── product_case_study.md  # PM-focused writeup
│   └── images/                # Architecture diagrams
│       └── system_flow.png
│
├── tests/
│   ├── __init__.py
│   └── test_expense_processor.py
│
└── examples/
    └── sample_outputs.md      # Example inputs/outputs
```

---

## Step 3: Essential Files to Create

### requirements.txt
```
streamlit==1.28.0
openai==1.3.0
python-dotenv==1.0.0
langchain==0.0.335
pydantic==2.4.0
```

### .gitignore
```
# Environment
.env
.venv/
venv/
ENV/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# IDEs
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Streamlit
.streamlit/secrets.toml
```

### .env.example
```
# Copy this to .env and add your actual API key
OPENAI_API_KEY=your_openai_api_key_here
```

---

## Step 4: First Commit Checklist

Before you push your first version:

✅ **README.md** - Clear, comprehensive (use PROJECT_README.md template)  
✅ **LICENSE** - Add MIT license  
✅ **requirements.txt** - All dependencies listed  
✅ **.gitignore** - Protect sensitive files  
✅ **.env.example** - Template for setup  
✅ **Basic app.py** - Even if just a skeleton with comments  

**Pro tip:** Add a screenshot or demo GIF to README once you have UI working!

---

## Step 5: Make It Discoverable

### GitHub Topics (Add to repository settings)
- `artificial-intelligence`
- `product-management`
- `openai`
- `streamlit`
- `python`
- `nlp`
- `expense-management`

### Repository Description (One-liner)
"AI-powered tool that generates persuasive business justifications for expense approvals using GPT-4"

---

## Step 6: Pin Your Best Repositories

On your GitHub profile, **pin**:
1. ✅ This AI project (expense-justification-generator)
2. ✅ Your group project when ready (Smart Meeting Prep Assistant)
3. ✅ Any other impressive projects (dashboards, data analysis)

**Aim for 3-4 pinned repos** that show range: AI/ML + data + product thinking

---

## Next Steps After Setup

1. **Get the skeleton code working** - Basic Streamlit UI + OpenAI API call
2. **Deploy a live demo** - Streamlit Cloud is free and takes 5 minutes
3. **Write the product case study** - Goes in `docs/product_case_study.md`
4. **Add to your resume** - Link to both repo and live demo

---

## 🎯 What Recruiters Will See

When they visit your GitHub profile:

1. **Profile README** - Professional summary, tech stack, links
2. **Pinned repos** - Your best work front and center
3. **Green contribution graph** - Shows consistent activity
4. **Project READMEs** - Detailed, well-documented work
5. **Live demos** - Click and interact with your projects

**This positions you as someone who ships real products, not just completes assignments.**

---

## Questions Before You Start?

- Do you want help with the basic `app.py` skeleton?
- Need help setting up Streamlit Cloud for deployment?
- Want to create the architecture diagram?

Let me know what piece you want to tackle first!
