import glob, re, random
from typing import List
from collections import Counter

import naive_bayes_practice as nb
import machine_learning_practice as ml

path = r'D:\Data\experiment\git_hub\data-science-from-scratch\scratch_practice\spam_data\*\**'

data: List[nb.Message] = []

for filename in glob.glob(path):
    is_spam = "ham" not in filename

    with open(filename, errors='ignore') as email_file:
        for line in email_file:
            if line.startswith("Subject: "):
                subject  = line.lstrip("Subject: ")
                data.append(nb.Message(subject, is_spam))
                break

random.seed(0)
train_messages, test_messages = ml.split_data(data, 0.75)

model = nb.NaiveBayesClassifier()
model.train(train_messages)

predictions = [(message, model.predict(message.text))
               for message in test_messages]

# Assume that spam_probability > 0.5 corresponds to spam prediction
# and count the combinations of (actual is_spam, predicted is_spam)
confusion_matrix = Counter((message.is_spam, spam_probability > 0.5)
                           for message, spam_probability in predictions)

print(confusion_matrix)

words = sorted(model.tokens, key=lambda t: nb.p_spam_given_token(t, model))

print("spammiest_words", words[-10:])
print("hammiest_words", words[:10])
