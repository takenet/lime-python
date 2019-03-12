from distutils.core import setup


setup(
    name='lime_models',
    packages=['lime_models'],
    version='0.2',
    license='apache-2.0',
    description='This module implements the basic models of the LIME protocol',
    author='Gabriel Rodrigues dos Santos',
    author_email='gabrielrsantoss@icloud.com',
    url='https://github.com/chr0m1ng/lime_models',
    download_url='https://github.com/chr0m1ng/lime_models/archive/v_02.tar.gz',
    keywords=['lime', 'blip', 'chatbot'],
    install_requires=[
        'jsonpickle',
        'deprecated',
    ],
    classifiers=[
        # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
