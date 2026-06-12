"""
app.py

Purpose:
Creates a Gradio web interface for the Medical Assistant Study Guide chatbot.
"""

import gradio as gr
from query import ask


def handle_query(question):
    """
    Sends the user question to the RAG pipeline and returns:
    1. The generated answer
    2. The retrieved source list
    """

    if not question.strip():
        return "Please enter a question.", ""

    result = ask(question)

    sources = "\n".join(f"• {source}" for source in result["sources"])

    return result["answer"], sources


with gr.Blocks() as demo:
    gr.Markdown("# Medical Assistant Study Guide Chatbot")
    gr.Markdown("Ask a study question about medical assisting topics such as HIPAA, vital signs, anatomy, EKGs, phlebotomy, or lab tests.")

    inp = gr.Textbox(label="Your question", placeholder="Example: What is a normal adult heart rate?")

    btn = gr.Button("Ask")

    answer = gr.Textbox(label="Answer", lines=8)

    sources = gr.Textbox(label="Retrieved from", lines=5)

    btn.click(handle_query, inputs=inp, outputs=[answer, sources])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])


if __name__ == "__main__":
    demo.launch()