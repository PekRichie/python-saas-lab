# Háttérfeladat-sor újrapróbálással és Dead-Letter Queue-val

- **Szint:** Medior
- **Fájlok:** `app.py`, `test_app.py`

## SaaS kontextus és cél
Megbízható háttérfeldolgozó sor (retry + maximális próbálkozás után DLQ-ba sorolás).

## Futtatás és tesztelés
```bash
python3 -m unittest test_app.py -v
```
