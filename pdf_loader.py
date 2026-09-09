import fitz


def load_pdf(pdf_path):
    document = fitz.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text()

        pages.append(
            f"\n--- PAGE {page_number} ---\n{text}"
        )

    document.close()

    return "\n".join(pages)