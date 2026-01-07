<h1>🔗 GitHub API Usage & Strategy</h1>

<p>
This document defines how the <b>Git Repository Health Analyzer</b>
interacts with the GitHub REST API.
It documents endpoint selection, authentication strategy,
rate-limit handling, and caching rules.
</p>

<hr/>

<h2>🎯 Design Goals</h2>

<ul>
  <li>Minimize API usage while maximizing signal quality</li>
  <li>Stay within free GitHub API limits</li>
  <li>Remain transparent and easy to reason about</li>
  <li>Avoid hidden dependencies or paid features</li>
</ul>

<hr/>

<h2>📌 API Type</h2>

<p>
The system uses the <b>GitHub REST API v3</b>.
GraphQL is intentionally avoided to keep the implementation simple,
debuggable, and recruiter-friendly.
</p>

<hr/>

<h2>📂 Repository Identification</h2>

<p>
All user input is normalized to the following internal format:
</p>

<pre>
owner/repository
</pre>

<p>
Example:
</p>

<pre>
https://github.com/kubernetes/kubernetes
→ kubernetes/kubernetes
</pre>

<p>
This normalized identifier is used consistently across:
</p>

<ul>
  <li>API calls</li>
  <li>Cache keys</li>
  <li>Database records</li>
</ul>

<hr/>

<h2>📡 GitHub API Endpoints Used</h2>

<h3>1️⃣ Repository Metadata</h3>

<p>
Validates repository existence and retrieves basic metadata.
</p>

<pre>
GET /repos/{owner}/{repo}
</pre>

<p>
Failure at this stage stops the analysis immediately.
</p>

<hr/>

<h3>2️⃣ Commit Activity</h3>

<p>
Used to measure repository activity and freshness.
</p>

<pre>
GET /repos/{owner}/{repo}/commits
</pre>

<h4>Query Parameters</h4>
<ul>
  <li><code>since</code> – ISO 8601 timestamp</li>
  <li><code>per_page=100</code></li>
</ul>

<p>
Only commit metadata is used.
Commit contents and diffs are intentionally ignored.
</p>

<hr/>

<h3>3️⃣ Contributor Diversity</h3>

<p>
Contributor diversity is derived from commit author metadata.
</p>

<pre>
GET /repos/{owner}/{repo}/commits
</pre>

<p>
Author logins are deduplicated across commits
within the analysis window.
</p>

<p>
The <code>/contributors</code> endpoint is not used
due to caching delays and reduced freshness.
</p>

<hr/>

<h3>4️⃣ Pull Request Hygiene</h3>

<p>
Used to evaluate collaboration and review practices.
</p>

<pre>
GET /repos/{owner}/{repo}/pulls
</pre>

<h4>Query Parameters</h4>
<ul>
  <li><code>state=all</code></li>
  <li><code>per_page=100</code></li>
  <li><code>sort=updated</code></li>
  <li><code>direction=desc</code></li>
</ul>

<p>
Pagination stops once pull requests exceed the
90-day analysis window.
</p>

<hr/>

<h3>5️⃣ CI/CD Presence Detection</h3>

<p>
Checks for automated pipelines.
</p>

<pre>
GET /repos/{owner}/{repo}/contents/.github/workflows
</pre>

<p>
Response interpretation:
</p>

<ul>
  <li>200 → CI/CD configuration present</li>
  <li>404 → CI/CD configuration absent</li>
</ul>

<hr/>

<h3>6️⃣ Documentation Quality</h3>

<p>
Evaluates onboarding readiness through README presence.
</p>

<pre>
GET /repos/{owner}/{repo}/readme
</pre>

<p>
The response content is decoded and analyzed for length only.
Semantic parsing is intentionally deferred to future versions.
</p>

<hr/>

<h2>📄 Pagination Strategy</h2>

<p>
GitHub API pagination rules:
</p>

<ul>
  <li>Default page size is 30</li>
  <li>Maximum page size is 100</li>
</ul>

<p>
Pagination rules enforced by this system:
</p>

<ul>
  <li>Always request <code>per_page=100</code></li>
  <li>Stop pagination once data falls outside the analysis window</li>
  <li>Never fetch complete repository history</li>
</ul>

<hr/>

<h2>⏱️ Rate Limits</h2>

<h3>Unauthenticated Requests</h3>
<ul>
  <li>60 requests per hour (IP-based)</li>
</ul>

<h3>Authenticated Requests</h3>
<ul>
  <li>5,000 requests per hour</li>
</ul>

<p>
Authentication is optional but strongly recommended.
</p>

<hr/>

<h2>🔐 Authentication Strategy</h2>

<p>
The system supports optional authentication using a
GitHub Personal Access Token (PAT).
</p>

<h3>Token Requirements</h3>
<ul>
  <li>Read-only permissions</li>
  <li>No private repository access required</li>
</ul>

<h3>Configuration</h3>

<pre>
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxx
</pre>

<p>
If a token is present, authenticated requests are used.
If absent, the system falls back to unauthenticated requests.
</p>

<p>
No credentials are hard-coded or stored in the repository.
</p>

<hr/>

<h2>💾 Caching Strategy</h2>

<h3>Cache Scope</h3>
<ul>
  <li>Final analysis result only</li>
</ul>

<h3>Cache Key</h3>
<ul>
  <li>Normalized repository identifier (<code>owner/repo</code>)</li>
</ul>

<h3>Cache Duration</h3>
<ul>
  <li>24 hours</li>
</ul>

<h3>Storage</h3>
<ul>
  <li>SQLite database</li>
</ul>

<p>
Caching reduces API usage, improves response times,
and enables consistent demo behavior.
</p>

<hr/>

<h2>🚨 Failure Handling</h2>

<h3>Repository Not Found</h3>
<ul>
  <li>HTTP 404 response</li>
  <li>Clear user-facing error message</li>
</ul>

<h3>Rate Limit Exceeded</h3>
<ul>
  <li>HTTP 429 response</li>
  <li>Includes retry guidance</li>
</ul>

<h3>Partial Data Failures</h3>
<ul>
  <li>Affected metric marked as <code>Unavailable</code></li>
  <li>Remaining metrics still evaluated</li>
</ul>

<p>
The system always fails gracefully and transparently.
</p>

<hr/>

<h2>🔮 Future Enhancements</h2>

<ul>
  <li>GraphQL optimization for large repositories</li>
  <li>Conditional requests using ETags</li>
  <li>Background refresh jobs</li>
</ul>

<p>
All enhancements will preserve simplicity and explainability.
</p>
