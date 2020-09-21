#!/usr/bin/env bash

docker build -t template_fastapi:latest .

cat ./data/github_token.txt | docker login docker.pkg.github.com -u miragecentury --password-stdin

docker tag template_fastapi:latest docker.pkg.github.com/sysunicorns-info/template_fastapi/template_fastapi:latest

docker push docker.pkg.github.com/sysunicorns-info/template_fastapi/template_fastapi:latest
