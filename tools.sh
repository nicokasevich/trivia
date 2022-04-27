#!/bin/bash

install() {
  docker-compose up --build -d
  docker-compose run --rm app python3 manage.py migrate
  docker-compose run --rm app python3 manage.py addquestions
  docker-compose run --rm app python3 manage.py createsuperuser
}

if [ "$0" = "$BASH_SOURCE" ]; then
    COMMAND="${1}"
    shift
    set -eo pipefail
    case $COMMAND in "install")
            ${COMMAND} ${@}
        ;;
        "-h" | "--help" | *)
            help
        ;;
    esac
fi