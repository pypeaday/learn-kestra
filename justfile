encode:
    #!/bin/bash
    set -euo pipefail
    while IFS='=' read -r key value; do
        echo "SECRET_$key=$(echo -n "$value" | base64)";
    done < .env > .env_encoded
    while IFS='=' read -r key value; do
        echo "export $key=$(echo -n "$value")";
    done < .env > .envrc

restart:
    #! /bin/bash
    docker compose restart