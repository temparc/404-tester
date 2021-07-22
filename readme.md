# 404 Link Tester

This is a small utility that will check a list of absolute links from a CSV file and save them to a new CSV file with their HTTP status code(s). This utility will not follow redirects by default, but you can do so by passing the `follow_redirects` argument to the script.

To get started, run: 

`python -m pip install -r requirements.txt`

Then paste your links as single column in `links.csv`, then run: 

`python check_links.py`

To follow redirects, use: 

`python check_links.py follow_redirects`

## Results
Links and their respective status codes will be saved to `results.csv`