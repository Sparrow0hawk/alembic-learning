#!/usr/bin/env bash

set -x
set -eo pipefail

docker stop database

docker rm database
