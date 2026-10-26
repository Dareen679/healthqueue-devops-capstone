# Appointment API operational runbook (proposed)

Owner: HealthQueue application on-call. CTO escalation: Maya Chen. No actual pager contacts supplied; configure production routing before launch.

## Alert: high error rate / loss of scheduling
1. Acknowledge page within a **target** of 5 minutes of *alert firing*; declare severity using impact, not only error count.
2. Inspect error rate and latency dashboards, request IDs and recent GitHub releases. Never expose patient information in chat or logs.
3. If a new release caused failures, revert the GitOps image change by PR and watch Argo CD Synced/Healthy and two Ready pods. If urgent, use the pre-approved emergency process, then reconcile the emergency change in Git.
4. Recheck synthetic test traffic and burn-rate reduction. Notify CTO and stakeholders based on severity.
5. Record impact start/end, alert firing time, acknowledgement time, timeline, causal factors and follow-up ownership in a blameless review.

## Recovery check
Kubernetes: `kubectl -n healthqueue get pods,svc`; port forward: `kubectl -n healthqueue port-forward svc/appointment-api 8080:80`; then `curl -i http://localhost:8080/healthz`. Do not claim these commands passed without captured results.
