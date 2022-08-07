# Hubify
A python script to convert your Markdown files into HTML which look just like GitHub's readme

## Installation

First, clone the repository:

```bash
git clone git@github.com:memory-hunter/hubify.git
```

And then run the following command to install the dependencies.
```bash
pip install -r requirements.txt
```

## Usage
```
usage: hubify.py [-h] [-m {light,dark,l,d}] file

Convert Markdown to HTML in GitHub Readme style

positional arguments:
  file                  Markdown file to convert

options:
  -h, --help            show this help message and exit
  -m {light,dark,l,d}, --mode {light,dark,l,d}
                        Color mode
```
## License
[MIT](https://choosealicense.com/licenses/mit/)
