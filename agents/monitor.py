import os
import requests
from agents.state import AgentState

class SchematronMonitorAgent:
    def __init__(self, schematron_dir="schematron"):
        self.schematron_dir = schematron_dir
        self.repo = "OpenPEPPOL/peppol-bis-invoice-3"
        self.file_path = "rules/sch/PEPPOL-EN16931-UBL.sch"
        os.makedirs(self.schematron_dir, exist_ok=True)

    def fetch_latest_version(self) -> str:
        """
        Fetches the latest release tag from GitHub.
        """
        try:
            url = f"https://api.github.com/api/v1/repos/{self.repo}/releases/latest"
            # Some versions of GitHub API/proxy might differ, fallback to public releases if needed
            response = requests.get(f"https://api.github.com/repos/{self.repo}/releases/latest", timeout=10)
            if response.status_code == 200:
                return response.json().get("tag_name", "unknown")
            return "unknown"
        except Exception as e:
            print(f"Error fetching version: {e}")
            return "unknown"

    def fetch_content(self, version="master") -> str:
        """
        Fetches the Schematron content from a specific branch or tag.
        """
        try:
            url = f"https://raw.githubusercontent.com/{self.repo}/{version}/{self.file_path}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.text
            return ""
        except Exception as e:
            print(f"Error fetching content: {e}")
            return ""

    def run(self, state: AgentState) -> AgentState:
        print("--- Schematron Monitor Agent (GitHub) ---")
        
        # 1. Fetch latest version from GitHub
        latest_version = self.fetch_latest_version()
        state["latest_version"] = latest_version
        
        # 2. Paths
        old_path = os.path.join(self.schematron_dir, "old_schematron.xml")
        new_path = os.path.join(self.schematron_dir, "new_schematron.xml")
        
        # 3. Load previous content from local file if exists
        try:
            if os.path.exists(new_path):
                with open(new_path, "r") as f:
                    state["schematron_content_old"] = f.read()
                    state["previous_version"] = "local_cache"
            else:
                # Fallback to a previous known release or dummy for first run
                state["schematron_content_old"] = ""
                state["previous_version"] = "none"
        except Exception as e:
            state["errors"] = state.get("errors", []) + [f"Error reading local cache: {e}"]

        # 4. Fetch real content for the latest version
        # If latest_version is 'unknown', fallback to master
        fetch_tag = latest_version if latest_version != "unknown" else "master"
        content_new = self.fetch_content(fetch_tag)
        
        if content_new:
            # Save to 'new_schematron.xml' for the next run's cache
            with open(new_path, "w") as f:
                f.write(content_new)
            state["schematron_content_new"] = content_new
            print(f"Fetched latest Schematron from GitHub ({fetch_tag}).")
        else:
            state["errors"] = state.get("errors", []) + ["Failed to fetch content from GitHub."]

        print(f"Monitor complete. Version: {state['latest_version']}")
        return state
