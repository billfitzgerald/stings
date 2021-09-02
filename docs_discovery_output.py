import pandas as pd
import re
import os
import datetime
import tldextract
import csv
import markdown

## source data
source_file = 'strings.csv' # file should be a csv with three columns named `purpose`, `source_strings`, and `precise`
source_domains = 'domains.csv' # file should be a csv with two columns named `organization` and `domain`

## output files
markdown = 'search.md'
html = 'search.html'

## Select Google or DuckDuckGo
#search_base = 'https://duckduckgo.com/?q='
search_base = 'https://www.google.com/search?q='

##########################################
## Do Not Adjust Values Below This Line ##
##########################################

count = 0

d = datetime.datetime.today()
year = d.strftime("%Y")
month = d.strftime("%m")
day = d.strftime("%d")

# create directory for output
reports_dir = "results/" + year + "_" + month + "_" + day + "/"
try:
	os.makedirs(reports_dir)
except FileExistsError:
	# directory already exists
	pass

md_output = reports_dir + markdown
html_output = reports_dir + html

def create_text(filename,text):
	with open (filename, 'a') as file:
		file.write(text)

# read in csv files as dataframe
df_domains = pd.read_csv(source_domains)
thank_you = pd.read_csv(source_file) 

intro_txt = "# Search terms, organized by company\n"
it_html = "<h1>Search terms, organized by company</h1>\n"
create_text(md_output,intro_txt)
# build search urls
for c,d in df_domains.iterrows():
	base_domain = d['domain']
	org = d['organization']
	org_txt = f"\n## {org}\n\n"
	ot_html = f"\n<h2>{org}</h2>\n\n"
	for a,b in thank_you.iterrows():
		string = b['source_strings']
		purpose = b['purpose']
		if b['precise'] == 'yes':
			search_url = f'<li>Find <a href="{search_base}&quot;{string}&quot; site:{base_domain}" alt="{purpose}" target="_blank" rel=noopener>{purpose}</a></li>'
		else:
			search_url = f'<li>Find <a href="{search_base}{string} site:{base_domain}" alt="{purpose}" target="_blank" rel=noopener>{purpose}</a></li>'
		count += 1
		org_txt = org_txt + f"{search_url}\n"
		ot_html = ot_html + f"{search_url}\n"
	org_txt = org_txt + "\n"
	ot_html = ot_html + "\n"
	create_text(md_output,org_txt)
	create_text(html_output, ot_html)
	
print("All Done! Processed {0} search strings.".format(count))
