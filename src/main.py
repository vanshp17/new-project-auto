# # Define paths and content
# template_path = 'C:\\Users\\admin\\Downloads\\resume_template.docx'
# output_path = 'C:\\Users\\admin\\Documents\\Vanshita RESUME\\Auto Custom Resume Generator\\output\\customized_resume.docx'


# main.py

from job_parser import extract_keywords_from_jd, generate_summary_from_keywords
from resume_updater import update_resume

def main():
    # Job description example (update as needed)
    job_description = """
    Seeking a Data Scientist with expertise in Python, SQL, machine learning, and data visualization.
    Experience with large datasets and predictive modeling is a plus.
    """

# Extract keywords and other details from the job description
    keywords, job_role = extract_keywords_from_jd(job_description)  # Returns keywords and job role separately
    summary = generate_summary_from_keywords(keywords, job_role)  # Generate a summary based on extracted info

    # File paths
    template_path = 'C:\\Users\\admin\\Downloads\\resume_template.docx'
    output_path = 'C:\\Users\\admin\\Documents\\Vanshita RESUME\\Auto Custom Resume Generator\\output\\custom_resume.docx'

    # Update the resume template with custom summary
    update_resume(template_path, output_path, summary)
    print("Resume has been updated successfully!")

# Run the main function
if __name__ == "__main__":
    main()

