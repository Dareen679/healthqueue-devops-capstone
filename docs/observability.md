# Observability and SRE plan — appointment API

**Proposed objectives, not measured production performance.** This starter API does not yet export telemetry: metrics instrumentation, a collector, dashboards and alert routing must be configured for deployment.

## User-facing SLIs
1. Availability = valid appointment API requests returning non-5xx / all valid requests. Target **99.9%** over a rolling 30-day window. Monitor 5xx, timeouts, and availability probes; 4xx validation errors do not count as server failures.
2. Latency = proportion of successful appointment requests completed within 500 ms. Target **99%** over 30 days. Track histogram-based latency by route; never use raw patient IDs as metric labels.

## Error budget math
30 days × 24 hours × 60 minutes = **43,200 minutes**. With 99.9% availability, allowable unavailability equivalent = 43,200 × (1−0.999) = **43.2 minutes** per 30 days. This minute-equivalent is a simple approximation; request-based budget is 0.1% of eligible requests, which more closely matches the defined SLI. The 99% latency objective permits 1% of successful requests exceeding 500 ms.

## Signal path and alerting
- API -> OpenTelemetry SDK/collector -> Prometheus (requests, status, duration histogram), Loki or centralized log store (JSON request and error events), Tempo/Jaeger (redacted distributed traces), Grafana dashboards; PagerDuty or equivalent for paging.
- Page on a sustained high error-budget burn, not every isolated 5xx. Example: 5-minute and 1-hour multi-window burn-rate signal; route to on-call. The on-call **acknowledgment objective is 5 minutes after an alert fires**, not a guarantee that incidents are discovered within 5 minutes of first impact.
- Warnings: rising p95 latency, pod restarts, saturation, elevated 4xx client mistakes. Keep 4xx separate from availability errors.
- Use trace/request IDs, not names, dates of birth, appointment detail, tokens, or patient references in logs. Restricted access, short retention, audit logging, encryption.

## Test and validation evidence to collect
1. Make 100 synthetic requests locally; verify request counts, traces and log IDs match after instrumentation is installed.
2. Inject 5xx in a staging environment; record the **actual** delay between injected failure and alert firing, then check the 5-minute acknowledgment goal separately.
3. Run a controlled load test; validate p95 and the 500 ms histogram bucket.
4. Simulate a 10-minute outage in SLO test data and verify that 33.2 minute-equivalent budget remains (43.2 − 10), assuming the month-equivalent simplification.
5. Verify monitoring access controls, sensitive-field redaction and alert routing by checking a test alert.

## Operational response
Sev 1: appointment scheduling unavailable across regions / widespread failures: page immediately, rollback bad image by reviewed Git commit, post status within 15 minutes, update every 30 minutes. Sev 2: degraded latency or partial availability: page on-call based on sustained burn and coordinate remediation. Afterward conduct blameless review with action owners and deadlines.
