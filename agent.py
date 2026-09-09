from pdf_loader import load_pdf
from chunking import chunk_text


def main():
    pdf_path = "data/rlm_sample_knowledge.pdf"

    print("Loading PDF...")

    text = load_pdf(pdf_path)

    print("PDF loaded successfully!")
    print("Total characters:", len(text))

    print("\nCreating chunks...")

    chunks = chunk_text(text)

    print("Total chunks:", len(chunks))

    for i, chunk in enumerate(chunks, start=1):
        print("\n" + "=" * 60)
        print(f"CHUNK {i}")
        print("=" * 60)
        print(chunk[:500])


if __name__ == "__main__":
    main()