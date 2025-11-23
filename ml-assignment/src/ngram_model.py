import random
import re

class TrigramModel:
    def __init__(self):
        """
        Initializes the TrigramModel.
        """
        self.trigrams = {}  # (word1, word2) -> {word3: count}
        
    def fit(self, text):
        """
        Trains the trigram model on the given text.

        Args:
            text (str): The text to train the model on.
        """
        if not text:
            return
            
        # Clean and tokenize
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        words = text.split()
        
        if not words:
            return
        
        # Pad with start and end tokens
        words = ['<s>', '<s>'] + words + ['</s>']
        
        # Count trigrams
        for i in range(len(words) - 2):
            w1, w2, w3 = words[i], words[i+1], words[i+2]
            context = (w1, w2)
            if context not in self.trigrams:
                self.trigrams[context] = {}
            self.trigrams[context][w3] = self.trigrams[context].get(w3, 0) + 1

    def generate(self, max_length=50):
        """
        Generates new text using the trained trigram model.

        Args:
            max_length (int): The maximum length of the generated text.

        Returns:
            str: The generated text.
        """
        if not self.trigrams:
            return ""
        
        words = ['<s>', '<s>']
        
        for _ in range(max_length):
            context = (words[-2], words[-1])
            
            if context not in self.trigrams:
                break
                
            # Get possible next words and their counts
            next_words = self.trigrams[context]
            total_count = sum(next_words.values())
            
            # Probabilistic selection
            rand = random.random() * total_count
            cumulative = 0
            for word, count in next_words.items():
                cumulative += count
                if rand <= cumulative:
                    words.append(word)
                    if word == '</s>':
                        break
                    break
        
        # Remove start tokens and end token, return as string
        result = [w for w in words[2:] if w != '</s>']
        return ' '.join(result)
