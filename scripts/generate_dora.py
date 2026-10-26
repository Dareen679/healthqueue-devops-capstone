"""Deterministic, SYNTHETIC 90-day DevOps events; not HealthQueue actual performance."""
import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)
OUT = Path(__file__).resolve().parent.parent / 'data'
OUT.mkdir(exist_ok=True)
start = date(2026, 7, 1)
rows = []
for day in range(90):
    dt = start + timedelta(days=day)
    deployments = random.choices([0, 1, 2, 3], weights=[12, 42, 36, 10])[0]
    for n in range(deployments):
        lead_hours = round(random.uniform(3, 29), 2)
        failure = random.random() < 0.12
        recovery_minutes = round(random.uniform(22, 140), 1) if failure else 0
        rows.append({'date': dt.isoformat(), 'deployment_id': f'd{day:03d}-{n}',
                     'lead_time_hours': lead_hours, 'caused_incident': int(failure),
                     'recovery_minutes': recovery_minutes})
with (OUT / 'dora_90day_synthetic.csv').open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)
from statistics import median, mean
count=len(rows)
failures=[r for r in rows if r['caused_incident']]
frequency=count/90
lead=median(r['lead_time_hours'] for r in rows)
cfr=100*len(failures)/count
restore=mean(r['recovery_minutes'] for r in failures) if failures else 0
result=f"""# DORA baseline — SYNTHETIC 90-day illustration

Period: {start.isoformat()} through {(start+timedelta(days=89)).isoformat()}. Generated using a seeded Python simulation, **not production evidence**.

| Metric | Simulated result | Reading |
|---|---:|---|
| Deployment frequency | {frequency:.2f}/day ({count} deployments / 90 days) | Approximately daily |
| Lead time for changes | {lead:.1f} hours (median) | Less than one day |
| Change failure rate | {cfr:.1f}% ({len(failures)}/{count}) | Share causing incidents |
| Time to restore service | {restore:.1f} minutes (mean) | Approximate recovery time |

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
"""
(OUT / 'dora_analysis.md').write_text(result)
print(result.split('## Benchmark')[0])
