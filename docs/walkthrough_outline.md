# 8–10 minute camera-on walkthrough — prompts, not a read-aloud script

Use your own words, keep your face visible throughout, and show genuine evidence. These are **speaker prompts only**, not a script to read verbatim.

| Time | Screen | Talking points |
|---|---|---|
| 0:00–0:50 | README/architecture | Introduce yourself as lead DevOps engineer; explain HealthQueue appointment API and why reproducibility matters to Maya. |
| 0:50–2:30 | API, tests, Actions | Show health endpoint, five tests and CI sequence; explain why HIGH/CRITICAL blocking is important; show actual GitHub run. |
| 2:30–3:25 | SBOM, GHCR/signature, supply-chain doc | SBOM inventory, signed digest, SLSA caveat and stronger provenance next step. |
| 3:25–4:30 | OpenTofu code, plan | Name S3 and DynamoDB resources; remote state; show actual `tofu plan` only if run. |
| 4:30–5:40 | K8s + Argo CD | Explain deployment, probes, two replicas, Git change -> reconciliation, and demonstrate actual Synced/Healthy only if deployed. |
| 5:40–7:00 | SLO doc | 99.9% availability, 43.2 min budget, 99% under 500 ms; distinguish plan from installed telemetry. |
| 7:00–8:10 | Synthetic CSV/analysis | Four DORA results, mixed benchmark assessment, concrete manual-toil reductions. |
| 8:10–9:20 | ADR, runbook, README | Explain privacy limits, tests needed, trade-offs, CTO-ready next steps. |

**Video submission:** 8–10 minutes (absolute maximum 10), MP4 preferred, entire time face on-camera (picture-in-picture acceptable). Upload through LMS along with repo URL and artifacts. Do not read this outline word-for-word.
