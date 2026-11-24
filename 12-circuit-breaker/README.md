# Circuit Breaker külső API-hívásokhoz

- **Szint:** Medior
- **Fájlok:** `app.py`, `test_app.py`

## SaaS kontextus és cél
Külső szolgáltatás kiesésekor automatikusan nyitó megszakító (CLOSED → OPEN → HALF_OPEN).

## Futtatás és tesztelés
```bash
python3 -m unittest test_app.py -v
```
