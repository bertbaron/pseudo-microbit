from setuptools import setup

setup(
    name='pseudo-microbit',
    version='1.8',
    packages=['microbit'],
    py_modules=['microbit', 'compass', 'display',
                'i2c', 'spi', 'uart', 'music', 'neopixel',
                'os', 'speech', 'radio'],
    install_requires=['microfs',
                      'uflash',
                      'pyminifier'],
    url='https://github.com/MrYsLab/pseudo-microbit',
    download_url='https://github.com/MrYsLab/pseudo-microbit',
    license='MIT',
    author='Alan Yorinks',
    author_email='MisterYsLab@gmail.com',
    description='API to be used with PyCharm for micro:bit python development',
    keywords=['micro:bit', 'microbit', 'micropython'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
    ],
)
