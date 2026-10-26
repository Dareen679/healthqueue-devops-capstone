# DORA baseline — SYNTHETIC 90-day illustration

Period: 2026-07-01 through 2026-09-28. Generated using a seeded Python simulation, **not production evidence**.

| Metric | Simulated result | Reading |
|---|---:|---|
| Deployment frequency | 1.49/day (134 deployments / 90 days) | Approximately daily |
| Lead time for changes | 17.1 hours (median) | Less than one day |
| Change failure rate | 14.2% (19/134) | Share causing incidents |
| Time to restore service | 87.1 minutes (mean) | Approximate recovery time |

## Benchmark interpretation
The historical DORA *four-metric* categories are frequently described as elite, high, medium, and low; thresholds vary by report year and some newer DORA reporting uses different clusters and five metrics. For a **teaching comparison**, classic elite markers often include on-demand/multiple daily deployments, less-than-one-day lead time, 0–15% change failure rate, and under-one-hour restore time. This simulated team meets the lead time and failure-rate examples, but daily frequency and mean restore time should not be labeled universally “elite.” Do not treat mixed metrics as one precise grade.

## Practical improvements to reduce toil
1. Automatically triage failing deployments via versioned runbooks and alerts.
2. Add automated image updating through reviewed pull requests instead of copying tags by hand.
3. Build self-service templates for standard changes and require human approval for sensitive production actions.
4. Track manual hours/week and alert noise/week before and after automation; aim for a 25% reduction in both during a monitored pilot.

## Validation and caveats
The CSV has one row per simulated deployment; failure means a simulated post-deployment incident, not a failed CI check. In a real environment, derive deployment timestamps from successful releases, lead time from commit-to-production telemetry, and recoveries from incident records. Use medians/percentiles alongside means for skewed incidents. Synthetic values cannot establish actual HealthQueue performance.

Sources: https://dora.dev/guides/dora-metrics-four-keys/ and https://dora.dev/research/2023/dora-report/ .
