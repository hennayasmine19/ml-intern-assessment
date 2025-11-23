# Evaluation

## Design Choices for Trigram Language Model

### N-gram Count Storage

I chose to store trigram counts using a nested dictionary structure: `{(word1, word2): {word3: count}}`. This design provides O(1) lookup time for context pairs and allows efficient access to all possible next words for a given context. The tuple `(word1, word2)` serves as the key representing the context, while the inner dictionary maps each possible next word to its frequency count. This structure is memory-efficient and enables fast probabilistic sampling during text generation.

### Text Cleaning and Preprocessing

The text cleaning process involves two main steps:
1. **Lowercasing**: All text is converted to lowercase to ensure consistency and reduce vocabulary size by treating words with different cases as the same token.
2. **Punctuation Removal**: All punctuation marks are removed using a regex pattern `[^\w\s]`, which keeps only alphanumeric characters and whitespace. This simplifies tokenization and focuses the model on word-level patterns rather than punctuation-specific contexts.

After cleaning, the text is tokenized by splitting on whitespace, creating a list of words ready for n-gram extraction.

### Padding Strategy

The model uses two start tokens (`<s> <s>`) at the beginning and one end token (`</s>`) at the end of each sequence. This padding strategy ensures that:
- The first two words in the text have proper context for trigram formation
- Sentence boundaries are clearly marked, allowing the model to learn when sentences naturally end
- The generation process can start from a consistent initial state

### Unknown Words Handling

The current implementation does not explicitly handle unknown words during training. All words in the training corpus are treated as known. During generation, if a context pair is not found in the trained model, generation stops gracefully. This is a simple approach that works well for closed-domain text generation where the vocabulary is limited to the training corpus.

### Probabilistic Generation

The `generate` function implements probabilistic sampling using cumulative distribution sampling:
1. For each context `(w1, w2)`, retrieve all possible next words and their counts
2. Calculate the total count for normalization
3. Generate a random number between 0 and the total count
4. Iterate through words, accumulating counts until the random number is reached
5. Select the word at which the cumulative count exceeds the random threshold

This approach ensures that words are selected proportionally to their frequency in the training data, creating more natural and varied text generation compared to always selecting the most frequent word. The generation stops when the end token `</s>` is encountered or when the maximum length is reached, or when an unknown context is encountered.

### Trade-offs and Future Improvements

The current implementation prioritizes simplicity and correctness. Potential improvements could include:
- Additive smoothing (Laplace smoothing) to handle unseen n-grams
- Explicit unknown word token (`<UNK>`) for out-of-vocabulary words
- Backoff strategies when a context is not found
- More sophisticated text cleaning that preserves sentence boundaries
