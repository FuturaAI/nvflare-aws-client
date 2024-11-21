# Advanced Notebooks NVFlare
Notebooks e risorse per l'inferenza su modelli addestrati con training federato standard e crittografia omomorfica (HE).

## Struttura
```
advanced_nvflare/
├── models/                      # Directory per i modelli addestrati
├── tenseal_context/            # Directory per contesti di crittografia
├── test/                       # Dataset di test per l'inferenza
├── nvflare_inference.ipynb     # Inferenza standard
└── nvflare_inference_HE.ipynb  # Inferenza per modelli HE
```

## Notebooks Disponibili
### nvflare_inference.ipynb
- Inferenza su modelli addestrati con training federato standard
- Caricamento diretto dei modelli PyTorch
- Non richiede componenti di crittografia

### nvflare_inference_HE.ipynb
- Inferenza su modelli addestrati con crittografia omomorfica
- Richiede i contesti di crittografia appropriati
- Utilizza TenSEAL per la gestione dei modelli crittografati

## Directory di Supporto
### models/
- Contiene i modelli addestrati
- Supporta sia modelli standard che HE
- I modelli devono essere copiati qui dopo il training

### tenseal_context/
- Contiene i contesti necessari per la crittografia omomorfica
- Richiesto solo per l'inferenza HE
- Deve contenere i file di contesto appropriati per la decrittografia
- Il file presente è solo un esempio, è da sostituire con il client_context.tenseal di uno dei client usato nel training di NVFlare

### test/
- Dataset di test per la validazione dei modelli
- Utilizzato da entrambi i notebook per l'inferenza
- Struttura attesa: immagini organizzate per classe in sottocartelle

## Utilizzo
1. Copiare il modello addestrato nella cartella `models/`
2. Per HE: assicurarsi che i contesti di crittografia siano in `tenseal_context/`
3. Inserire il dataset di test nella cartella `test/`
4. Eseguire il notebook appropriato in base al tipo di modello

## Note
- I notebook testano fino a 1000 immagini per default
- I risultati includono predizioni per singola immagine e accuratezza globale
- Verificare sempre la corrispondenza tra il tipo di modello e il notebook utilizzato

## ⚠️ Gestione Path
- I path nei notebook sono relativi alla root `advanced_nvflare/`:
  ```python
  test_data_folder = "./test/"
  model_path = "./models/model_name.pt"
  context_path = "./tenseal_context/client_context.tenseal"  # Solo per HE
  ```