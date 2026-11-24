# SaaS Jóváhagyási Állapotgép (Workflow State Machine)

- **Szint:** Medior
- **Fájlok:** `app.py`, `test_app.py`

## SaaS kontextus és cél
Szigorú átmenet-szabályokkal védett üzleti folyamatgép (`draft → review → approved / rejected → archived`).

## Futtatás és tesztelés
```bash
python3 -m unittest test_app.py -v
```
