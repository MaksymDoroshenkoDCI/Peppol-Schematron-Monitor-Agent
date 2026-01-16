import json
import os
from agents.state import AgentState

class MappingImpactAgent:
    def __init__(self, mappings_dir="mappings"):
        self.mappings_dir = mappings_dir
        os.makedirs(self.mappings_dir, exist_ok=True)

    def run(self, state: AgentState) -> AgentState:
        print("--- Mapping Impact Agent ---")
        
        diff_results = state.get("diff_results", [])
        impact_analysis = []
        
        # Load all mappings
        mappings = []
        try:
            for filename in os.listdir(self.mappings_dir):
                if filename.endswith(".json"):
                    with open(os.path.join(self.mappings_dir, filename), 'r') as f:
                        mappings.append({
                            "file": filename,
                            "content": json.load(f)
                        })
        except Exception as e:
            state["errors"] = state.get("errors", []) + [f"Error loading mappings: {e}"]
        
        # Simple analysis: Check if changed node names appear in mappings
        # This is a heuristic for the PoC.
        
        for diff in diff_results:
            diff_details = diff.get("details", "")
            
            # Very naive string matching for PoC
            for mapping in mappings:
                mapping_str = json.dumps(mapping["content"])
                
                # Check for broad match (real logic would parse XPath/IDs)
                # Here we assume diff details contain some element names
                
                # TODO: Improve this logic based on actual xmldiff output structure
                # For now, we flag the mapping if any part of it is 'touched'.
                
                # Let's assume we find a "warning"
                pass 
                
        # Mocking finding an impact for demonstration
        if diff_results:
            impact_analysis.append({
                "mapping_file": "order_mapping.json",
                "affected_field": "cbc:ID",
                "severity": "WARNING",
                "reason": "Schematron rule changed for ID field."
            })
            
        state["impact_analysis"] = impact_analysis
        print(f"Impact Analysis complete. Found {len(impact_analysis)} potential impacts.")
        return state
