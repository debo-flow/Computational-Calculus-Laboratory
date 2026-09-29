import json
import datetime
from typing import Dict, Any

def generate_verification_report(results: Dict[str, Any], format: str = "json") -> str:
    """Serializes test and benchmark results into standardized regression formats."""
    report = {
        "Timestamp": datetime.datetime.now().isoformat(),
        "Verification Protocol": "Milestone 24 Automated Mathematical Laboratory",
        "Results": results
    }
    
    if format == "json":
        return json.dumps(report, indent=4)
    elif format == "markdown":
        md = f"# Mathematical Verification Report\n*Generated: {report['Timestamp']}*\n\n"
        for key, val in results.items():
            md += f"### {key}\n"
            for k, v in val.items():
                md += f"- **{k}**: {v}\n"
            md += "\n"
        return md
    else:
        raise ValueError("Unsupported format. Use 'json' or 'markdown'.")
