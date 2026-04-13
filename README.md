<div align="center">
  <img src="https://cdn.pensieriincodice.it/images/pensieriincodice-locandina.png" alt="Logo Progetto" width="150"/>
  <h1>Pensieri in codice — Episode to LinkedIn</h1>
  <p>GitHub Action che pubblica automaticamente i nuovi episodi del podcast su LinkedIn.</p>
  <p>
    <img src="https://img.shields.io/github/stars/valeriogalano/pensieriincodice-episode-to-linkedin?style=for-the-badge" alt="GitHub Stars"/>
    <img src="https://img.shields.io/github/forks/valeriogalano/pensieriincodice-episode-to-linkedin?style=for-the-badge" alt="GitHub Forks"/>
    <img src="https://img.shields.io/github/last-commit/valeriogalano/pensieriincodice-episode-to-linkedin?style=for-the-badge" alt="Last Commit"/>
    <a href="https://pensieriincodice.it/sostieni" target="_blank" rel="noopener noreferrer">
      <img src="https://img.shields.io/badge/sostieni-Pensieri_in_codice-fb6400?style=for-the-badge" alt="Sostieni Pensieri in codice"/>
    </a>
  </p>
</div>

---

## Come funziona

Il workflow controlla il feed RSS del podcast e pubblica i nuovi episodi sull'account LinkedIn tramite le API ufficiali. L'ultimo episodio pubblicato viene tracciato tramite la variabile GitHub `LAST_PUBLISHED_URL` per evitare duplicati. Il workflow può essere attivato manualmente dalla scheda Actions.

> **Nota sull'autenticazione:** Le API di LinkedIn non restituiscono un `refresh_token`. L'`access_token` ha validità di 60 giorni e richiede un rinnovo manuale periodico tramite lo script `auth.py` del repository [readwise-to-linkedin](https://github.com/valeriogalano/pensieriincodice-news-to-linkedin).

### Monitoraggio scadenza token

Il workflow controlla ad ogni esecuzione la variabile `TOKEN_CREATED_AT` per verificare la scadenza del token (60 giorni):

- **≤10 giorni alla scadenza** → warning nel log della build
- **≤5 giorni alla scadenza** → errore, la build fallisce con messaggio chiaro

`TOKEN_CREATED_AT` viene aggiornato automaticamente quando si rinnova il token tramite `auth.py` (se questo repository è configurato in `GH_CSV`).

---

## Requisiti

- Python 3.11+
- Un account LinkedIn con applicazione OAuth configurata
- Un feed RSS del podcast

---

## Installazione e configurazione

### 1. Clona la repository

```bash
git clone https://github.com/YOUR_USERNAME/pensieriincodice-episode-to-linkedin.git
cd pensieriincodice-episode-to-linkedin
```

### 2. Sviluppo locale (opzionale)

Per eseguire lo script in locale, crea e attiva un virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 3. Configura i secrets di GitHub Actions

In **Settings → Secrets and variables → Actions**, aggiungi i seguenti **Secrets**:

| Secret | Descrizione |
|---|---|
| `LINKEDIN_ACCESS_TOKEN` | Access token LinkedIn (validità 60 giorni) |
| `LINKEDIN_PERSON_URN` | URN personale dell'account LinkedIn |

### 4. Configura le variabili di GitHub Actions

Nella stessa sezione, sotto la scheda **Variables**, aggiungi:

| Variabile | Descrizione |
|---|---|
| `PODCAST_RSS_URL` | URL del feed RSS del podcast |
| `LINKEDIN_MESSAGE_TEMPLATE` | Template del messaggio da pubblicare |
| `TOKEN_CREATED_AT` | Data di creazione del token LinkedIn (formato `YYYY-MM-DD`) |

### 5. Template del messaggio

I placeholder disponibili sono `{title}` e `{link}`. Esempio:

```
Nuovo episodio di Pensieri in codice!

{title}

Ascoltalo qui: {link}

#Podcast #Tech #Informatica
```

---

## Contributi

Se noti qualche problema o hai suggerimenti, sentiti libero di aprire una **Issue** e successivamente una **Pull Request**. Ogni contributo è ben accetto!

---

## Importante

Vorremmo mantenere questo repository aperto e gratuito per tutti, ma lo scraping del contenuto di questo repository **NON È CONSENTITO**. Se ritieni che questo lavoro ti sia utile e vuoi utilizzare qualche risorsa, ti preghiamo di citare come fonte il podcast e/o questo repository.
