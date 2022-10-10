#!/bin/bash

set -eu

docker build -t registry.heroku.com/sisnat/web ./sisnat -f ./sisnat/Dockerfile.heroku \
    && docker push registry.heroku.com/sisnat/web \
    && heroku container:release -a sisnat web
