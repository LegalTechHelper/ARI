import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.ARI',
      version='2.0.0',
      description=('ARI - Automated Readabilty Index'),
      long_description='# ARI\r\nARI is a [docassemble](https://docassemble.org) package for automated readability indexing.\r\n\r\n## License\r\n- This package is licensed under the terms of [GPLv3](https://opensource.org/licenses/gpl-3.0.html).\r\n- Docassemble itself is licensed under an [MIT license](https://opensource.org/licenses/MIT), see [github.com/jhpyle/docassemble/blob/master/LICENSE.txt](https://github.com/jhpyle/docassemble/blob/master/LICENSE.txt).\r\n\r\n## Prerequisite\r\nIn order to use this package you have to have already installed a **docassemble server**.\r\n\r\n## How to install\r\nYou can **either** install this package using the standard way of installing packages in docassemble from the playground, see \r\n[https://docassemble.org/docs/packages.html#github_install](https://docassemble.org/docs/packages.html#github_install)<br/>\r\n**or** you can use the bash script provided in this repository.\r\n\r\nIf you are using the bash script `build.sh` provided here, here is what you need to do:-<br/>\r\n\r\n1. Get into the bash shell of your running docassemble docker container\r\n```console\r\ndocker exec -t -i <your container> /bin/bash\r\n```\r\nand then clone this repository\r\n```console\r\ncd /tmp\r\ngit clone https://github.com/LegalTechHelper/ARI.git\r\n```\r\n... or if you are pulling to get the latest changes for this repo then\r\n```console\r\ncd /tmp/ARI\r\ngit pull origin main --ff-only\r\n```\r\n\r\n2. Now build/ install the package:\r\n```console\r\ncd /tmp/ARI\r\nchmod 755 build.sh\r\nsh build.sh\r\n```\r\n\r\nThe service should then be available under the following URL<br/>\r\n__https://&lt;your domain&gt;/interview?i=docassemble.ARI:data/questions/text.yml__\r\n\r\n\r\n## Demo\r\nYou can find a demo of this package installed at<br/>\r\n[https://dh-demo.legaltechhelper.com/interview?i=docassemble.ARI:data/questions/text.yml](https://dh-demo.legaltechhelper.com/interview?i=docassemble.ARI:data/questions/text.yml)\r\n\r\nStart by trying out the phrase "The cat sat on a mat."',
      long_description_content_type='text/markdown',
      author='Legal Tech Helper',
      author_email='info@legaltechhe;per.com.au',
      license='GPLv3',
      url='https://github.com/LegalTechHelper/ARI',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/ARI/', package='docassemble.ARI'),
     )

