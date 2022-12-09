### Prepare optimized models

```bash
python app/optimizer.py
rm -rf app/model_weights/*coder.onnx
```


### Test app locally

```bash
uvicorn app.main.app --reload
```


### Example

```
context: Donald Trump is an American media personality and businessman who served as the 45th president of the United States
answer: Donald Trump
```


### Build Dockerfile locally to test

```bash
docker build -t t5_qa .
docker run --name t5_qna -p 80:80 t5_qa
```


### Google cloud setup

1. Setup a project, copy the project id and enable container registry
2. `gcloud init`
3. `docker build . --tag gcr.io/{project_id=t5qa-371015}/t5_qa:latest`
4. `docker push gcr.io/t5qa-371015/t5_qa:latest`
5. If auth error comes up: `gcloud auth configure-docker`
6. `gcloud run deploy --image gcr.io/t5qa-371015/t5_qa:latest --cpu 2 --concurrency 1 --memory 4Gi --platform managed --min-instances 0 --timeout 1m --port 80`
7. Get the url and try requesting to it


### Tutorial

https://youtu.be/OzV21spbCfI
