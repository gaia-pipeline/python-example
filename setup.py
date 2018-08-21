from setuptools import setup

setup(name='testpipeline',
      description='simple gaia python pipeline example',
      packages=['pipeline'],
      author='pipelineauthor',
      author_email='pipelineauthor@mail.com',
      install_requires=[
            'gaiasdk>=0.0.12',
      ])