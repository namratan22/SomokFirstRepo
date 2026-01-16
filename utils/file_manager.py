"""
File Manager Module
Handles file operations for markdown and tracking
"""

import os
import json
from datetime import datetime
from typing import Dict, List


KNOWLEDGE_BASE_FILE = "outputs/knowledge_base.json"


def save_markdown(content: str, filename: str) -> bool:
    """
    Save content to a markdown file

    Args:
        content: Markdown content to save
        filename: Output filename

    Returns:
        True if successful, False otherwise
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error saving markdown: {e}")
        return False


def append_to_markdown(content: str, filename: str) -> bool:
    """
    Append content to an existing markdown file

    Args:
        content: Markdown content to append
        filename: Target filename

    Returns:
        True if successful, False otherwise
    """
    try:
        separator = "\n\n" + "="*80 + "\n\n"
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(separator)
            f.write(content)
        return True
    except Exception as e:
        print(f"Error appending to markdown: {e}")
        return False


def load_knowledge_base() -> List[Dict]:
    """
    Load the knowledge base tracking file

    Returns:
        List of transcript entries
    """
    if not os.path.exists(KNOWLEDGE_BASE_FILE):
        return []

    try:
        with open(KNOWLEDGE_BASE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading knowledge base: {e}")
        return []


def save_knowledge_base(entries: List[Dict]) -> bool:
    """
    Save the knowledge base tracking file

    Args:
        entries: List of transcript entries

    Returns:
        True if successful, False otherwise
    """
    try:
        os.makedirs(os.path.dirname(KNOWLEDGE_BASE_FILE), exist_ok=True)
        with open(KNOWLEDGE_BASE_FILE, 'w', encoding='utf-8') as f:
            json.dump(entries, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving knowledge base: {e}")
        return False


def add_transcript_entry(video_id: str, url: str, markdown_file: str, pdf_file: str, title: str = None) -> bool:
    """
    Add a new transcript entry to the knowledge base

    Args:
        video_id: YouTube video ID
        url: YouTube video URL
        markdown_file: Path to markdown file
        pdf_file: Path to PDF file
        title: Optional title

    Returns:
        True if successful, False otherwise
    """
    entries = load_knowledge_base()

    new_entry = {
        'video_id': video_id,
        'url': url,
        'title': title,
        'markdown_file': markdown_file,
        'pdf_file': pdf_file,
        'created_at': datetime.now().isoformat()
    }

    entries.append(new_entry)
    return save_knowledge_base(entries)


def get_transcript_count() -> int:
    """
    Get the total number of transcripts in the knowledge base

    Returns:
        Number of transcripts
    """
    return len(load_knowledge_base())


def get_latest_files() -> Dict[str, str]:
    """
    Get the paths to the latest markdown and PDF files

    Returns:
        Dictionary with 'markdown' and 'pdf' keys
    """
    entries = load_knowledge_base()
    if not entries:
        return {'markdown': None, 'pdf': None}

    latest = entries[-1]
    return {
        'markdown': latest.get('markdown_file'),
        'pdf': latest.get('pdf_file')
    }
