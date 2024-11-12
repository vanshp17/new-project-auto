# job_parser.py

import spacy

# Load the NLP model for keyword extraction
nlp = spacy.load("en_core_web_sm")

def extract_keywords_from_jd(job_description):
    """
    Extracts keywords from the given job description based on parts of speech.
    
    Args:
        job_description (str): The job description text.
    
    Returns:
        set: A set of keywords extracted from the job description.
    """
    doc = nlp(job_description)
    keywords = {token.text.lower() for token in doc if token.pos_ in {"NOUN", "PROPN", "ADJ"}}
    return keywords

def generate_summary_from_keywords(keywords):
    """
    Generates a professional summary based on extracted keywords.
    
    Args:
        keywords (set): A set of keywords to include in the summary.
    
    Returns:
        str: A custom summary string.
    """
    summary = f"Experienced professional focused on {', '.join(keywords)}."
    summary += " Skilled in delivering solutions in data-driven environments."
    return summary
