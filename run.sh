#!/bin/bash

# Automated PDF Marking System - Startup Script

echo "========================================"
echo "  Automated PDF Marking System"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if dependencies are installed
echo "Checking dependencies..."
if ! pip list | grep -i streamlit > /dev/null; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
    echo "Dependencies installed."
    echo ""
fi

# Launch the application
echo "Launching Automated PDF Marking System..."
echo ""
echo "The application will open in your browser at: http://localhost:8501"
echo "Press Ctrl+C to stop the server."
echo ""

streamlit run app.py
