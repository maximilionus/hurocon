import setuptools

from huawei_lte_cli.meta import version


package_name = 'huawei_lte_cli'
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
            'huawl = huawei_lte_cli.cli:cli'
        ]
    },
    license='Apache-2.0',
    url='https://github.com/maximilionus/huawei_lte_cli',
    project_urls={  # TODO
        'Documentation': '',
        'Tracker': 'https://github.com/maximilionus/serialix/huawei_lte_cli'
    },
    classifiers=[  # TODO
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ]
)
