from io import BytesIO # So we can treat bytes as a file.
import requests
import tarfile

BASE_URL = "https://spamassassin.apache.org/old/publiccorpus"
FILES = ["20021010_easy_ham.tar.bz2",
         "20021010_hard_ham.tar.bz2",
         "20021010_spam.tar.bz2"]

OUTPUT_DIR = r'D:\Data\experiment\git_hub\data-science-from-scratch\scratch_practice\spam_data'

for filename in FILES:
    content = requests.get(f"{BASE_URL}/{filename}").content
    # Wrap the in-memory bytes so we can use them as a "file."
    fin = BytesIO(content)

    with tarfile.open(fileobj=fin, mode='r:bz2') as tf:
        tf.extractall(OUTPUT_DIR)