# Monitoring, Governance, and Release

Use this module for production readiness, rollout, governance, and maintenance.

## Monitoring

Instrument:

- User/task metadata with privacy-safe IDs
- Model calls and prompt versions
- Retrieval queries, chunks, scores, citations
- Tool calls, arguments, errors, approvals, side effects
- Skill routes and eligibility failures
- Cost, latency, retries, and rate limits
- User outcomes and human review labels

## Governance and security

Review:

- Data permissions and tenant isolation
- PII/secrets redaction
- Tool risk tiers and approval gates
- Prompt injection/tool poisoning defenses
- Audit logs and retention
- Model/provider/data provenance
- Red-team coverage

## Release gates

Gate on:

- Must-pass safety/privacy cases
- Eval quality threshold
- No forbidden tool/side-effect traces
- Cost/latency within budget
- Canary monitoring plan
- Rollback plan

## Deliverables

- Readiness review
- Release gate
- Rollout/canary plan
- Monitoring dashboard spec
- Incident response plan
