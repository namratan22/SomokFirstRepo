"""
YouTube Transcript Knowledge Base Tool
A simple web application to scrape YouTube transcripts and build a knowledge repository
"""

import streamlit as st
import os
from datetime import datetime
from utils import (
    get_video_transcript,
    format_transcript_for_markdown,
    create_pdf_from_transcript,
    save_markdown,
    append_to_markdown,
    add_transcript_entry,
    get_transcript_count,
    get_latest_files,
    load_knowledge_base
)


# Page configuration
st.set_page_config(
    page_title="YouTube Transcript Knowledge Base",
    page_icon="📚",
    layout="wide"
)


def main():
    """Main application function"""

    # Header
    st.title("📚 YouTube Transcript Knowledge Base")
    st.markdown("Build your personal knowledge repository from YouTube videos")
    st.markdown("---")

    # Sidebar with statistics
    with st.sidebar:
        st.header("📊 Statistics")
        transcript_count = get_transcript_count()
        st.metric("Total Transcripts", transcript_count)

        st.markdown("---")
        st.header("📖 About")
        st.info(
            "This tool helps you build a knowledge base by scraping YouTube video transcripts. "
            "Simply paste a YouTube URL and choose to create a new document or append to existing ones."
        )

        st.markdown("---")
        st.header("📝 Knowledge Base")
        if transcript_count > 0:
            entries = load_knowledge_base()
            with st.expander("View all entries"):
                for idx, entry in enumerate(entries, 1):
                    st.write(f"**{idx}. {entry.get('title', 'Untitled')}**")
                    st.caption(f"Video ID: {entry['video_id']}")
                    st.caption(f"Added: {entry['created_at'][:10]}")
                    st.markdown("---")

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("🎬 Add New Transcript")

        # URL input
        video_url = st.text_input(
            "YouTube URL",
            placeholder="https://www.youtube.com/watch?v=...",
            help="Paste the full YouTube video URL here"
        )

        # Optional title
        custom_title = st.text_input(
            "Title (Optional)",
            placeholder="Give this transcript a custom title",
            help="Leave empty to use default title"
        )

    with col2:
        st.header("⚙️ Options")

        # File handling option
        if transcript_count > 0:
            file_option = st.radio(
                "File Handling",
                ["Create new files", "Append to existing files"],
                help="Choose whether to create new PDF/Markdown files or append to the latest ones"
            )
        else:
            file_option = "Create new files"
            st.info("First transcript will create new files")

    # Process button
    st.markdown("---")

    if st.button("🚀 Scrape Transcript", type="primary", use_container_width=True):
        if not video_url:
            st.error("⚠️ Please enter a YouTube URL")
        else:
            with st.spinner("Fetching transcript..."):
                # Get transcript
                result = get_video_transcript(video_url)

                if not result['success']:
                    st.error(f"❌ Error: {result['error']}")
                else:
                    video_id = result['video_id']
                    st.success(f"✅ Transcript fetched successfully! (Video ID: {video_id})")

                    # Generate filenames
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

                    if file_option == "Create new files":
                        # Create new files
                        markdown_file = f"outputs/transcript_{timestamp}.md"
                        pdf_file = f"outputs/transcript_{timestamp}.pdf"

                        # Format and save markdown
                        markdown_content = format_transcript_for_markdown(
                            result,
                            title=custom_title
                        )
                        save_markdown(markdown_content, markdown_file)

                        # Create PDF
                        create_pdf_from_transcript(result, pdf_file, title=custom_title)

                        # Add to knowledge base
                        add_transcript_entry(
                            video_id,
                            video_url,
                            markdown_file,
                            pdf_file,
                            title=custom_title
                        )

                        st.success(f"✅ New files created!")

                    else:
                        # Append to existing files
                        latest_files = get_latest_files()

                        # Append to markdown
                        markdown_content = format_transcript_for_markdown(
                            result,
                            title=custom_title
                        )
                        append_to_markdown(markdown_content, latest_files['markdown'])

                        # For PDF, we'll create a new one with the appended content
                        # (since fpdf2 doesn't easily support modifying existing PDFs)
                        timestamp_suffix = datetime.now().strftime("%Y%m%d_%H%M%S")
                        new_pdf_file = latest_files['pdf'].replace('.pdf', f'_updated_{timestamp_suffix}.pdf')
                        create_pdf_from_transcript(result, new_pdf_file, title=custom_title)

                        # Update knowledge base
                        add_transcript_entry(
                            video_id,
                            video_url,
                            latest_files['markdown'],
                            new_pdf_file,
                            title=custom_title
                        )

                        markdown_file = latest_files['markdown']
                        pdf_file = new_pdf_file

                        st.success(f"✅ Content appended to existing files!")

                    # Display download buttons
                    st.markdown("---")
                    st.subheader("📥 Download Files")

                    col_a, col_b = st.columns(2)

                    with col_a:
                        # Markdown download
                        with open(markdown_file, 'r', encoding='utf-8') as f:
                            markdown_data = f.read()
                        st.download_button(
                            label="📄 Download Markdown",
                            data=markdown_data,
                            file_name=os.path.basename(markdown_file),
                            mime="text/markdown"
                        )

                    with col_b:
                        # PDF download
                        with open(pdf_file, 'rb') as f:
                            pdf_data = f.read()
                        st.download_button(
                            label="📕 Download PDF",
                            data=pdf_data,
                            file_name=os.path.basename(pdf_file),
                            mime="application/pdf"
                        )

                    # Show preview
                    st.markdown("---")
                    st.subheader("👁️ Transcript Preview")
                    with st.expander("Click to view transcript", expanded=True):
                        st.text_area(
                            "Transcript Content",
                            result['transcript'],
                            height=300,
                            disabled=True
                        )

    # Footer
    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit • All files are saved in the 'outputs' folder")


if __name__ == "__main__":
    # Ensure outputs directory exists
    os.makedirs("outputs", exist_ok=True)
    main()
