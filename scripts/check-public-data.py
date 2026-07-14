#!/usr/bin/env python3
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
FILES = [ROOT / 'docs/data/project.json', ROOT / 'docs/data/exchanges.json']
errors = []

for path in FILES:
    try:
        json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{path}: invalid JSON: {exc}')

project = json.loads(FILES[0].read_text(encoding='utf-8'))
exchanges = json.loads(FILES[1].read_text(encoding='utf-8'))
required = {'schema_version','repository_url','status','status_label','status_title','status_description','current_exchange','cash_used_yen','public_personal_data_count','offers_open','current_item'}
missing = required - set(project)
if missing:
    errors.append(f'project.json missing keys: {sorted(missing)}')

numbers = [x.get('number') for x in exchanges]
if numbers != sorted(numbers) or len(numbers) != len(set(numbers)):
    errors.append('exchange numbers must be unique and sorted')

text = '\n'.join(p.read_text(encoding='utf-8') for p in FILES)
patterns = {
    'email address': r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
    'Japanese postal code': r'\b\d{3}-\d{4}\b',
    'phone-like number': r'(?<!\d)0\d{1,4}-\d{1,4}-\d{3,4}(?!\d)',
    'tracking-number field': r'"(?:tracking|tracking_number|phone|email|address|postal_code|real_name)"\s*:',
}
for label, pattern in patterns.items():
    if re.search(pattern, text, re.I):
        errors.append(f'possible {label} found in public data')

if project.get('public_personal_data_count') != 0:
    errors.append('public_personal_data_count must remain 0')

if errors:
    print('Public data validation failed:')
    for error in errors:
        print(f'- {error}')
    sys.exit(1)
print('Public data validation passed.')
