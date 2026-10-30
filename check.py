from support import load, require, main


def signals():
    mapping = load('ops/signals.json')
    expected = dict(latency='latency_p95_seconds', traffic='requests_total',
                    errors='error_ratio', saturation='cpu_ratio')
    require(mapping == expected, 'Golden-signal mappings disagree with metric definitions in README.')
    metrics = load('fixtures/metrics.json')
    for signal, metric in mapping.items():
        print(f'{signal}: {metric}={metrics[metric]}')


def alert():
    cfg = load('ops/alert.json')
    require(cfg['metric'] == 'error_ratio', 'Alert must measure user-facing request error ratio, not CPU.')
    require(type(cfg['threshold']) in (int, float) and cfg['threshold'] == 0.05,
            'Agreed threshold is ratio 0.05, not percent 5.')
    require(type(cfg['window_seconds']) is int and cfg['window_seconds'] == 60,
            'Require six complete 10-second buckets (60 seconds).')
    require(cfg['runbook'] == 'ops/runbook.md', 'Use existing ops/runbook.md.')
    data = load('fixtures/scenarios.json')
    for name, expected in [('healthy', False), ('short_spike', False), ('sustained_errors', True)]:
        elapsed = 0
        fired = False
        for value in data[name][cfg['metric']]:
            elapsed = elapsed + data['sample_interval_seconds'] if value > cfg['threshold'] else 0
            fired |= elapsed >= cfg['window_seconds']
        print(f'{name}: {"FIRING" if fired else "QUIET"}')
        require(fired == expected, f'Unexpected alert result for {name}.')


def budget():
    w = load('fixtures/window.json')
    sli = 100 * (w['requests'] - w['errors']) / w['requests']
    allowed = w['requests'] * (1 - w['objective_percent'] / 100)
    print(f"window={w['window']}")
    print(f"requests={w['requests']} errors={w['errors']} SLO={w['objective_percent']}%")
    print(f'SLI={sli:.2f}% allowed_errors={allowed:.0f} remaining_budget={allowed-w["errors"]:.0f}')
    print('Analysis is NOT auto-graded. Explain SLI vs SLO and negative remaining budget in analysis.md.')


if __name__ == '__main__':
    raise SystemExit(main(dict(signals=signals, alert=alert, budget=budget)))
