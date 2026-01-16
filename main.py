import argparse
from agents.graph import run_graph

def main():
    parser = argparse.ArgumentParser(description="Run Peppol Schematron Monitor Agent")
    parser.add_argument("--cli", action="store_true", help="Run in CLI mode without Streamlit")
    args = parser.parse_args()

    if args.cli:
        print("Starting CLI Monitoring...")
        result = run_graph()
        print("Monitoring Complete.")
        print(f"Report saved to: {result.get('report_path')}")
    else:
        print("Please run the Streamlit app using: streamlit run streamlit_app/app.py")

if __name__ == "__main__":
    main()
