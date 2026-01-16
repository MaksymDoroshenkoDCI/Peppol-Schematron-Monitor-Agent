from agents.state import AgentState
from xmldiff import main, formatting
from lxml import etree

class DiffAnalyzerAgent:
    def run(self, state: AgentState) -> AgentState:
        print("--- Diff Analyzer Agent ---")
        
        content_old = state.get("schematron_content_old")
        content_new = state.get("schematron_content_new")
        
        if not content_old or not content_new:
             state["diff_results"] = []
             return state
            
        # Parse XML (Simple string comparison or xmldiff)
        # Using xmldiff for structured difference
        try:
            # xmldiff doesn't like strings with encoding declarations.
            # Convert to bytes.
            b_old = content_old.encode('utf-8') if isinstance(content_old, str) else content_old
            b_new = content_new.encode('utf-8') if isinstance(content_new, str) else content_new
            
            diffs = main.diff_texts(b_old, b_new)
            
            # Formating diffs into a consumable list
            # The diffs variable contains objects like <MoveNode>, <DeleteNode>, etc.
            # We'll serialize them to strings for the PoC.
            
            results = []
            for d in diffs:
                results.append({
                    "type": str(type(d).__name__),
                    "details": str(d)
                })
                
            state["diff_results"] = results
            print(f"Diff Analysis complete. Found {len(results)} changes.")
            
        except Exception as e:
            error_msg = f"Error during XML diff: {str(e)}"
            print(error_msg)
            state["errors"] = state.get("errors", []) + [error_msg]
            state["diff_results"] = []

        return state
