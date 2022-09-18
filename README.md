# simple-python-server

## Instale o Docker

```bash
# Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository    "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update -y
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
sudo usermod -aG docker $USER
docker --version
```

## Buildar Img e Executar Container
```bash
sudo docker build -t api .
sudo docker run -p 8080:8080 -e FLASK_APP=api.py api:latest
# em outro terminal, faca uma requisicao http
curl -X GET 0.0.0.0:8080/get_hello_world
```

