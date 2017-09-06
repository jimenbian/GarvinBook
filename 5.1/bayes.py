from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier

newsTrainer = Trainer(tokenizer)

newsSet =[
    {'text': 'not to eat too much is not enough to lose weight', 'category': 'health'},
    {'text': 'Russia try to invade Ukraine', 'category': 'politics'},
    {'text': 'do not neglect exercise', 'category': 'health'},
    {'text': 'Syria is the main issue, Obama says', 'category': 'politics'},
    {'text': 'eat to lose weight', 'category': 'health'},
    {'text': 'you should not eat much', 'category': 'health'}
]
for news in newsSet:
    newsTrainer.train(news['text'], news['category'])

newsClassifier = Classifier(newsTrainer.data, tokenizer)

classification = newsClassifier.classify("eat more, you will become fatter")

print(classification)