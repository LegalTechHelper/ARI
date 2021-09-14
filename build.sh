#!/usr/bin/env bash
mkdir -p  /tmp/docassemble-ARI
cp -r ./packages/docassemble-ARI /tmp/docassemble-ARI/
source /usr/share/docassemble/local3.8/bin/activate \
&& pip3 install --upgrade /tmp/docassemble-ARI
echo "Package docassemble-ARI installed and is available on"
echo "https://<your domain>/interview?i=docassemble.ARI:data/questions/text.yml"
