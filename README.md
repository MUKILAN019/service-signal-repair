# Repair Service Monitoring and Reliability Checks

CampusEvents API responds to requests, but its monitoring report confuses golden signals, its alert misses sustained request failures, and its reliability summary incorrectly reports remaining error budget. Repair monitoring configuration and explain whether service meets its agreed objective.

Module 5 only (LU 5.1, 5.2, 5.4). Local, free, no cloud account or credentials.

## Before 30-minute timer

Fork https://github.com/kalviumcommunity/service-signal-repair and clone your fork. Python 3.9+ standard library, terminal, editor and PDF/screenshot tool must already work. No package install. Run commands from repository root. Report unrelated environment failures to instructor and pause timer. Q3 binds ephemeral localhost ports and terminates only processes it creates. Windows may use `python` instead of `python3`.

## Application/evidence contract

Metric definitions: latency_p95_seconds is p95 request duration in seconds; requests_total is request count in supplied window; error_ratio is failed requests / total requests; cpu_ratio is CPU use / CPU capacity. Map all four correctly in ops/signals.json.

Agreed symptom alert: error_ratio strictly greater than 0.05 for 60 consecutive seconds, runbook ops/runbook.md. Each sample represents a complete 10-second bucket; six consecutive failing buckets are needed. High CPU alone must stay quiet, one short error spike must stay quiet, sustained request errors must fire. ops/alert.json has exactly four fields to correct. This is offline sample evaluation, not installed Prometheus/Grafana.

Budget review: fixtures/window.json contains 10,000 requests, 120 errors and agreed 99.0% SLO for its explicitly supplied fixed window. SLI=successful/total ×100; allowed errors=total×(1−SLO/100); remaining=allowed−actual errors. Keep target and fixture data unchanged. Negative remaining budget requires reliability work before routine feature releases for this exercise.

## Exactly three task groups

1. Correct golden-signal mapping — 4 configuration lines — 6 marks. Correct four mapping values using metric definitions, then show all four signal names and values. Explain original mismatch in screenshot caption.

2. Repair symptom alert — 4 configuration lines — 7 marks. Correct metric, ratio threshold, complete observation window and runbook. Run all three scenarios; show healthy and short spike QUIET and sustained errors FIRING. Do not shorten window to make test pass.

3. Assess reliability — 4 written lines — 7 marks. Replace four draft lines: measured SLI versus agreed SLO/window; allowed errors with formula; remaining budget with formula; release recommendation explaining negative budget. Use supplied totals, not invented observations.

## Commands (complete in order)

```bash
python3 check.py signals
python3 check.py alert
python3 check.py budget
```

Permitted edits: **ops/signals.json, ops/alert.json, analysis.md**. Do not change check.py, support.py, drill.py, fixtures, generated evidence or targets. Tasks are independently callable; Task 1 repair is needed for Q2 trace, but written analysis may be drafted from supplied evidence. Report commands may run successfully even when written drafts are wrong: a PASS line validates only runtime/configuration, NEVER correctness of prose. Written answers are manually graded against evidence, not exact keywords.

Each task is one fault/incomplete-analysis group, not necessarily one bad line. Three-to-five meaningful content lines per task; existing scaffolding supplied. Braces/blank lines/comments and editor wrapping do not count. No artificial line padding. Normal JSON pretty-printing may expand formatting without increasing task scope.

## Submission

One PDF, three labelled task sections, fork URL as text, readable real command output and corrected diff/file, requested 3–5-line analysis (PDF text or editor screenshot). Show failing configuration output before repair and passing output after for code/config tasks; written tasks show supplied source evidence and corrected analysis. Minimum one real screenshot per task; combine related evidence if readable or use extra screenshots. No PR/video/ZIP required. Commit corrections to your own fork; evaluator grades PDF, not private account access. Suggested 5 minutes diagnosis, 18 minutes repair/analysis, 7 minutes verification/PDF. Never fabricate results or include secrets. Checker success does not replace written reasoning or screenshot proof.

Protected sources are starter implementation of previously taught operations concepts, not new Python algorithms students must implement. Do not distribute instructor reference solutions with this repo.
