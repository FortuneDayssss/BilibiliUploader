from setuptools import setup
import bilibiliuploader

with open('requirements.txt') as f:
    requires = f.readlines()

setup(
    name='bilibiliuploader',
    version=bilibiliuploader.__version__,
    packages=['bilibiliuploader'],
    url='https://github.com/FortuneDayssss/BilibiliUploader',
    install_requires=requires,
    license='MIT',
    author='FortuneDayssss',
    author_email='717622995@qq.com',
    description='Simulate pc ugc_assistant for bilibili',
    keywords=['bilibili', 'upload'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
