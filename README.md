# Shorted links

This script allows you to shorten links using the service [bit.ly](https://bitly.com/) and view the number of clicks on them.

To work with the script, you need to enter a link.
If it's a shorted link, application will return the number of clicks on it.
If  it's a normal link, application will create a shortened link.

If the link is incorrect, application will notify you.

### How to install

Python3 should already be installed. 
```
git clone https://github.com/user-name-art/week1_shorted_links.git
```
Create virtual environment, if you need. For example:
```
python3 -m venv .venv
```
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
### Settings

You need to create .env file with BITLY_TOKEN (type GENERIC ACCESS TOKEN) for [bit.ly](https://bitly.com/). See .env.template file for example.

### How to run

```
python script.py <link>
```
### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
