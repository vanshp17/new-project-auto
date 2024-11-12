# resume_updater.py

from docx import Document

def update_resume(template_path, output_path, summary):
    """
    Updates the resume template with a custom summary.
    
    Args:
        template_path (str): Path to the resume template DOCX file.
        output_path (str): Path where the updated resume will be saved.
        summary (str): Custom summary to insert into the resume.
    """
    doc = Document(template_path)

    for paragraph in doc.paragraphs:
        if "{{ summary }}" in paragraph.text:
            paragraph.text = paragraph.text.replace("{{ summary }}", summary)

    doc.save(output_path)
