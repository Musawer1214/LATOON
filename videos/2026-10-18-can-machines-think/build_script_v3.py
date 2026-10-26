# Rebuild script.json from v3 (v3_en.json text + dub/voice_en/timings_v3.json real voice times + plan/shots_v3.json visuals if present).
# Old v2 script.json kept as script_v2_obsolete.json.
import json, os
B = os.path.dirname(os.path.abspath(__file__))
v3 = json.load(open(f'{B}/v3_en.json')); tm = json.load(open(f'{B}/dub/voice_en/timings_v3.json'))
T = {c['id']: c for c in tm['cards']}
shots = {}
if os.path.exists(f'{B}/plan/shots_v3.json'):
    for s in json.load(open(f'{B}/plan/shots_v3.json'))['shots']:
        shots.setdefault(s['card'], []).append(s)
order = [c['id'] for s in v3['sections'] for c in s['cards']]
lines = []
for s in v3['sections']:
    for c in s['cards']:
        t = T[c['id']]; i = order.index(c['id'])
        nxt = T[order[i + 1]]['start'] if i + 1 < len(order) else None
        sh = shots.get(c['id'], [])
        lines.append({'id': c['id'], 'chapter': s['id'], 'chapter_title': s['title'], 'start_s': t['start'], 'end_s': t['end'],
                      'dur_s': t['dur'], 'pause_after_s': round(nxt - t['end'], 2) if nxt else None, 'words': t['n_words'],
                      'text': c['en'], 'visual': ' | '.join(f"{x['id']}: {x['see']}" for x in sh),
                      'shots': [x['id'] for x in sh], 'tool': sorted({x['tool'] for x in sh})})
mm = lambda x: f"{int(x // 60)}:{int(x % 60):02d}"
end_hold, quote, endf = 2.0, 7.0, 12.0
total = tm['cards'][-1]['end'] + end_hold + quote + endf
meta = {'title_working': 'Can Machines Think?', 'series': 'Big Questions', 'version': 'v3 2026-10-26 (owner final Urdu v3; EN final)',
        'status': 'SCRIPT v3 FINAL; English voiced (Lite Iapetus, ~168 wpm accepted by owner); timings = real voice (timings_v3.json)',
        'narrator': 'EN Gemini Iapetus (gemini-3.8-flash-lite-tts); UR/PS owner own voice (pending)',
        'closing_line_rule': 'LATOON / Voyaging the Unseen shown on the end frame, never spoken (PLAYBOOK s4.3)',
        'visual_rule': 'Golden Rule s5.0b: visuals designed per idea (CONCEPT.md v3); language-neutral labels only; no burned captions',
        'stats': {'spoken_words': sum(l['words'] for l in lines), 'cards': len(lines), 'narration_s': tm['meta']['total_s'],
                  'speech_ends_s': tm['cards'][-1]['end'], 'closing': {'hold_s': end_hold, 'silent_quote_s': quote, 'end_frame_s': endf},
                  'est_runtime_s': round(total, 1), 'est_runtime': mm(total)},
        'chapters': [{'id': s['id'], 'title': s['title'], 'start': mm(max(0, s['start'] - 1.0)), 'start_s': s['start']} for s in tm['sections']]}
json.dump({'meta': meta, 'lines': lines}, open(f'{B}/script.json', 'w'), indent=1, ensure_ascii=False)
print(meta['stats'])
