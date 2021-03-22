# 404 Link Tester

This is a small utility that will check a list of absolute links from a CSV file and sort them into separate CSV files for 200 or 404 status codes. 

To get started, run: 

`python3 -m pip install -r requirements.txt`

Then paste your links into `links.csv` and run: 

`python3 check_links.py`

## 404s
Will be saved to a CSV in `/results called 404.csv`

## 200s
Will be saved to a CSV in `/results called 200.csv`

## 3xx or Other Status Codes
Are not saved to a CSV file but will be printed to stdout.