import pandas as pd
from agents.state import AgentState

class ReportGeneratorAgent:
    def run(self, state: AgentState) -> AgentState:
        print("--- Report Generator Agent ---")
        
        diff_results = state.get("diff_results", [])
        impact_analysis = state.get("impact_analysis", [])
        version = state.get("latest_version", "unknown")
        
        report_lines = []
        report_lines.append(f"# Peppol Schematron Change Report - Version {version}")
        report_lines.append("\n## Schematron Changes")
        
        if not diff_results:
            report_lines.append("No changes detected.")
        else:
            for d in diff_results:
                report_lines.append(f"- [{d['type']}] {d['details']}")
                
        report_lines.append("\n## Mapping Impact Analysis")
        if not impact_analysis:
            report_lines.append("No immediate mapping impacts detected.")
        else:
            for impact in impact_analysis:
                report_lines.append(f"- **{impact['severity']}**: {impact['mapping_file']} (Field: {impact['affected_field']}) - {impact['reason']}")
                
        report_content = "\n".join(report_lines)
        state["report_summary"] = report_content
        
        # Save to file
        with open("report.md", "w") as f:
            f.write(report_content)
            
        state["report_path"] = "report.md"
        print("Report generated successfully.")
        
        return state
