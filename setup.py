from setuptools import setup

setup(name='django-xsession',
      version='0.1',
      description='Django middleware that allows cookie sharing across multiple domains.',
      author='Factor AG',
      author_email='webmaster@factor.ch',
      url='https://github.com/FactorAG/django-xsession',
      license='LGPLv3',
      keywords='django single sign on cookie sharing',
      packages=['django-xsession'],
      platforms=['any'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
    )