<h1 align="center">
  <img src="https://github.com/daemoncibsec/subenumerator/blob/main/subenumerator-logo.png" alt="subenumerator" width="1000px">
  <br>
</h1>

Subenumerator is a fast and easy-to-usetool that allows to automatize subdomains recon. It written in Python to allow the cybersecurity specialist having a quick lookup to accessible webpages, redirections and other types of codes in web pages. The tool shines specially in Bug Bounty, where many domains exists but only few are accessible.

## Installation

```bash
git clone https://github.com/daemoncibsec/subenumerator.git
pip install httpx
pip install argparse
cd subenumerator
```

Additionally, you can make it a binary in Linux systems using these "cython" library, so you don't have to move between folders, and have it implemented in your system as well as with other commands.

```bash
pip install cython
python3 -m cython subenumerator.py --embed
gcc -Os $(python3-config --includes) subenumerator.c -o subenumerator $(python3-config --ldflags --embed)
sudo cp subenumerator /usr/bin/
```
## Usage/Examples

- [Video example](https://www.instagram.com/reel/DH9HUYUOoHo/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==)

```bash
python3 subenumerator -h
```

In case you have the script compiled with cython and gcc:

```bash
subenumerator -h
```
## Authors

- [@daemoncibsec](https://www.github.com/daemoncibsec)

