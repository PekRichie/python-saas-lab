# Wildcard Webhook Eseménybusz & Hibaizoláció

- **Szint:** Medior
- **Fájlok:** `app.py`, `test_app.py`

## SaaS kontextus és cél
Topic-minta alapú (`invoice.*`) eseményelosztás úgy, hogy egy hibás feliratkozó ne állítsa le a többit.

## Futtatás és tesztelés
```bash
python3 -m unittest test_app.py -v
```
