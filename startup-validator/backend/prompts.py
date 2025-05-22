def get_prompt(idea):
    return f"""
    Act as a startup analyst. Analyze the startup idea below:
    
    Startup Idea: {idea}

    Provide the following:
    1. Market Analysis
    2. Potential Competitors
    3. SWOT Analysis
    4. Monetization Strategy
    5. MVP Feature Suggestions
    """
