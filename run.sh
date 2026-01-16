#!/bin/bash

# YouTube Transcript Knowledge Base - Startup Script

echo "Starting YouTube Transcript Knowledge Base Tool..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

# Check if dependencies are installed
if ! python3 -c "import streamlit" &> /dev/null; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

# Create outputs directory if it doesn't exist
mkdir -p outputs

# Run the application
echo "Opening web browser..."
echo "Access the app at: http://localhost:8501"
echo ""
streamlit run app.py
