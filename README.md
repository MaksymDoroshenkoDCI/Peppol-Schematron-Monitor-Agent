# Agentic Peppol Monitor

An AI agent system to monitor Peppol schematron changes, analyze their impact on mappings, and report findings.

## Structure

- `agents/`: LangGraph agent implementations.
- `schematron/`: Schematron XML storage.
- `mappings/`: Integration mappings.
- `streamlit_app/`: UI for control and visualization.
- `utils/`: Helper functions.

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Run the UI: `streamlit run streamlit_app/app.py`
