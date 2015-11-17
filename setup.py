# -*- coding: utf-8 -*
from setuptools.command.install import install
from setuptools import find_packages
from setuptools import setup
from sys import version_info, stderr, exit
import codecs
import sys
import os


if sys.platform == "win32" or sys.platform == "cygwin":
    stderr.write("Hitch will not work on Windows. Sorry.\n")
    exit(1)


if version_info[0] == 2:
    if version_info[1] < 6:
        stderr.write("The hitch bootstrapper will not run on versions of python below v2.6.\n")
        exit(1)


if version_info[0] == 3:
    if version_info[1] < 3:
        stderr.write("The hitch bootstrapper will not run on python 3.0.x, 3.1.x or 3.2.x.\n")
        exit(1)


def read(*parts):
    # intentionally *not* adding an encoding option to open
    # see here: https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts), 'r').read()

setup(name="hitch",
      version="0.5.7",
      description="Bootstrapper for hitchtest - the loosely coupled integration testing framework",
      long_description=read('README.rst'),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Topic :: Software Development :: Libraries',
          'Operating System :: Unix',
          'Environment :: Console',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
      ],
      keywords='hitch testing framework bdd tdd declarative tests bootstrap virtualenv',
      author='Colm O\'Connor',
      author_email='colm.oconnor.github@gmail.com',
      url='https://hitchtest.readthedocs.org/',
      license='AGPL',
      install_requires=[],
      packages=find_packages(exclude=["docs", ]),
      package_data={},
      entry_points=dict(console_scripts=['hitch=hitch:commandline.run',]),
      zip_safe=False,
      include_package_data=True,
)
