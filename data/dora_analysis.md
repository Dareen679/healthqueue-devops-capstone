
# DORA Baseline — Synthetic 90-Day Analysis

## Overview

This report evaluates HealthQueue's software delivery performance using simulated data covering July 1 through September 28, 2026 (90 days).

The dataset was generated using a seeded Python simulation. These results are for educational purposes and do not represent actual production performance.

## DORA Metrics Results

| Metric | Simulated Result | Interpretation |
|---|---|---|
| Deployment Frequency | 1.49 deployments per day (134 deployments in 90 days) | Approximately daily deployment |
| Lead Time for Changes | 17.1 hours (median) | Changes are delivered in less than one day |
| Change Failure Rate | 14.2% (19 of 134 deployments) | Relatively low failure rate |
| Time to Restore Service | 87.1 minutes (mean) | Recovery takes approximately 1.5 hours |

## Benchmark Interpretation

Historical DORA performance categories include Elite, High, Medium, and Low. These categories are useful for evaluating software delivery performance, although benchmark definitions and thresholds can change between report years.

### Historical Benchmark Comparison

| Performance Category | General Characteristics |
|---|---|
| Elite | Very frequent deployments, short lead times, low failure rates, and rapid recovery |
| High | Frequent deployments, relatively fast delivery, and reliable recovery |
| Medium | Moderate deployment frequency, longer delivery times, and opportunities to improve reliability |
| Low | Infrequent deployments, slow delivery, and greater operational challenges |

### HealthQueue Comparison

HealthQueue's simulated results demonstrate strengths and improvement opportunities.

**Deployment Frequency:** With 1.49 deployments per day, HealthQueue demonstrates frequent delivery, although elite-performing teams may deploy multiple times daily or on demand.

**Lead Time:** The median lead time of 17.1 hours is a strength because most changes reach deployment within one day.

**Change Failure Rate:** A 14.2% failure rate is relatively low compared with some historical DORA category thresholds. However, reducing failures remains important.

**Recovery Time:** The average recovery time of 87.1 minutes suggests that incident response and rollback procedures could be improved.

Overall, the simulated team shows a mixture of performance characteristics rather than fitting neatly into one category. These comparisons are illustrative, not an official DORA performance classification.

## Practical Improvements to Reduce Manual Toil

### 1. Automate Incident Triage

Use monitoring alerts and versioned runbooks to identify failing deployments and recommend recovery actions.

**Expected benefit:** Reduce time spent investigating recurring incidents.

### 2. Automate Image Updates

Use automated pull requests to update container image references instead of manually copying image tags.

Require human review before sensitive production changes are approved.

**Expected benefit:** Reduce repetitive work while maintaining deployment oversight.

### 3. Introduce Self-Service Templates

Create reusable templates for common software delivery tasks, including testing, infrastructure configuration, and deployment.

**Expected benefit:** Improve consistency and reduce manual configuration errors.

### 4. Measure Toil Reduction

Track hours spent on manual tasks and unnecessary alerts before and after introducing automation.

Set a pilot target of reducing both manual effort and alert noise by 25%.

This is a proposed improvement target, not a measured outcome.

## Validation and Limitations

The supporting dataset is stored in `data/dora_90day_synthetic.csv`.

Each row represents a simulated deployment.

For production measurement:

- Calculate deployment frequency from successful production deployment records.
- Measure lead time using commit timestamps and production deployment timestamps.
- Calculate change failure rate using deployments that cause incidents.
- Measure recovery time from incident records.
- Use appropriate medians, percentiles, and averages.
- Compare results against benchmark definitions from the same reporting year.

The simulated dataset cannot establish HealthQueue's real production performance.

## Recommendations

HealthQueue should prioritize faster incident recovery while maintaining reliable deployments.

The team should also introduce automated rollback guidance, strengthen observability, and reduce repetitive manual deployment tasks.

Progress should be reviewed using consistently defined DORA metrics and documented results rather than assumptions.

## References

- DORA — Four Keys: https://dora.dev/guides/dora-metrics-four-keys/
- DORA — 2023 State of DevOps Report: https://dora.dev/research/2023/dora-report/

