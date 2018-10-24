# LIST S3 Buckets

This is simple Python script to list AWS S3 buckets in given region or all regions

# Requirements

[Python 2.x or 3.x](https://www.python.org/downloads/)

Python libs: argparse, boto3, sys

# Installation
```bash
$ pip install boto3
$ pip install argparse
```

# Usage example

Below are examples for Linux operating system

```bash
# List all regions
$ .\s3.py all

# List buckets in given region, e.g.
$ .\s3.py eu-west-1

# List help
$ .\s3.py -h
```

# Changelog

- v.1.0 - 24.10.2018 - Public release
