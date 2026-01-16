from typing import TypedDict, List, Dict, Any, Optional

class AgentState(TypedDict):
    """
    Represents the shared state passing through the LangGraph agents.
    """
    # Monitor Agent Outputs
    latest_version: str
    previous_version: str
    schematron_content_new: str
    schematron_content_old: str
    
    # Diff Agent Outputs
    diff_results: List[Dict[str, Any]]  # List of changes
    
    # Mapping Agent Outputs
    impact_analysis: List[Dict[str, Any]] # List of affected mappings
    
    # Report Agent Outputs
    report_path: str
    report_summary: str
    
    # Router/Control
    task_type: str # 'monitor', 'analyze', 'report'
    errors: List[str]
