from fastT5 import generate_onnx_representation, quantize
from transformers import AutoTokenizer, T5Config

if __name__ == "__main__":
    trained_model_path = "ramsrigouthamg/t5_squad_v1"
    output_path = "app/model_weights"

    onnx_model_paths = generate_onnx_representation(
        trained_model_path, output_path=output_path
    )
    quant_model_paths = quantize(onnx_model_paths)

    tokenizer_onnx = AutoTokenizer.from_pretrained(trained_model_path)
    config = T5Config.from_pretrained(trained_model_path)
    tokenizer_onnx.save_pretrained(output_path)
    config.save_pretrained(output_path)
