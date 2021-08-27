# SScanner

## About

This is a basic folder/repo scanner for secrets and file permissions. Written in python3.

### Things it can do

1. Scan for files with permissions (777)
2. Scan for secrets/PII in files (passwords, address, phone number, AWS keys, AWS buckets, server IP)
3. Directory or Github repo (or both) can be passed as CLI arguments.
4. Can be installed as CLI
5. Can check for file permissions other than 777.

### How to install as a CLI

```bash
git clone https://github.com/Siddharth-Rajput/sscanner.git
cd sscaner
pip3 install .
```
