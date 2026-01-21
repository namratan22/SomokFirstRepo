"""
Simple test script - just transcript scraping and markdown
"""

from utils.transcript_scraper import get_video_transcript, format_transcript_for_markdown
from utils.file_manager import save_markdown
from datetime import datetime
import os

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
print(f"   Transcript length: {len(result['transcript'])} characters")
print(f"   Word count: ~{len(result['transcript'].split())} words\n")

# Step 2: Generate Markdown file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
markdown_file = f"outputs/test_transcript_{timestamp}.md"

print("📝 Generating Markdown file...")
markdown_content = format_transcript_for_markdown(result, title="Test Video Transcript")
os.makedirs("outputs", exist_ok=True)
save_markdown(markdown_content, markdown_file)
print(f"✅ Markdown saved: {markdown_file}\n")

# Step 3: Show preview
print("=" * 60)
print("📄 TRANSCRIPT PREVIEW (First 1000 characters)")
print("=" * 60)
print(result['transcript'][:1000])
if len(result['transcript']) > 1000:
    print(f"\n... [+{len(result['transcript']) - 1000} more characters]")
print("\n")

print("=" * 60)
print("✅ SUCCESS! Transcript scraped and saved!")
print("=" * 60)
print(f"\n📁 Generated file:")
print(f"   • {markdown_file}\n")
print("📊 Stats:")
print(f"   • Characters: {len(result['transcript'])}")
print(f"   • Words: ~{len(result['transcript'].split())}")
print(f"   • Lines: ~{result['transcript'].count('.') + result['transcript'].count('?') + result['transcript'].count('!')}\n")
