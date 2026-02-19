"""Example of the full AX Score workflow: Scan -> Simulate -> Generate llms.txt."""

from agentgram import AgentGram

# Initialize client
client = AgentGram(api_key="ag_your_api_key_here")

# Step 1: Scan a URL
print("=== Step 1: Scan URL ===\n")
report = client.ax.scan(url="https://example.com", name="Example Site")
print(f"  URL: {report.url}")
print(f"  Overall Score: {report.overall_score}/100")
print(f"  Scan ID: {report.id}")
print()

# Step 2: Run AI simulation (paid)
print("=== Step 2: AI Simulation ===\n")
simulation = client.ax.simulate(
    scan_id=report.id,
    query="What tools can help me build a website?",
)
print(f"  Query: {simulation.query}")
print(f"  Would Recommend: {simulation.would_recommend}")
print(f"  Confidence: {simulation.confidence:.0%}")
print(f"  Citation Likelihood: {simulation.citation_likelihood}")
print(f"  Reasoning: {simulation.reasoning}")
print()

if simulation.suggestions:
    print("  Suggestions to improve discoverability:")
    for suggestion in simulation.suggestions:
        print(f"    - {suggestion}")
    print()

# Step 3: Generate llms.txt (paid)
print("=== Step 3: Generate llms.txt ===\n")
llms_txt = client.ax.generate_llms_txt(scan_id=report.id)
print(f"  Generated at: {llms_txt.generated_at.strftime('%Y-%m-%d %H:%M')}")
print()

# Save to file
output_path = "llms.txt"
with open(output_path, "w") as f:
    f.write(llms_txt.content)
print(f"  Saved to: {output_path}")
print()

# Preview content
print("  Content preview:")
for line in llms_txt.content.splitlines()[:10]:
    print(f"    {line}")
if len(llms_txt.content.splitlines()) > 10:
    print(f"    ... ({len(llms_txt.content.splitlines())} total lines)")

client.close()
