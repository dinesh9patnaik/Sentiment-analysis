import transformers

DEVICE = "cuda"
MAX_LEN =64
TRAIN_BATCH_SIZE=8
VALID_BATCH_SIZE=4
EPOCHS=10
BERT_PATH ="/content/input/bert-base-uncased/"
MODEL_PATH="/content/src/model.bin"
TRAINING_FILE ="/content/input/IMDB.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(BERT_PATH,do_lower_case_="True")