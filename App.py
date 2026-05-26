""" AI appplication to justify expense and billing """

import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load env variables from env file
load_dotenv()

# Configure Google Gemini API 
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# Page configuration set up
st.set_page_config(
    page_title = "Expense Justification Assistant",
    layout = "wide",
    page_icon = "💰"
)

def generate_justification(expense_type, amount, description, role, department, company_context, additional_context):
    """ 
    Generates expense explanation using Google Gemini

    Parameters:
    - expense_type: Type of expenditure (conference, training, software, raw materials etc.)
    - amount: dollar value
    - description: Brief description of the expense
    - role: User's job role
    - department: User's department
    - company_context: Company's size, industry etc.
    - additional_context: Any additional relevant information

    Returns:
    - Generated email text

    """

    #Construct the promtp for Gemini
    prompt = f"""You are a n expert bsuiness communicator helping an employee write a compelling expense approval request.
    
    Generate a professional email requesting approval for the following expense:

    **Expense Details:**
    - Type: {expense_type}
    - Amount: {amount}
    - Description: {description}
    - Employee Role: {role}
    - Department: {department}
    - Company Context: {company_context}
    - Additional Context: {additional_context}

    **Your Task:**
    1. Write a professional email witha clear subject line
    2. Explain the business value ROI
    3. Address potential concerns
    4. Include specific, quantified benefits where possible
    5. Keep it concise but pursuasive (around 200 - 300 words)
    6. Use professional, collaborative tone

    Format the output as:
    Subject: [compelling subject line]
    [Email Body]

    Make the business case strong, data driven and focused on impact 
    """

    try:
        # Call Gemini API since fast, free, and perfect for text generation
        model = genai.GenerativeModel('gemini-2.5-flash')        
        
        # Generate content
        response = model.generate_content(prompt)

        # Extract the generated text
        generated_text = response.text
        return generated_text
    
    except Exception as e:
        return f"Error generating jsutification: {str(e)}\n\nPlease check your Google Gemini API Key and try again"
    

# ======= STRAMLIT UI =======

# Header
st.title("Expense Explanation Assitant")
st.markdown("Transform basic expense info into compelling business case")
st.markdown("---")


# Instructions
with st.expander("How to use this tool?"):
    st.markdown(
        """
        1. Fill in your expense details
        2. Provide context about your role and company
        3. Click "Generate email"
        4. Review and customise the generated email
        5. Copy and send to your manager

        **Tip:** The more context your provide, the better the justofication will be.
        """
    )

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Expense Details")

    # Expense type dropdown
    expense_type = st.selectbox(
        "Expense Type",
        [
            "Conference Registration", "Software Subscription", "Professional Development Course",
            "Equipment/Hardware", "Training Program", "Certification", "Other"
        ],
        help = "Select the category that best fits your expense"
    )

    # Amount input
    amount = st.number_input(
        "Amount ($)",
        min_value = 0,
        value = 1000,
        step = 100,
        help = "Enter the total cost of expense"
    )

    # Description
    description = st.text_area(
        "Description",
        help = "Brief description of what the expense is for",
        height = 100
    )

    with col2:
        st.subheader("Your Context")

        # Role
        role = st.text_input(
            "Your Role",
            placeholder = "e.g., Product Analyst, Software Engineer",
            help = "Your current job title"
        )

        # Department
        department = st.text_input(
            "Department",
            placeholder = "e.g., Product, R&D, Engineering, Analytics",
            help = "Which department do you work in?"
        )

        # Company Context
        company_context = st.text_input(
            "Company Context",
            placeholder = "e.g., Mid-market SaaS company, 500 employees",
            help = "Brief context about your company (size, industry, stage)"
        )

    # Additional Context (full width)
    st.subheader("Additional Context (optional)")
    additional_context = st.text_area(
        "Any additional information that would help justify this expanse?",
        placeholder = "e.g., Currently working on AI feature integration, team has skill gap in this area, competing priorities",
        help = "Provide any relevant context: current projects, team needs, strategic initiatives, etc.",
        height = 100
    )

    # Generate Button
    st.markdown("----")
    if st.button("Generate Response", type = "primary", use_container_width = True):
        # Validation
        if not description or not role or not department:
            st.error("Please fill out all details")
        elif not os.getenv("GOOGLE_API_KEY"):
            st.error("Google API key not found. Please add GOOGLE_API_KEY to your .env file")
        else:
            # Show loading spinner
            with st.spinner("Generating your email"):
                result = generate_justification(
                    expense_type, amount, description, role, department, company_context, 
                    additional_context
                )
        
        # Display Result
        st.markdown("----")
        st.subheader("Genearted Email")
        st.markdown(result)

        #Copy button
        st.code(result, language= None)
        st.caption("Click the copy button to copy the mail draft")

        #Success message
        st.success("Justification generated! Review, customize if needed, and send")

    # Footer
    st.markdown("----")
    st.markdown("""
                <div style = 'text-align: center; color: #666; font-size 0.9em;'>
                Powered by Google Gemini | <a href='https://github.com/svd110/expense-justification-generator'>
                View on GitHub </a>
                </div>
                """, unsafe_allow_html = True)
