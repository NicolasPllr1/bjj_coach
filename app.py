import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import sys


def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", max_length=500, truncation=True)
    outputs = model.generate(**inputs)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text


def load_model(model_name):
    # Load the chosen fine-tuned model and its tokenizer

    TOKENIZERS_PATH = ""  # path to the fine-tuned tokenizer
    MODELS_PATH = ""  # path to the fine-tuned model
    try:
        model = AutoModelForCausalLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        return model, tokenizer
    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)


def gradio_app(model_name):
    # Load the model and its tokenizer
    global model, tokenizer
    model, tokenizer = load_model(model_name)

    # Create Gradio Interface
    iface = gr.Interface(
        fn=generate_text,
        inputs="text",
        outputs="text",
        live=True,
        title="Your BJJ Coach",
        description="Ask your BJJ coach a question",
    )

    # Launch Gradio Interface
    iface.launch()


# python app.py model_name
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app.py <model_name>")
        sys.exit(1)

    # Retrieve the model name from the command line
    model_name_arg = sys.argv[1]

    # Launch the Gradio interface
    gradio_app(model_name_arg)
