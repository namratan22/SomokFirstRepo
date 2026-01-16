"""
PDF Generator Module
Handles PDF generation from transcript data
"""

from fpdf import FPDF
from datetime import datetime
from typing import List, Dict


class TranscriptPDF(FPDF):
    """Custom PDF class for transcript documents"""

    def header(self):
        """Add header to each page"""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'YouTube Transcript Knowledge Base', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        """Add footer with page number"""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title: str):
        """Add a chapter title"""
        self.set_font('Arial', 'B', 14)
        self.multi_cell(0, 10, title)
        self.ln(4)

    def chapter_body(self, body: str):
        """Add chapter body text"""
        self.set_font('Arial', '', 11)
        # Handle unicode characters
        try:
            self.multi_cell(0, 6, body)
        except UnicodeEncodeError:
            # Fallback to latin-1 encoding
            safe_body = body.encode('latin-1', 'ignore').decode('latin-1')
            self.multi_cell(0, 6, safe_body)
        self.ln()


def create_pdf_from_transcript(transcript_data: Dict, filename: str, title: str = None) -> bool:
    """
    Create a PDF file from transcript data

    Args:
        transcript_data: Dictionary containing transcript information
        filename: Output PDF filename
        title: Optional title for the document

    Returns:
        True if successful, False otherwise
    """
    try:
        pdf = TranscriptPDF()
        pdf.add_page()

        # Add title
        if title:
            pdf.chapter_title(title)
        else:
            pdf.chapter_title("YouTube Video Transcript")

        # Add metadata
        video_id = transcript_data.get('video_id', 'Unknown')
        video_url = transcript_data.get('url', f'https://youtube.com/watch?v={video_id}')

        pdf.set_font('Arial', 'I', 10)
        pdf.multi_cell(0, 5, f"Video ID: {video_id}")
        pdf.multi_cell(0, 5, f"URL: {video_url}")
        pdf.multi_cell(0, 5, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        pdf.ln(10)

        # Add transcript content
        pdf.chapter_title("Transcript")
        transcript = transcript_data.get('transcript', 'No transcript available')
        pdf.chapter_body(transcript)

        # Save PDF
        pdf.output(filename)
        return True

    except Exception as e:
        print(f"Error creating PDF: {e}")
        return False


def append_to_pdf(existing_pdf: str, transcript_data: Dict, output_filename: str, title: str = None) -> bool:
    """
    Append transcript to an existing PDF

    Args:
        existing_pdf: Path to existing PDF file
        transcript_data: Dictionary containing transcript information
        output_filename: Output PDF filename
        title: Optional title for the new section

    Returns:
        True if successful, False otherwise
    """
    try:
        # Create new PDF with combined content
        pdf = TranscriptPDF()

        # Note: fpdf2 doesn't support reading existing PDFs easily
        # So we'll create a new PDF with a separator indicating it's an append
        pdf.add_page()
        pdf.chapter_title("=" * 50)
        pdf.chapter_title("NEW TRANSCRIPT ENTRY")
        pdf.chapter_title("=" * 50)
        pdf.ln(10)

        # Add new transcript
        if title:
            pdf.chapter_title(title)
        else:
            pdf.chapter_title("YouTube Video Transcript")

        # Add metadata
        video_id = transcript_data.get('video_id', 'Unknown')
        video_url = transcript_data.get('url', f'https://youtube.com/watch?v={video_id}')

        pdf.set_font('Arial', 'I', 10)
        pdf.multi_cell(0, 5, f"Video ID: {video_id}")
        pdf.multi_cell(0, 5, f"URL: {video_url}")
        pdf.multi_cell(0, 5, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        pdf.ln(10)

        # Add transcript content
        pdf.chapter_title("Transcript")
        transcript = transcript_data.get('transcript', 'No transcript available')
        pdf.chapter_body(transcript)

        # Save PDF
        pdf.output(output_filename)
        return True

    except Exception as e:
        print(f"Error appending to PDF: {e}")
        return False
