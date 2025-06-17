
import spacy
from spacy.tokens import DocBin
import sys

nlp = spacy.blank("sk")
db = DocBin().from_disk(sys.argv[1])
with open(sys.argv[2], "w", encoding="utf8") as out_f:
    for doc in db.get_docs(nlp.vocab):
        out_f.write(doc.text.strip().replace("\n", " ") + "\n")