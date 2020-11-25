from lxml import html
import requests

# Returns a dictionary with term names as keys and term numbers as values. (e.g. 'Spring 2021': '202102')
def get_terms():
    page = requests.get('https://oscar.gatech.edu/pls/bprod/bwckschd.p_disp_dyn_sched') # generate "Select Term of Date Range" page
    tree = html.fromstring(page.content)
    termlist = tree.xpath("//td[@class='dedefault']/select[@name='p_term']/option") # list of terms in dropdown
    return {term.text_content(): term.attrib['value'] for term in termlist} # https://lxml.de/3.2/lxmlhtml.html

# generated from get_terms() on Nov 25, 2020
terms = {'None': '', 'Language Inst IEP: Fall 1 21 (View only)': '202127', 'Spring 2021': '202102', 'Language Inst IEP: Fall 2 20 (View only)': '202028', 'Language Institute 2020 (View only)': '202023', 'Fall 2020': '202008', 'Summer 2020': '202005', 'Spring 2020': '202002', 'Fall 2019': '201908', 'Summer 2019 (View only)': '201905', 'Spring 2019 (View only)': '201902', 'Fall 2018 (View only)': '201808', 'Summer 2018 (View only)': '201805', 'Spring 2018 (View only)': '201802', 'Fall 2017 (View only)': '201708', 'Summer 2017 (View only)': '201705', 'Spring 2017 (View only)': '201702', 'Fall 2016 (View only)': '201608', 'Summer 2016 (View only)': '201605', 'Spring 2016 (View only)': '201602', 'Fall 2015 (View only)': '201508', 'Summer 2015 (View only)': '201505', 'Spring 2015 (View only)': '201502', 'Fall 2014 (View only)': '201408', 'Summer 2014 (View only)': '201405', 'Spring 2014 (View only)': '201402', 'Fall 2013 (View only)': '201308', 'Summer 2013 (View only)': '201305', 'Spring 2013 (View only)': '201302', 'Fall 2012 (View only)': '201208', 'Summer 2012 (View only)': '201205', 'Spring 2012 (View only)': '201202', 'Fall 2011 (View only)': '201108', 'Summer 2011 (View only)': '201105', 'Spring 2011 (View only)': '201102', 'Fall 2010 (View only)': '201008', 'Summer 2010 (View only)': '201005', 'Spring 2010 (View only)': '201002', 'Fall 2009 (View only)': '200908', 'Summer 2009 (View only)': '200905', 'Spring 2009 (View only)': '200902', 'Fall 2008 (View only)': '200808', 'Summer 2008 (View only)': '200805', 'Spring 2008 (View only)': '200802', 'Fall 2007 (View only)': '200708', 'Summer 2007 (View only)': '200705', 'Spring 2007 (View only)': '200702', 'Fall 2006 (View only)': '200608', 'Summer 2006 (View only)': '200605', 'Spring 2006 (View only)': '200602'}

