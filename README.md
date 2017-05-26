## Run Container locally

```bash
docker build -t ml-api .
docker run -d -p 5020:5020 ml-api
curl http://localhost:5020/version
```