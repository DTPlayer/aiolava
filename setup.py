from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='aiolavapy',
  version='0.1.0',
  author='reff06',
  author_email='info@dnsprovider.tech',
  description='Async library for Lava API',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/DTPlayer/aiolava',
  packages=find_packages(),
  install_requires=['aiohttp>=3.9.1', "pydantic>=2.0.2"],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='lava aiolava lavaapi',
  project_urls={
    'Official documentation': 'https://dev.lava.ru/',
  },
  python_requires='>=3.10'
)