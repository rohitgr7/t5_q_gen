from pathlib import Path

from fastT5 import OnnxT5, get_onnx_runtime_sessions
from transformers import AutoTokenizer


def get_model_and_tokenizer(weights_path):
    weights_path = Path("model_weights")

    encoder_path = weights_path / "t5_squad_v1-encoder-quantized.onnx"
    decoder_path = weights_path / "t5_squad_v1-decoder-quantized.onnx"
    init_decoder_path = weights_path / "t5_squad_v1-init-decoder-quantized.onnx"

    onnx_sessions = get_onnx_runtime_sessions(
        (encoder_path, decoder_path, init_decoder_path)
    )
    model = OnnxT5(weights_path, onnx_model_sessions=onnx_sessions)
    tokenizer = AutoTokenizer.from_pretrained(weights_path)
    return model, tokenizer


def generate_question(context, answer, model, tokenizer):
    text = f"context: {context} answer: {answer}"
    max_len = 256
    encoding = tokenizer.encode_plus(
        text, max_length=max_len, pad_to_max_length=True, return_tensors="pt"
    )

    input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

    outs = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        early_stopping=True,
        num_beams=5,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        max_length=300,
    )

    dec = [tokenizer.decode(ids, skip_special_tokens=True) for ids in outs]
    question = dec[0].replace("question:", "").strip()
    return question
