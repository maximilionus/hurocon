import setuptools

from hurocon.meta import version


package_name = 'hurocon'
package_version = version


with open('README.md', 'r') as f:
    readme_text = f.read()

setuptools.setup(
    name=package_name,
    version=package_version,
    python_requires='~=3.7',
    author='maximilionus',
    author_email='maximilionuss@gmail.com',
    description='',  # TODO
    long_description_content_type='text/markdown',
    long_description=readme_text,
    keywords='',  # TODO
    packages=setuptools.find_packages(),
    install_requires=[  # TODO
        'huawei-lte-api',
        'serialix',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'hurocon = hurocon.cli:cli'
        ]
    },
    license='Apache-2.0',
    url='https://github.com/maximilionus/hurocon',
    project_urls={  # TODO
        'Documentation': 'https://github.com/maximilionus/hurocon/blob/master/README.md',
        'Tracker': 'https://github.com/maximilionus/serialix/hurocon'
    },
    classifiers=[  # TODO
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
    ]
)
