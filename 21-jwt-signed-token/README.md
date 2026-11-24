# JWT-szerű HMAC-SHA256 Aláírt Token Motor

- **Szint:** Medior
- **Fájlok:** `app.py`, `test_app.py`

## SaaS kontextus és cél
Stateless hitelesítési token generálás, base64url kódolás, HMAC-SHA256 aláírás és lejárati idő (`exp`) ellenőrzés.

## Futtatás és tesztelés
```bash
python3 -m unittest test_app.py -v
```
