"""Setup for IAA XBlock."""


import os

from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='iaaxblock',
    version='0.1',
    description='Documento iterativo',
    license='GPL 3.0',
    packages=[
        'iaaxblock',
    ],
    install_requires=[
        'XBlock',
        'web-fragments',
    ],
    entry_points={
        'xblock.v1': [
            'iaaxblock = iaaxblock:IterativeAssessedActivityXBlock',
        ],
        "lms.djangoapp": [
            "iaaxblock = iaaxblock.apps:IAAAppConfig",
        ],
        "cms.djangoapp": [
            "iaaxblock = iaaxblock.apps:IAAAppConfig",
        ]
    },
    package_data=package_data("iaaxblock", ["static", "public"]),
)
