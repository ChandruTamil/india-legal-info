#!/usr/bin/env python3
"""Rebuild worker.js by inlining index.html into its template literal."""
from pathlib import Path

root = Path(__file__).resolve().parent
index = (root / 'index.html').read_text(encoding='utf-8')
worker_tpl = (root / 'worker.js').read_text(encoding='utf-8')

marker = 'const INDEX = `'
start = worker_tpl.index(marker) + len(marker)
i = start
while True:
    j = worker_tpl.index('`', i)
    k = j + 1
    while k < len(worker_tpl) and worker_tpl[k] in ' \t':
        k += 1
    if k < len(worker_tpl) and worker_tpl[k] == ';':
        end = j
        break
    i = j + 1

escaped = index.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')
(root / 'worker.js').write_text(worker_tpl[:start] + escaped + worker_tpl[end:], encoding='utf-8')
print(f'synced index.html ({len(index)} chars) -> worker.js')
