<h1>📐 Repository Health Metrics – Design & Rationale</h1>

<p>
This document defines the engineering metrics used by the
<b>Git Repository Health Analyzer</b>.
Each metric is intentionally chosen to reflect real-world
maintainability, collaboration, and delivery discipline.
</p>

<hr/>

<h2>🎯 Design Principles</h2>

<ul>
  <li>Metrics must be explainable and transparent</li>
  <li>All signals should be derivable from public GitHub data</li>
  <li>No stars, forks, or popularity-based shortcuts</li>
  <li>Bias toward operational and collaboration health</li>
</ul>

<hr/>

<h2>1️⃣ Commit Activity</h2>

<h3>What it Measures</h3>
<p>
How consistently the repository is being updated.
This indicates whether the project is actively maintained
or potentially abandoned.
</p>

<h3>Data Source</h3>
<ul>
  <li>GitHub Commits API</li>
</ul>

<h3>Calculation</h3>
<ul>
  <li>Number of commits in the last 30 days</li>
  <li>Number of commits in the last 90 days</li>
</ul>

<h3>Scoring Logic</h3>
<table border="1" cellpadding="8" cellspacing="0">
  <tr>
    <th>Condition</th>
    <th>Score</th>
  </tr>
  <tr>
    <td>20+ commits in last 30 days</td>
    <td>Healthy</td>
  </tr>
  <tr>
    <td>5–19 commits</td>
    <td>Moderate</td>
  </tr>
  <tr>
    <td>&lt;5 commits</td>
    <td>Stale</td>
  </tr>
</table>

<h3>Limitations</h3>
<p>
This metric does not account for repository size or maturity.
Stable projects may have lower commit frequency but still be healthy.
</p>

<hr/>

<h2>2️⃣ Contributor Diversity (Bus Factor)</h2>

<h3>What it Measures</h3>
<p>
Dependency on individual contributors.
A low number of active contributors increases maintenance risk.
</p>

<h3>Data Source</h3>
<ul>
  <li>Commit author metadata</li>
</ul>

<h3>Calculation</h3>
<ul>
  <li>Unique commit authors in the last 90 days</li>
</ul>

<h3>Scoring Logic</h3>
<table border="1" cellpadding="8" cellspacing="0">
  <tr>
    <th>Contributors</th>
    <th>Risk Level</th>
  </tr>
  <tr>
    <td>5+</td>
    <td>Low Risk</td>
  </tr>
  <tr>
    <td>2–4</td>
    <td>Medium Risk</td>
  </tr>
  <tr>
    <td>1</td>
    <td>High Risk</td>
  </tr>
</table>

<h3>Limitations</h3>
<p>
Does not differentiate between core maintainers and casual contributors.
Future versions may apply weighted contribution analysis.
</p>

<hr/>

<h2>3️⃣ Pull Request Hygiene</h2>

<h3>What it Measures</h3>
<p>
Collaboration quality and review discipline.
Healthy repositories review and merge changes predictably.
</p>

<h3>Data Source</h3>
<ul>
  <li>GitHub Pull Requests API</li>
</ul>

<h3>Calculation</h3>
<ul>
  <li>PR merge rate in last 90 days</li>
  <li>Average time from PR open to merge</li>
</ul>

<h3>Scoring Logic</h3>
<table border="1" cellpadding="8" cellspacing="0">
  <tr>
    <th>Condition</th>
    <th>Status</th>
  </tr>
  <tr>
    <td>Merge rate &gt;70% and avg merge &lt;3 days</td>
    <td>Healthy</td>
  </tr>
  <tr>
    <td>Merge rate 40–70%</td>
    <td>Acceptable</td>
  </tr>
  <tr>
    <td>Below 40%</td>
    <td>Risky</td>
  </tr>
</table>

<h3>Limitations</h3>
<p>
Repositories using direct commits instead of PRs may score lower
despite having healthy practices.
</p>

<hr/>

<h2>4️⃣ CI/CD Presence</h2>

<h3>What it Measures</h3>
<p>
Automation maturity and delivery discipline.
CI pipelines reduce regression risk and improve reliability.
</p>

<h3>Data Source</h3>
<ul>
  <li>Repository file tree</li>
</ul>

<h3>Detection Rules</h3>
<ul>
  <li>.github/workflows directory</li>
  <li>.gitlab-ci.yml file</li>
  <li>Other known CI configuration files</li>
</ul>

<h3>Scoring</h3>
<ul>
  <li>Present → Pass</li>
  <li>Missing → Fail</li>
</ul>

<h3>Limitations</h3>
<p>
Does not validate pipeline quality or coverage.
Only checks for presence, not effectiveness.
</p>

<hr/>

<h2>5️⃣ Documentation Quality</h2>

<h3>What it Measures</h3>
<p>
Ease of onboarding and usability.
Well-documented projects scale better and reduce knowledge silos.
</p>

<h3>Data Source</h3>
<ul>
  <li>Repository root files</li>
</ul>

<h3>Evaluation Rules</h3>
<ul>
  <li>README.md exists</li>
  <li>Minimum content length threshold</li>
</ul>

<h3>Scoring</h3>
<ul>
  <li>Present and meaningful → Good</li>
  <li>Missing or minimal → Weak</li>
</ul>

<h3>Limitations</h3>
<p>
Does not assess documentation accuracy or completeness.
Future versions may analyze structure and section coverage.
</p>

<hr/>

<h2>📊 Final Health Score</h2>

<p>
Each metric contributes to the final score using weighted aggregation.
Weights reflect the importance of delivery discipline and collaboration.
</p>

<ul>
  <li><b>80–100</b> → Healthy</li>
  <li><b>60–79</b> → Needs Attention</li>
  <li><b>&lt;60</b> → At Risk</li>
</ul>

<hr/>

<h2>🔁 Future Improvements</h2>

<ul>
  <li>Language-specific scoring adjustments</li>
  <li>Repository age normalization</li>
  <li>ML-based anomaly detection</li>
  <li>Historical trend comparison</li>
</ul>

<p>
All enhancements will preserve transparency and explainability.
</p>
