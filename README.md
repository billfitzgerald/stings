# STINGS, or Search The Things

STINGS is a tool that allows streamlined searching for information (privacy policies, terms of service, cookie policies, governance documents, or really, anything!) across a large number of domains.

The tool has two scripts: one for a targeted search of a single domain, and one for a standardized search using identical criteria across multiple domains.

The tool can set up searches using DuckDuckGo or Google. 

## Search a single domain

To search a single domain, modify the **strings.csv** file to contain the search strings you want to use. If you want to limit the search to find exact matches, set the "precise" column to "yes".

When you run the script, you will be prompted to enter the domain you want to search.

Then, the script will open a new web browser, with each search in a new tab. **Note**: this functionality requires Firefox, Selenium, and the Selenium web driver for Firefox. If you are unsure about installing any of these elements, you can get comparable functionality with the tooling to search multiple domains.

## Search multiple domains

To search multiple domains, modify both the **domains.csv** and **strings.csv** files.

In **domains.csv** put the company name and the corresponding domain you want to search.

In **strings.csv** put the strings you want to use. In the "purpose" column, put a word or phrase describing what the search should uncover (ie, Privacy Policy, End User License Agreement, Cookie Policy, etc). If you want to limit the search to find exact matches, set the "precise" column to "yes".

Then, run the **docs_discovery_output.py** script, and it will generate an html page with links to each specific search, organized by company.