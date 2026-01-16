from langgraph.graph import StateGraph, END
from agents.state import AgentState
from agents.monitor import SchematronMonitorAgent
from agents.diff import DiffAnalyzerAgent
from agents.mapping import MappingImpactAgent
from agents.report import ReportGeneratorAgent

# Initialize Agents
monitor_agent = SchematronMonitorAgent()
diff_agent = DiffAnalyzerAgent()
mapping_agent = MappingImpactAgent()
report_agent = ReportGeneratorAgent()

def run_monitor(state: AgentState):
    return monitor_agent.run(state)

def run_diff(state: AgentState):
    return diff_agent.run(state)

def run_mapping(state: AgentState):
    return mapping_agent.run(state)

def run_report(state: AgentState):
    return report_agent.run(state)

# Define Graph
builder = StateGraph(AgentState)

# Add Nodes
builder.add_node("monitor", run_monitor)
builder.add_node("diff", run_diff)
builder.add_node("mapping", run_mapping)
builder.add_node("report", run_report)

# Define Edges
builder.set_entry_point("monitor")
builder.add_edge("monitor", "diff")
builder.add_edge("diff", "mapping")
builder.add_edge("mapping", "report")
builder.add_edge("report", END)

# Compile Graph
graph = builder.compile()

def run_graph():
    """
    Entry point to run the graph.
    """
    initial_state = {
        "latest_version": "",
        "previous_version": "",
        "schematron_content_new": "",
        "schematron_content_old": "",
        "diff_results": [],
        "impact_analysis": [],
        "report_path": "",
        "report_summary": "",
        "task_type": "monitor",
        "errors": []
    }
    
    result = graph.invoke(initial_state)
    return result
