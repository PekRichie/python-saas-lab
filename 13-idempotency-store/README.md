# Idempotency-Key kezelő fizetési végpontokhoz

- **Szint:** Medior
- **Fájlok:** `app.py`, `test_app.py`

## SaaS kontextus és cél
Dupla terhelés és ismételt POST kérések elleni védelem idempotencia-kulcs alapú válasz-visszajátszással.

## Futtatás és tesztelés
```bash
python3 -m unittest test_app.py -v
```
