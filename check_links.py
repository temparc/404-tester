import requests
import csv
from colors import status_colors
import time
import sys


file_links = 'links.csv'
file_results = 'results/results.csv'
follow_redirects = False if len(sys.argv) <= 1 else sys.argv[1]


# Get the HTTP status of a URL
# @return int status_code
def get_http_status(url):

	if not url:
		return

	allow_redirects = False

	if follow_redirects == 'follow_redirects':
		allow_redirects = True

	try:
		r = requests.get(url, headers={"content-type":"text/html", "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}, allow_redirects=allow_redirects)
	except Exception as e:
		print(f"{status_colors.WARN}{e}{status_colors.ENDC}")
		return 'Error'
	return r.status_code


# Read/Write to CSVs
with open(file_results, 'w', newline='') as results:

	results_writer = csv.writer(results, delimiter=',')

	with open(file_links, newline='') as csvfile:

		print(f"{status_colors.OK}Reading CSV file...{status_colors.ENDC}")

		reader = csv.reader(csvfile)

		for row in reader:

			# check if row has value
			if row:
				status_code = get_http_status(row[0])
				print(row[0])

				if status_code == 200:
					print(f"{status_colors.OK}{status_code}{status_colors.ENDC}")
				elif status_code == 404:
					print(f"{status_colors.FAIL}{status_code}{status_colors.ENDC}")
				else:
					print(f"{status_colors.WARN}{status_code}{status_colors.ENDC}")

				# write url and status code to csv
				results_writer.writerow([row[0], status_code])

				# sleep so we don't overwhelm the server or get blocked
				time.sleep(1)
			else:
				print(f"{status_colors.WARN}Empty row{status_colors.ENDC}")

		print(f"{status_colors.OK}CSV read complete! Results written to results.csv{status_colors.ENDC}")
