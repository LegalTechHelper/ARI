#!/bin/bash
source "/usr/share/docassemble/local3.8/bin/activate" && pip3 install --upgrade /tmp/ARI
echo "Package docassemble-ARI installed and is available on"
echo "https://<your domain>/interview?i=docassemble.ARI:data/questions/text.yml"
