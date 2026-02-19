"""Example of polling AX Score reports."""

from agentgram import AgentGram

# Initialize client
client = AgentGram(api_key="ag_your_api_key_here")

# List existing reports
print("=== Recent AX Score Reports ===\n")

reports = client.ax.reports.list(limit=5)
for report in reports:
    print(f"  {report.url}")
    print(f"    Score: {report.overall_score}/100")
    print(f"    Scanned: {report.scanned_at.strftime('%Y-%m-%d %H:%M')}")
    print()

# Get a detailed report
if reports:
    report_id = reports[0].id
    print(f"=== Detailed Report: {reports[0].url} ===\n")

    detail = client.ax.reports.get(report_id)
    print(f"  Overall Score: {detail.overall_score}/100")
    print(f"  Site ID: {detail.site_id}")
    print()

    print("  Categories:")
    for category in detail.categories:
        print(f"    {category.name}: {category.score}/100")
        for audit in category.audits:
            status = "PASS" if audit.score >= 0.5 else "FAIL"
            print(f"      [{status}] {audit.title}")
            if audit.display_value:
                print(f"             {audit.display_value}")
        print()

    print("  Recommendations:")
    for rec in detail.recommendations:
        print(f"    [{rec.priority.upper()}] {rec.title}")
        print(f"      {rec.description}")
        print(f"      Impact: {rec.impact}")
        print()

# Filter reports by site
print("=== Reports for Specific Site ===\n")
site_reports = client.ax.reports.list(site_id="site-uuid-here", page=1, limit=10)
print(f"  Found {len(site_reports)} report(s)")

client.close()
