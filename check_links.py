import requests
import csv
from colors import status_colors
import time

file_links = 'links.csv'
file_notfound = 'results/404.csv'
file_ok = 'results/200.csv';

def get_http_status(url):
	r = requests.get(url, headers={"content-type":"text/html", "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"})
	return r.status_code

with open(file_notfound, 'w', newline='') as notfound_file:
	notfound_writer = csv.writer(notfound_file, delimiter=',')

	with open(file_ok, 'w', newline='') as ok_file:
		ok_writer = csv.writer(ok_file, delimiter=',')

		with open(file_links, newline='') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				status_code = get_http_status(row[0])
				print(row[0])
				if status_code == 200:
					print(f"{status_colors.OK}{status_code}{status_colors.ENDC}")
					ok_writer.writerow([row[0]])
				elif status_code == 404:
					print(f"{status_colors.FAIL}{status_code}{status_colors.ENDC}")
					notfound_writer.writerow([row[0]])
				else:
					print(f"{status_colors.WARN}{status_code}{status_colors.ENDC}")
				# sleep so we don't overwhelm the server or get blocked
				time.sleep(1)




