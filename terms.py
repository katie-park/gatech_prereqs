from lxml import html
from courses import AtoZ
import requests

# Returns a dictionary with term names as keys and term numbers as values. (e.g. 'Spring 2021': '202102')
def get_terms():
    page = requests.get('https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_dyn_sched') # generate "Select Term of Date Range" page
    tree = html.fromstring(page.content)
    termlist = tree.xpath("//td[@class='dedefault']/select[@name='p_term']/option") # list of terms in dropdown
    return {term.text_content(): term.attrib['value'] for term in termlist}

print(get_terms())
