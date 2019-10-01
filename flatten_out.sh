#!/bin/bash

for fname in `find out -type f | grep .txt`; do mv "$fname" out; done
for fname in `find out -type d`; do rm -d "$fname"; done
