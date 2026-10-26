# HealthQueue — DevOps Capstone Reference Architecture

A **repository-ready learning demonstration**, not a live or HIPAA-compliant appointment system. Designed for a CTO briefing; all data synthetic. Do not submit claims of verified infrastructure or running Argo CD until you personally test them and collect evidence.

## Contents
- `app/`, `tests/`: Flask demonstration appointment API with validation and synthetic IDs
- `.github/workflows/ci.yml`: test, image build, Trivy policy gate, SBOM, GHCR image, keyless signing
- `infra/`: OpenTofu S3 audit bucket + DynamoDB, remote S3 state configuration
- `k8s/`, `gitops/`: Kubernetes deployment/service, Argo CD GitOps application (templates)
- `scripts/generate_dora.py`, `data/`: seeded synthetic 90-day deployment CSV and analysis
- `docs/`: architecture/ADRs, SLSA assessment, monitoring/SLO budget, runbook, video outline

## Local test
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -q
python -m app.main
# another terminal:
curl http://127.0.0.1:8080/healthz
curl -X POST http://127.0.0.1:8080/appointments -H 'Content-Type: application/json' -d '{"patient_ref":"synthetic-only","starts_at":"2026-11-04T15:00:00Z"}'
python scripts/generate_dora.py
```

## GitHub preparation and scan/sign verification
1. Create a new GitHub repository and push these files. In repo settings enable Actions and ensure `GITHUB_TOKEN` has permitted GHCR package publishing. Protect `main` by PR review and status checks.
2. Show the **actual** workflow run, passing tests, Trivy results, and uploaded SBOM. A scan can fail due to newly published vulnerabilities. Resolve/record findings rather than suppressing them simply to pass.
3. On `main` pushes, see the GHCR image tagged with the commit SHA and Cosign signing log. Inspect image digest and verify signing using `cosign verify --certificate-identity-regexp 'https://github.com/.+/.+/.github/workflows/ci.yml@refs/heads/main' --certificate-oidc-issuer https://token.actions.githubusercontent.com ghcr.io/OWNER/REPO@sha256:YOUR_DIGEST` (replace all placeholders; inspect certificate identity from your run).
4. To deploy, edit `k8s/deployment.yaml` to your **actual** image location and immutable SHA tag. For stronger reproducibility/security, use the digest instead of a mutable tag. Open and merge a PR to promote the release.

## OpenTofu: AWS credentials, cost, and remote state
1. An AWS account is needed; creating real resources can incur costs. Set a budget/cleanup plan. Never put credentials or patient details in Git.
2. Create a **separate existing S3 bucket** for Terraform state with versioning, encryption, access restrictions and locking support. Copy `infra/backend.hcl.example` to `infra/backend.hcl` and replace placeholders. Remote state is not automatically provisioned by this project; it must exist first.
3. `cd infra && tofu init -backend-config=backend.hcl && tofu fmt -check && tofu validate && tofu plan -var='name_suffix=YOUR_UNIQUE_SUFFIX'`.
4. Review plan and optionally `tofu apply -var='name_suffix=YOUR_UNIQUE_SUFFIX'` in a demo account. Save and screenshot the plan / applied resources; use `tofu destroy` when finished. Do not destroy the separately bootstrapped state bucket before cleaning up.

## Kubernetes and Argo CD
1. Use an existing authorized Kubernetes cluster with Argo CD installed, a kube context and adequate permissions.
2. Update `gitops/application.yaml` with your actual GitHub URL, and change Kubernetes image placeholders.
3. `kubectl apply -f gitops/application.yaml`, inspect Argo CD app `healthqueue` for **Synced** and **Healthy** and inspect pods `Ready`. Edit image via PR, merge and confirm reconciliation. Capture before/after evidence.
4. This demonstration has no public ingress, TLS or authentication. Do not expose to real users. This project **does not yet automate image tag promotion**. Argo CD reconciliation is configured, not proven until tested.

## What is and is not implemented
**Locally checkable:** Python endpoints and tests, deterministic data generator, documents and configuration syntax. **Depends on your environment:** successful CI security gate, image push/sign, IaC deployment, Argo CD sync and Kubernetes app health. **Planned, not installed:** OpenTelemetry pipeline, Grafana, alert routing, automated supply-chain provenance verification, persistence/auth/security review. Present these honestly in the video.

## Sources
- DORA: https://dora.dev/guides/dora-metrics-four-keys/ and https://dora.dev/research/2023/dora-report/
- SLSA: https://slsa.dev/spec/v1.1/levels
- Argo CD: https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/
- OpenTofu: https://opentofu.org/docs/language/settings/backends/s3/
- Kubernetes: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
- Google SRE: https://sre.google/workbook/alerting-on-slos/

## Submission checklist
- [ ] Repository pushed and working CI run screenshotted
- [ ] SBOM & signing evidence, explain Trivy fail behavior
- [ ] `tofu plan`/apply evidence using remote state
- [ ] Argo CD Synced/Healthy and pods Ready screenshot
- [ ] DORA CSV, analysis, security and SRE docs
- [ ] Diagram, ADRs, runbook and README
- [ ] Camera-on 8–10 minute video recorded in your own words and uploaded through LMS
- [ ] GitHub URL + all required deliverables submitted
