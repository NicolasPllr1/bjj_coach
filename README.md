# Fine-tuning an LLM into a BJJ Coach
Let's train an LLM into speaking like the great John Danaher, arguably one of the greatest BJJ coach.




## Training Data
John Danaher regularly write high quality posts on Instagram where he develops ideas around BJJ in his captions. 
We will download these captions and feed them into a pre-trained LLM for supervised fine-tuning.

## Pre-Trained Model
We will use Mistral7B model available on Hugging Face.

## Supervised fine-tuning
We will make use of QLoRA to greatly reduce both the computational cost and memory footprint of training. This modern technique is readily available in python through the peft librairy.

## Gradio App
We will build a small gradio app around this model.