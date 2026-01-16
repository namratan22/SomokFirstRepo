# Quick Start Guide

Get up and running in 3 simple steps!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- Streamlit (web framework)
- youtube-transcript-api (transcript fetcher)
- fpdf2 (PDF generator)
- python-dotenv (environment management)

## Step 2: Run the Application

**Option A - Use the startup script (Linux/Mac):**
```bash
./run.sh
```

**Option B - Use the startup script (Windows):**
```bash
run.bat
```

**Option C - Run directly:**
```bash
streamlit run app.py
```

## Step 3: Use the Tool

1. Your browser will open automatically to `http://localhost:8501`
2. Paste a YouTube URL (e.g., `https://www.youtube.com/watch?v=dQw4w9WgXcQ`)
3. (Optional) Add a custom title
4. Click "Scrape Transcript"
5. Download your Markdown and PDF files!

## Example YouTube URLs to Try

Here are some educational videos with transcripts you can test:

- TED Talks: `https://www.youtube.com/watch?v=...`
- Educational channels (Crash Course, Khan Academy, etc.)
- Conference talks
- Tutorial videos

## Where Are My Files?

All generated files are saved in the `outputs/` folder:
- `transcript_*.md` - Markdown files
- `transcript_*.pdf` - PDF files
- `knowledge_base.json` - Tracking database

## Tips

- Videos must have transcripts/captions enabled
- Use descriptive titles to organize your knowledge base
- Use "Append to existing files" to group related videos
- The sidebar shows your knowledge base statistics

## Troubleshooting

**"No transcript found"** - The video doesn't have captions. Try another video.

**Module not found** - Run `pip install -r requirements.txt` again.

**Port already in use** - Close other Streamlit apps or use: `streamlit run app.py --server.port 8502`

## Next Steps

Check out the full [README.md](README.md) for:
- Detailed feature list
- Project structure
- Advanced usage
- Future enhancements

---

Happy scraping! Start building your knowledge base now!
