# 404 Link Tester

This is a small utility that will check a list of absolute links from a CSV file and save them to a new CSV file with their HTTP status code(s). This utility will not follow redirects by default, but you can do so by passing the `follow_redirects` argument to the script.

To get started, run: 

`python3 -m pip install -r requirements.txt`

Then paste your links into `links.csv` and run: 

`python3 check_links.py`

To follow redirects, use: 

`check_links.py follow_redirects`

## 404s
Will be saved to a CSV in `/results` called `404.csv`

## 200s
Will be saved to a CSV in `/results` called `200.csv`

## 3xx or Other Status Codes
Are not saved to a CSV file but will be printed to stdout when not using the `follow_redirects` argument.