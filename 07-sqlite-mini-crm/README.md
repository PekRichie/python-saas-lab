# SQLite Mini-CRM & Multi-Tenant Adattár

- **Szint:** Junior+
- **Fájlok:** `app.py`, `test_app.py`

## SaaS kontextus és cél
Paraméterezett SQLite CRUD adattár szigorú `tenant_id` szűréssel (SQL-injection és adatszivárgás ellen).

## Futtatás és tesztelés
```bash
python3 -m unittest test_app.py -v
```
