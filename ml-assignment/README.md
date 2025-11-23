# Trigram Language Model

This directory contains the core assignment files for the Trigram Language Model.

## How to Run

### Prerequisites

Install the required dependencies:
```bash
pip install pytest
```

### Training and Generating Text

1. **Using the example corpus:**
   ```bash
   cd ml-assignment
   python src/generate.py
   ```

2. **Using your own text:**
   ```python
   from src.ngram_model import TrigramModel
   
   model = TrigramModel()
   with open("your_text_file.txt", "r") as f:
       text = f.read()
   model.fit(text)
   generated_text = model.generate(max_length=100)
   print(generated_text)
   ```

### Running Tests

From the root directory:
```bash
python -m pytest ml-assignment/tests/test_ngram.py -v
```

Or from the `ml-assignment` directory:
```bash
cd ml-assignment
python -m pytest tests/test_ngram.py -v
```

## Design Choices

Please see `evaluation.md` for a detailed summary of design decisions and implementation choices.
