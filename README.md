Live Demo: https://git-repo-health-analyzer.onrender.com/
API Docs: https://git-repo-health-analyzer.onrender.com/docs


<h1 align="center">📊 Git Repository Health Analyzer</h1>

<p align="center">
  Analyze the real engineering health of any public GitHub repository.
</p>

<hr/>

<h2>🧠 Problem Statement</h2>

<p>
Recruiters and engineering managers often judge repositories by stars, forks, or recent activity.
These signals are shallow and miss critical engineering indicators like collaboration quality,
delivery discipline, automation maturity, and maintainability.
</p>

<p>
The <b>Git Repository Health Analyzer</b> solves this by evaluating public GitHub repositories
using objective DevOps and engineering metrics, and producing a clear, explainable health score.
</p>

<p>
This project is designed to be:
</p>

<ul>
  <li>Completely free and open-source</li>
  <li>Publicly accessible with a live demo</li>
  <li>Useful for recruiters, engineers, and open-source maintainers</li>
</ul>

<hr/>

<h2>📌 What This Tool Does</h2>

<ul>
  <li>Accepts a public GitHub repository URL</li>
  <li>Fetches repository data using GitHub APIs</li>
  <li>Evaluates multiple engineering health signals</li>
  <li>Generates a transparent health score (0–100)</li>
  <li>Displays detailed metric breakdowns</li>
</ul>

<hr/>

<h2>📐 Health Metrics (v1)</h2>

<h3>1️⃣ Commit Activity</h3>
<p>
Measures how actively and consistently the repository is maintained.
</p>
<ul>
  <li>Commits in the last 30 and 90 days</li>
  <li>Detects stale or abandoned repositories</li>
</ul>

<h3>2️⃣ Contributor Diversity (Bus Factor)</h3>
<p>
Evaluates dependency on individual contributors.
</p>
<ul>
  <li>Counts unique contributors in recent history</li>
  <li>Flags single-maintainer risk</li>
</ul>

<h3>3️⃣ Pull Request Hygiene</h3>
<p>
Analyzes collaboration and review practices.
</p>
<ul>
  <li>PR merge rate</li>
  <li>Average PR open-to-merge time</li>
</ul>

<h3>4️⃣ CI/CD Presence</h3>
<p>
Checks whether automated pipelines exist.
</p>
<ul>
  <li>GitHub Actions workflows</li>
  <li>Other CI configuration files</li>
</ul>

<h3>5️⃣ Documentation Quality</h3>
<p>
Assesses onboarding and usability readiness.
</p>
<ul>
  <li>README presence</li>
  <li>Minimum documentation depth</li>
</ul>

<hr/>

<h2>⚖️ Scoring Model</h2>

<table border="1" cellpadding="8" cellspacing="0">
  <tr>
    <th>Metric</th>
    <th>Weight</th>
  </tr>
  <tr>
    <td>Commit Activity</td>
    <td>25%</td>
  </tr>
  <tr>
    <td>Contributor Diversity</td>
    <td>20%</td>
  </tr>
  <tr>
    <td>Pull Request Hygiene</td>
    <td>25%</td>
  </tr>
  <tr>
    <td>CI/CD Presence</td>
    <td>15%</td>
  </tr>
  <tr>
    <td>Documentation Quality</td>
    <td>15%</td>
  </tr>
</table>

<p>
Final scores are classified as:
</p>

<ul>
  <li><b>80–100</b> → Healthy</li>
  <li><b>60–79</b> → Needs Attention</li>
  <li><b>&lt;60</b> → At Risk</li>
</ul>

<hr/>

<h2>📥 Input</h2>

<pre>
https://github.com/organization/repository
</pre>

<hr/>

<h2>📤 Example Output</h2>

<pre>
{
  "repository": "organization/repository",
  "health_score": 82,
  "status": "Healthy",
  "metrics": {
    "commit_activity": "Healthy",
    "contributors": "Low Risk",
    "pull_request_hygiene": "Healthy",
    "ci_cd": "Present",
    "documentation": "Good"
  }
}
</pre>

<hr/>

<h2>🛠️ Tech Stack (Planned)</h2>

<ul>
  <li>Python</li>
  <li>GitHub REST API</li>
  <li>FastAPI</li>
  <li>SQLite</li>
  <li>Docker</li>
  <li>Public hosting (free tier)</li>
</ul>

<hr/>

<h2>🚀 Project Status</h2>

<p>
This project is under active development.
Upcoming milestones include:
</p>

<ul>
  <li>GitHub API integration</li>
  <li>Backend scoring engine</li>
  <li>Public API endpoint</li>
  <li>Web UI for live analysis</li>
</ul>

<hr/>

<p align="center">
Built to demonstrate real-world DevOps and data engineering thinking.
</p>
