<h1>🏗️ System Architecture & Data Flow</h1>

<p>
This document describes the system architecture of the
<b>Git Repository Health Analyzer</b>.
It explains how data flows through the system, what components exist,
and the responsibility of each layer.
</p>

<hr/>

<h2>🎯 Architectural Goals</h2>

<ul>
  <li>Keep the system simple and explainable</li>
  <li>Separate concerns clearly</li>
  <li>Allow easy addition of new metrics</li>
  <li>Remain fully deployable using free and open-source tools</li>
</ul>

<hr/>

<h2>🧱 High-Level Architecture</h2>

<p>
The system is designed as a lightweight, service-oriented application
with four logical layers:
</p>

<pre>
User
  ↓
API Layer
  ↓
Data Collection & Scoring Engine
  ↓
Storage
</pre>

<p>
Each layer has a single, well-defined responsibility.
</p>

<hr/>

<h2>1️⃣ User Layer</h2>

<h3>Purpose</h3>
<p>
Acts as the public entry point for the system.
Allows users (recruiters, engineers, reviewers) to analyze any
public GitHub repository.
</p>

<h3>Responsibilities</h3>
<ul>
  <li>Accept a GitHub repository URL</li>
  <li>Display analysis results</li>
</ul>

<h3>Notes</h3>
<p>
No authentication is required.
The interface is intentionally simple to allow quick evaluation.
</p>

<hr/>

<h2>2️⃣ API Layer</h2>

<h3>Technology</h3>
<ul>
  <li>FastAPI</li>
</ul>

<h3>Responsibilities</h3>
<ul>
  <li>Validate input repository URLs</li>
  <li>Expose analysis endpoints</li>
  <li>Coordinate analysis workflow</li>
  <li>Return structured JSON responses</li>
</ul>

<h3>Responsibilities Explicitly Excluded</h3>
<ul>
  <li>No GitHub-specific parsing logic</li>
  <li>No scoring or business logic</li>
</ul>

<p>
This keeps the API layer thin, predictable, and testable.
</p>

<hr/>

<h2>3️⃣ Data Collection & Scoring Engine</h2>

<p>
This layer contains the core intelligence of the system.
It is divided into modular components to support extensibility
and clear ownership of logic.
</p>

<h3>a) GitHub Data Collector</h3>

<h4>Purpose</h4>
<p>
Fetch raw repository data from GitHub.
</p>

<h4>Data Retrieved</h4>
<ul>
  <li>Commits</li>
  <li>Contributors</li>
  <li>Pull requests</li>
  <li>Repository file tree</li>
</ul>

<h4>Design Rule</h4>
<p>
This module only retrieves data.
It performs no scoring, classification, or interpretation.
</p>

<hr/>

<h3>b) Metric Evaluators</h3>

<p>
Each metric is implemented as an independent evaluator.
</p>

<ul>
  <li>CommitActivityEvaluator</li>
  <li>ContributorDiversityEvaluator</li>
  <li>PullRequestHygieneEvaluator</li>
  <li>CIPresenceEvaluator</li>
  <li>DocumentationEvaluator</li>
</ul>

<h4>Responsibilities</h4>
<ul>
  <li>Accept raw GitHub data</li>
  <li>Apply metric-specific logic</li>
  <li>Return normalized metric results</li>
</ul>

<p>
This design allows metrics to be added, removed, or modified
without impacting other parts of the system.
</p>

<hr/>

<h3>c) Score Aggregator</h3>

<h4>Purpose</h4>
<p>
Combines individual metric results into a final health score.
</p>

<h4>Responsibilities</h4>
<ul>
  <li>Apply metric weights</li>
  <li>Calculate final score (0–100)</li>
  <li>Assign repository health status</li>
</ul>

<p>
The aggregator understands the scoring model,
not how the data was collected.
</p>

<hr/>

<h2>4️⃣ Storage Layer</h2>

<h3>Technology</h3>
<ul>
  <li>SQLite</li>
</ul>

<h3>Purpose</h3>
<ul>
  <li>Cache analysis results</li>
  <li>Reduce GitHub API usage</li>
  <li>Enable future historical comparisons</li>
</ul>

<h3>Stored Data</h3>
<ul>
  <li>Repository identifier</li>
  <li>Analysis timestamp</li>
  <li>Metric results</li>
  <li>Final health score</li>
</ul>

<p>
SQLite is chosen for simplicity, portability, and zero operational overhead.
</p>

<hr/>

<h2>🔁 End-to-End Data Flow</h2>

<pre>
1. User submits a GitHub repository URL
2. API validates input
3. API checks local cache (SQLite)
4. If cached:
   → Return stored result
5. If not cached:
   → Fetch data from GitHub
   → Evaluate individual metrics
   → Aggregate final score
   → Store result in SQLite
6. API returns structured response
</pre>

<hr/>

<h2>📡 API Contract</h2>

<h3>Endpoint</h3>
<pre>POST /analyze</pre>

<h3>Request</h3>
<pre>
{
  "repo_url": "https://github.com/organization/repository"
}
</pre>

<h3>Response</h3>
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
  },
  "analyzed_at": "2026-01-07T14:10:00Z"
}
</pre>

<hr/>

<h2>🔮 Future Architectural Extensions</h2>

<ul>
  <li>Historical trend analysis</li>
  <li>Metric versioning</li>
  <li>Async background processing</li>
  <li>Optional authentication for private repositories</li>
</ul>

<p>
All future enhancements will preserve modularity and transparency.
</p>
