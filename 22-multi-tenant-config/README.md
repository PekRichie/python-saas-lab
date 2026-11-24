# Többszintű Multi-Tenant Konfiguráció-feloldó

- **Szint:** Medior
- **Fájlok:** `app.py`, `test_app.py`

## SaaS kontextus és cél
Hierarchikus beállítás-feloldás: globális alapérték → előfizetési csomag → egyedi ügyfél-felülírás.

## Futtatás és tesztelés
```bash
python3 -m unittest test_app.py -v
```
