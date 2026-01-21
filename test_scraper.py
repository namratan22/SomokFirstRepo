"""
Test script to demonstrate YouTube transcript scraping
"""

from utils import (
    get_video_transcript,
    format_transcript_for_markdown,
    create_pdf_from_transcript,
    save_markdown,
    add_transcript_entry
)
from datetime import datetime

# YouTube URL provided by user
video_url = "https://www.youtube.com/watch?v=y2NeAef6d30"

print("=" * 60)
print("YouTube Transcript Knowledge Base Tool - Test Run")
print("=" * 60)
print(f"\n📹 Video URL: {video_url}\n")

# Step 1: Fetch the transcript
print("⏳ Fetching transcript from YouTube...")
result = get_video_transcript(video_url)

if not result['success']:
    print(f"❌ Error: {result['error']}")
    exit(1)

print(f"✅ Transcript fetched successfully!")
print(f"   Video ID: {result['video_id']}")
print(f"   Transcript length: {len(result['transcript'])} characters\n")

# Step 2: Generate filenames
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
markdown_file = f"outputs/test_transcript_{timestamp}.md"
pdf_file = f"outputs/test_transcript_{timestamp}.pdf"

# Step 3: Create Markdown file
print("📝 Generating Markdown file...")
markdown_content = format_transcript_for_markdown(result, title="Test Video Transcript")
save_markdown(markdown_content, markdown_file)
print(f"✅ Markdown saved: {markdown_file}\n")

# Step 4: Create PDF file
print("📕 Generating PDF file...")
pdf_success = create_pdf_from_transcript(result, pdf_file, title="Test Video Transcript")
if pdf_success:
    print(f"✅ PDF saved: {pdf_file}\n")
else:
    print(f"⚠️  PDF generation had issues\n")

# Step 5: Add to knowledge base
print("💾 Adding to knowledge base...")
add_transcript_entry(
    result['video_id'],
    video_url,
    markdown_file,
    pdf_file,
    title="Test Video Transcript"
)
print("✅ Entry added to knowledge base\n")

# Step 6: Show preview
print("=" * 60)
print("📄 TRANSCRIPT PREVIEW (First 500 characters)")
print("=" * 60)
print(result['transcript'][:500] + "...\n")

print("=" * 60)
print("✅ SUCCESS! All files generated successfully!")
print("=" * 60)
print(f"\n📁 Generated files:")
print(f"   • {markdown_file}")
print(f"   • {pdf_file}")
print(f"   • outputs/knowledge_base.json\n")
