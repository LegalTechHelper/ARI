# ARI
ARI is a [docassemble](https://docassemble.org) package for automated readability indexing.

## License
- This package is licensed under the terms of [GPLv3](https://opensource.org/licenses/gpl-3.0.html).
- Docassemble itself is licensed under an [MIT license](https://opensource.org/licenses/MIT), see [github.com/jhpyle/docassemble/blob/master/LICENSE.txt](https://github.com/jhpyle/docassemble/blob/master/LICENSE.txt).

## Prerequisite
In order to use this package you have to have already installed a **docassemble server**.

## How to install
You can either:<br/>
install this package using either a standard way of installing packages in docseemble, see 
[https://docassemble.org/docs/packages.html#github_install](https://docassemble.org/docs/packages.html#github_install)<br/>
or use the bash script provided in this repository.

If you are using the bash script `build.sh` provided here, here is what you need to do:-<br/>

1. Get into the bash shell of your running docassemble docker container
```
docker exec -t -i <your container> /bin/bash
```
and then clone this repository
```
cd /tmp
git clone https://github.com/LegalTechHelper/ARI.git
```

2. Now build/ install the package:
```
cd /tmp/ARI
chmod 755 build.sh
sh build.sh
```

The service should then be available under the following URL<br/>
__https://&lt;your domain&gt;/interview?i=docassemble.ARI:data/questions/text.yml__


## Demo
You can find a demo of this package installed at
[https://dh-demo.legaltechhelper.com/interview?i=docassemble.ARI:data/questions/text.yml](https://dh-demo.legaltechhelper.com/interview?i=docassemble.ARI:data/questions/text.yml)

Start by trying out the phrase "The cat sat on a mat."
