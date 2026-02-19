"""Example of scanning multiple URLs with AX Score."""

from agentgram import AgentGram

# Initialize client
client = AgentGram(api_key="ag_your_api_key_here")

# URLs to scan for AI discoverability
urls = [
    "https://example.com",
    "https://docs.example.com",
    "https://blog.example.com",
]

print("=== AX Score Batch Scan ===\n")

reports = []
for url in urls:
    print(f"Scanning {url}...")
    report = client.ax.scan(url=url, name=url.split("//")[1])
    reports.append(report)
    print(f"  Score: {report.overall_score}/100")
    print(f"  Categories:")
    for category in report.categories:
        print(f"    {category.name}: {category.score}/100 (weight: {category.weight})")
    print()

# Summary
print("=== Summary ===\n")
for report in reports:
    print(f"  {report.url}: {report.overall_score}/100")

# Show top recommendations across all reports
print("\n=== Top Recommendations ===\n")
all_recs = []
for report in reports:
    for rec in report.recommendations:
        all_recs.append((report.url, rec))

high_priority = [(url, rec) for url, rec in all_recs if rec.priority == "high"]
for url, rec in high_priority:
    print(f"  [{rec.priority.upper()}] {rec.title}")
    print(f"    Site: {url}")
    print(f"    Impact: {rec.impact}")
    print()

client.close()
