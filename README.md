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

Il workflow controlla il feed RSS del podcast e pubblica i nuovi episodi sull'account LinkedIn tramite le API ufficiali. Gli episodi già pubblicati vengono tracciati per evitare duplicati. Il workflow può essere attivato anche manualmente dalla scheda Actions.

> **Nota sull'autenticazione:** Le API di LinkedIn non restituiscono un `refresh_token`. L'`access_token` ha validità di 60 giorni e richiede un rinnovo manuale periodico.

---

## Requisiti

- Un account LinkedIn con applicazione OAuth configurata
- Uno o più feed RSS di podcast

---

## Installazione e configurazione

### 1. Clona la repository

```bash
git clone https://github.com/YOUR_USERNAME/pensieriincodice-episode-to-linkedin.git
cd pensieriincodice-episode-to-linkedin
```

### 2. Configura i secrets di GitHub Actions

In **Settings → Secrets and variables → Actions**, aggiungi i seguenti **Secrets**:

| Secret | Descrizione |
|---|---|
| `LINKEDIN_ACCESS_TOKEN` | Access token LinkedIn (validità 60 giorni) |
| `LINKEDIN_PERSONAL_URN` | URN personale dell'account LinkedIn |

### 3. Configura le variabili di GitHub Actions

Nella stessa sezione, sotto la scheda **Variables**, aggiungi:

| Variabile | Descrizione |
|---|---|
| `PODCAST1_RSS_URL` | URL del feed RSS del primo podcast |
| `PODCAST1_TEMPLATE` | Template del messaggio per il primo podcast |

### 4. Template del messaggio

I placeholder disponibili sono `{title}` e `{link}`. Esempio:

```
🎙️ Nuovo episodio di Pensieri in codice!

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
