try:
    # we don't want to depend on setuptools
    # please don't use any setuptools specific API
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import ropemode


classifiers=[
    'Development Status :: 4 - Beta',
    'Operating System :: OS Independent',
    'Environment :: X11 Applications',
    'Environment :: Win32 (MS Windows)',
    'Environment :: MacOS X',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Topic :: Software Development']

setup(name='ropemode',
      version=ropemode.VERSION,
      description=ropemode.INFO,
      author='Ali Gholami Rudi',
      author_email='aligrudi@users.sourceforge.net',
      url='http://rope.sf.net/',
      packages=['ropemode'],
      license='GNU GPL',
      classifiers=classifiers,
      requires=['rope (>= 0.9.2)'],
)

