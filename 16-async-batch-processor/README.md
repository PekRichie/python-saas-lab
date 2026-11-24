# Aszinkron kötegelt adatfeldolgozó (`asyncio` + Semaphore)

- **Szint:** Medior
- **Fájlok:** `app.py`, `test_app.py`

## SaaS kontextus és cél
Párhuzamossági korláttal (`asyncio.Semaphore`) védett aszinkron munkafolyamat külső API-k kímélésére.

## Futtatás és tesztelés
```bash
python3 -m unittest test_app.py -v
```
