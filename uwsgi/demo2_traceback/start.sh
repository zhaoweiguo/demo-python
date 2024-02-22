#!/bin/bash

uwsgi --http :8080 -w slow --master --processes 2 --threads 4 --py-tracebacker /tmp/tbsocket.



