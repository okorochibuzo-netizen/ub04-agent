from PyPDF2 import PdfReader, PdfWriter

INPUT_PDF = "ub04_template.pdf"
OUTPUT_PDF = "ub04_updated.pdf"

def update_pdf(fields):
    reader = PdfReader(INPUT_PDF)
    writer = PdfWriter()

    page = reader.pages[0]
    writer.add_page(page)

    writer.update_page_form_field_values(writer.pages[0], fields)

    with open(OUTPUT_PDF, "wb") as f:
        writer.write(f)

    print("PDF updated successfully!")

if __name__ == "__main__":
    # Example values (ChatGPT Agent will replace these)
    fields = {
        "PatientName": "Maria Gonzalez",
        "StatementFrom": "03/01/2026",
        "StatementThrough": "03/31/2026",
        "TotalCharges": "2450"
    }

    update_pdf(fields)
