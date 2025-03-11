#!/bin/bash
/home/livelink/mlat-client/venv/bin/mlat-client \
  --server 10.8.0.30:8123 \
  --no-udp \
  --lat 50.81939247623894 \
  --lon -1.1833555083141927 \
  --alt 10.8 \
  --input-type dump1090 \
  --input-connect 127.0.0.1:30005 \
  --results beast,connect,127.0.0.1:30104 \
  --results basestation,listen,31003 \
  --user `hostname` \
  --privacy

