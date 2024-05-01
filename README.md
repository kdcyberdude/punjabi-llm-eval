# PunjabiLLM eval

## What is currently covered:

* Common sense reasoning: `Hellaswag`, `Winogrande`, `PIQA`, `OpenbookQA`, `ARC-Easy`, `ARC-Challenge`
* World knowledge: `NaturalQuestions`, `TriviaQA`
* Reading comprehension: `BoolQ`
* Alpaca dataset

## Run translation

Finally run (note `model`, `translation_project_id` and `model_args` are not important for us but we need to specify them):

```
python main.py \
    --model hf \
    --model_args pretrained=mistralai/Mistral-7B-v0.1 \
    --tasks hellaswag \
    --translation_project_id 123
    --char_limit 500000
    --start_from_doc_index 0
```

## Contact
You can find me `@kdcyberdude`

For any queries regarding the work, please reach out at kdsingh.cyberdude@gmail.com or https://linkedin.com/in/kdcyberdude
