# Python SaaS Lab — 24 Junior → Medior SaaS Alkalmazás 🐍

**24 önálló, tesztelt, tiszta Python 3 (stdlib-only) SaaS építőkockát és kisalkalmazást** tartalmazó portfólió repó — hitelesítés, rate limiting, számlázás, multi-tenancy, audit hash-lánc, circuit breaker, BM25 keresés, aszinkron feldolgozás és AI költségbecslés.

🌐 Portfólió: [cuppashot.hu](https://cuppashot.hu) · 👤 Készítette: **Pék Richárd**

## Összes teszt futtatása egyetlen paranccsal
```bash
python3 run_all_tests.py
```

## Projektek (24 db)

| # | Alkalmazás | Szint | Leírás |
|---|---|---|---|
| `01` | **[API-kulcs generátor és HMAC-ellenőrző](./01-api-key-manager/)** | Junior | Biztonságos, prefixelt SaaS API-kulcsok (pl. `cs_live_...`) generálása, SHA-256 hash-alapú tárolása és konstans idejű ellenőrzése. |
| `02` | **[Token Bucket API Rate Limiter](./02-token-bucket-rate-limiter/)** | Junior+ | Ügyfelenkénti (per-tenant) API kéréskorlátozó determinisztikus időforrással a túlterhelés ellen. |
| `03` | **[Webhook HMAC-SHA256 aláíró és ellenőrző](./03-webhook-hmac-signer/)** | Junior+ | Stripe-stílusú időbélyeges webhook aláírás és replay-támadás elleni időablak ellenőrzés. |
| `04` | **[SaaS előfizetés-árazó és időarányosítás (Proration)](./04-subscription-proration/)** | Junior+ | Csomagváltáskor (upgrade/downgrade) pontos, napra lebontott időarányos különbözet és ÁFA számítás. |
| `05` | **[RBAC jogosultságkezelő motor](./05-rbac-policy-engine/)** | Junior+ | Szerepkör-alapú hozzáférés-vezérlés wildcard támogatással (`projects:*`) és tenant-szintű ellenőrzéssel. |
| `06` | **[Feature Flag & Százalékos Rollout kiértékelő](./06-feature-flag-evaluator/)** | Medior | Determinisztikus hash-alapú fokozatos funkcióbevezetés (canary rollout) és ügyfél-whitelist kezelés. |
| `07` | **[SQLite Mini-CRM & Multi-Tenant Adattár](./07-sqlite-mini-crm/)** | Junior+ | Paraméterezett SQLite CRUD adattár szigorú `tenant_id` szűréssel (SQL-injection és adatszivárgás ellen). |
| `08` | **[TTL + LRU API Válasz-gyorsítótár](./08-ttl-lru-cache/)** | Medior | Lejárati idővel (TTL) és maximális elemszámmal (LRU kilakoltatás) rendelkező memóriabeli gyorsítótár. |
| `09` | **[Háttérfeladat-sor újrapróbálással és Dead-Letter Queue-val](./09-worker-queue-dlq/)** | Medior | Megbízható háttérfeldolgozó sor (retry + maximális próbálkozás után DLQ-ba sorolás). |
| `10` | **[Használatalapú számlázás (Usage Metering)](./10-usage-metering/)** | Medior | API-hívás és AI-token fogyasztás mérése ügyfelenként, ingyenes keret + túllépési díj számítással. |
| `11` | **[Manipulációbiztos Audit Napló (SHA-256 Hash-lánc)](./11-audit-hash-chain/)** | Medior | Láncolt kriptográfiai hash-sel védett eseménynapló, amely azonnal jelzi az utólagos adatmódosítást. |
| `12` | **[Circuit Breaker külső API-hívásokhoz](./12-circuit-breaker/)** | Medior | Külső szolgáltatás kiesésekor automatikusan nyitó megszakító (CLOSED → OPEN → HALF_OPEN). |
| `13` | **[Idempotency-Key kezelő fizetési végpontokhoz](./13-idempotency-store/)** | Medior | Dupla terhelés és ismételt POST kérések elleni védelem idempotencia-kulcs alapú válasz-visszajátszással. |
| `14` | **[BM25 Dokumentum-kereső (Mini RAG előkészítő)](./14-mini-bm25-search/)** | Medior | Külső függőség nélküli BM25 relevancia-pontozó magyar/angol dokumentum-darabok (chunks) rangsorolására. |
| `15` | **[AI Prompt Sablonmotor és Token-költség Becslő](./15-prompt-cost-estimator/)** | Medior | Változó-behelyettesítéses prompt-sablon kezelő bemeneti/kimeneti token és USD költségbecsléssel. |
| `16` | **[Aszinkron kötegelt adatfeldolgozó (`asyncio` + Semaphore)](./16-async-batch-processor/)** | Medior | Párhuzamossági korláttal (`asyncio.Semaphore`) védett aszinkron munkafolyamat külső API-k kímélésére. |
| `17` | **[SLA & Rendelkezésre állás figyelő](./17-sla-uptime-tracker/)** | Junior+ | Incidens-időtartamokból számított havi SLA százalék és hiba-költségkeret (Error Budget) követő. |
| `18` | **[CSV Számlaadat-normalizáló és validátor](./18-csv-invoice-normalizer/)** | Junior | Vegyes formátumú CSV számlasorok tisztítása, összeg-validálás és hibás sorok elkülönítése. |
| `19` | **[SaaS Jóváhagyási Állapotgép (Workflow State Machine)](./19-workflow-state-machine/)** | Medior | Szigorú átmenet-szabályokkal védett üzleti folyamatgép (`draft → review → approved / rejected → archived`). |
| `20` | **[Mini REST API Router & Middleware lánc](./20-mini-rest-router/)** | Medior | FastAPI-ihletésű, külső függőség nélküli útválasztó és middleware lánc (request-ID, naplózás, hibakezelés). |
| `21` | **[JWT-szerű HMAC-SHA256 Aláírt Token Motor](./21-jwt-signed-token/)** | Medior | Stateless hitelesítési token generálás, base64url kódolás, HMAC-SHA256 aláírás és lejárati idő (`exp`) ellenőrzés. |
| `22` | **[Többszintű Multi-Tenant Konfiguráció-feloldó](./22-multi-tenant-config/)** | Medior | Hierarchikus beállítás-feloldás: globális alapérték → előfizetési csomag → egyedi ügyfél-felülírás. |
| `23` | **[XSS-védett Tranzakciós E-mail Sablonmotor](./23-email-template-engine/)** | Junior+ | HTML-escape-elt, kötelező változókat ellenőrző tranzakciós e-mail renderelő motor. |
| `24` | **[Wildcard Webhook Eseménybusz & Hibaizoláció](./24-webhook-event-bus/)** | Medior | Topic-minta alapú (`invoice.*`) eseményelosztás úgy, hogy egy hibás feliratkozó ne állítsa le a többit. |
