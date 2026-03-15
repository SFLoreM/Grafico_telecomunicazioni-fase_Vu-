# Grafico_telecomunicazioni-fase_Vu-
codice per la realizzazione del grafico del punto 4 della realizzazione di telecomunicazioni 

Questo script serve per generare i grafici della relazione sul doppino telefonico (33.5 metri). Usa i dati misurati in laboratorio per creare i diagrammi di Bode e la simulazione della distorsione dell'onda.

Cosa serve per farlo girare

Per usare questo script devi avere Python installato. 
```bash
pip install numpy matplotlib scipy

```

come si usa 

1. Scarica il file `main.py` nella tua cartella.
2. Apri il terminale nella cartella del progetto.
3. Lancia lo script con:
```bash
python main.py

```

Cosa genera

Una volta eseguito, lo script crea automaticamente due immagini:

* **bode_plot.png**: Mostra come cambiano l'attenuazione e la fase al variare della frequenza (i dati sono presi dalla nostra tabella di laboratorio).
* **distorsione_onda.png**: Mostra l'effetto "arrotondato" dell'onda quadra causato dal cavo, proprio come l'abbiamo visto sull'oscilloscopio.

Modificare i dati

Se vuoi cambiare i valori (perché magari i tuoi sono diversi da quelli nella tabella), apri il file `main.py` con un editor di testo e modifica i numeri dentro gli array `frequencies`, `attenuation` e `phase`.

---
