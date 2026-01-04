#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pathlib import Path

# Read README.md for PyPI long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="rtmps",
    version="0.1.0",
    author="Ankit Chaubey",
    author_email="",
    description="Telegram RTMPS Voice Chat music streaming engine (educational, non-commercial)",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/ankit-chaubey/rtmps",

    packages=find_packages(),

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Multimedia :: Sound/Audio :: Players",
        "Topic :: Communications :: Chat",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],

    install_requires=[
        "telethon>=1.34.0",
    ],

    entry_points={
        "console_scripts": [
            "rtmps=rtmps.__main__:run",
            "rtmps-config=rtmps.cli:run",
        ],
    },

    python_requires=">=3.8",

    keywords=[
        "telegram",
        "voice-chat",
        "music-bot",
        "rtmps",
        "ffmpeg",
        "telethon",
        "streaming",
        "education",
        "non-commercial",
    ],

    project_urls={
        "Source": "https://github.com/ankit-chaubey/rtmps",
        "Bug Tracker": "https://github.com/ankit-chaubey/rtmps/issues",
        "Documentation": "https://github.com/ankit-chaubey/rtmps#readme",
    },
)
