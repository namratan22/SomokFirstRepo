# YouTube Transcript Knowledge Base Tool

A simple, powerful web application that allows you to build a personal knowledge repository by scraping YouTube video transcripts. Save transcripts as both Markdown and PDF formats with just a click!

## Features

- **Simple Web Interface**: Clean, intuitive browser-based UI
- **One-Click Scraping**: Just paste a YouTube URL and click a button
- **Multiple Formats**: Automatically generates both Markdown and PDF files
- **Flexible Storage**: Create new files or append to existing ones
- **Knowledge Base Tracking**: Keeps track of all scraped transcripts
- **Download Options**: Instantly download generated files
- **Preview**: View transcripts before downloading
- **Statistics Dashboard**: See your knowledge base grow

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository** (or download the files):
   ```bash
   git clone <repository-url>
   cd SomokFirstRepo
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the web application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**:
   - The app will automatically open in your default browser
   - If not, navigate to `http://localhost:8501`

3. **Start scraping**:
   - Paste a YouTube URL
   - (Optional) Add a custom title
   - Choose to create new files or append to existing ones
   - Click "Scrape Transcript"
   - Download your files!

## How It Works

### First Time Usage

1. Paste a YouTube video URL
2. The tool will scrape the transcript
3. Creates new Markdown and PDF files in the `outputs` folder
4. Adds the entry to your knowledge base

### Subsequent Usage

You have two options:

1. **Create New Files**: Generate separate Markdown and PDF files for each video
2. **Append to Existing**: Add new transcripts to your existing Markdown file and create an updated PDF

## Project Structure

```
SomokFirstRepo/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── utils/                  # Utility modules
│   ├── __init__.py
│   ├── transcript_scraper.py  # YouTube transcript fetching
│   ├── pdf_generator.py       # PDF creation
│   └── file_manager.py        # File operations and tracking
└── outputs/                # Generated files (auto-created)
    ├── transcript_*.md     # Markdown files
    ├── transcript_*.pdf    # PDF files
    └── knowledge_base.json # Tracking database
```

## Usage Examples

### Example 1: Single Video

```
URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Title: "My First Transcript"
Option: Create new files

Result:
- outputs/transcript_20260116_123456.md
- outputs/transcript_20260116_123456.pdf
```

### Example 2: Building a Knowledge Base

```
Video 1: Create new files
Video 2: Append to existing files
Video 3: Append to existing files

Result:
- One Markdown file with all three transcripts
- Three PDF files (one for each video)
- All tracked in knowledge_base.json
```

## Features in Detail

### Markdown Output

- Clean, readable format
- Includes video metadata (ID, URL)
- Easy to edit and search
- Perfect for note-taking apps

### PDF Output

- Professional formatting
- Automatic page numbering
- Chapter-style layout
- Easy to share and archive

### Knowledge Base

- JSON database of all transcripts
- Tracks video IDs, URLs, files, and timestamps
- View history in the sidebar
- Never lose track of your sources

## Troubleshooting

### "No transcript found"

Some YouTube videos don't have transcripts available. Try:
- Videos with closed captions
- Educational content
- Popular channels

### "Transcripts are disabled"

The video owner has disabled transcripts. Try another video.

### Installation Issues

If you encounter issues installing dependencies:

```bash
# Upgrade pip first
pip install --upgrade pip

# Install dependencies one by one
pip install streamlit
pip install youtube-transcript-api
pip install fpdf2
pip install python-dotenv
```

## Requirements

All dependencies are listed in `requirements.txt`:

- **streamlit**: Web interface framework
- **youtube-transcript-api**: Fetches YouTube transcripts
- **fpdf2**: PDF generation library
- **python-dotenv**: Environment variable management

## Tips for Best Results

1. **Use descriptive titles**: Makes it easier to find transcripts later
2. **Organize by topic**: Use the append feature to group related videos
3. **Regular backups**: Copy your `outputs` folder regularly
4. **Educational content**: Works best with videos that have good captions

## Future Enhancements

Possible features to add:
- Search functionality across all transcripts
- Topic categorization and tagging
- Export to other formats (Word, HTML)
- Batch processing multiple URLs
- AI-powered summarization
- Timestamp preservation

## License

This project is open source and available for personal and educational use.

## Support

If you encounter any issues:
1. Check the Troubleshooting section
2. Ensure all dependencies are installed correctly
3. Verify the YouTube URL is valid and has transcripts available

## Credits

Built with:
- [Streamlit](https://streamlit.io/) - Web framework
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) - Transcript fetching
- [fpdf2](https://github.com/py-pdf/fpdf2) - PDF generation

---

Happy learning! Build your knowledge base one video at a time.
