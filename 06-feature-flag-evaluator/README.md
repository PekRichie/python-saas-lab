# Feature Flag & Százalékos Rollout kiértékelő

- **Szint:** Medior
- **Fájlok:** `app.py`, `test_app.py`

## SaaS kontextus és cél
Determinisztikus hash-alapú fokozatos funkcióbevezetés (canary rollout) és ügyfél-whitelist kezelés.

## Futtatás és tesztelés
```bash
python3 -m unittest test_app.py -v
```
