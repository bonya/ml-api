## Run Container locally

```bash
docker build -t ml-api .
docker run -d -p 5000:5000 ml-api
curl http://localhost:5000/version
```