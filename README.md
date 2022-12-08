# Prepare optimized models
```bash
python app/optimizer.py
rm -rf model_weights/*coder.onnx
```

# Test app locally
```bash
uvicorn app.main.app --reload
```

## Example
```
context: Donald Trump is an American media personality and businessman who served as the 45th president of the United States
answer: Donald Trump
```

## Build Dockerfile locally to test

docker build -t t5_qa .
docker run --name t5_qna -p 80:80 t5_qa