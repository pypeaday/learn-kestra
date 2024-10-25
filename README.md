# Learn Kestra

My repo for learning [kestra](https://kestro.io)

## Getting Started

`docker compose up -d` will get you a nice ui at `http://localhost:8080`

[flows.yml](./flows.yml) illustrates two example flows and how to use some outputs and secrets.

[Secrets in Kestra](https://kestra.io/docs/concepts/secret) have to be base64 encoded and can be passed to flows by setting `SECRET_<environment variable key>=<base64 encoded secret>`

See [.env.example](./.env.example) for setting env variables needed to use Minio.

You need a `.env` then you need to `just encode` to get `.env_encoded` which will be used with docker compose
