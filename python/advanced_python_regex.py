```
import pandas as pd

faculty=pd.read_csv('faculty.csv', index_col=0)

def clean_type(name):
    new_string=''    
    for char in name:
        if not char.isdigit():
            new_string += char
    return new_string.replace('.','').strip().split()
# Q1 find degree titles
def degree_titles(faculty):
    titles=[]    
    for title in faculty[' degree']:        
        titles.append(clean_type(title))
    return titles

def unique_types(types):
    unique=[]
    for title in degree_titles(types):
        for one in title:
            if one not in unique:
                unique.append(one)
    return unique
    
unique_degrees=dict.fromkeys(unique_types(faculty),0)
total_degrees=degree_titles(faculty)

def count_occur(d,l):
    for key in d:
        for el in l:
            if key in el:
                d[key] +=1
    return d
# Q2 find each position title    
def position_titles(faculty):
    titles=[]
    for title in faculty[' title']:
        titles.append(title)
    return titles
    
def unique_positions(faculty):
    unique=[]
    for type in position_titles(faculty):
        if type not in unique:
            unique.append(type)
    return unique
    
positions=dict.fromkeys(unique_positions(faculty),0)
total_positions=position_titles(faculty)

def count_titles(d,l):
    for key in d:
        for el in l:
            if key== el:
                d[key]+=1
    return d
    
# Q3 email addresses
def emails(l):
    address_list=[]    
    for address in faculty[' email']:
        address_list.append(address)
    return address_list

# Q4 unique domains
def get_domains(*e):
    addresses=[]
    domains=[]    
    for email in emails(faculty):
        addresses.append(email.split('@'))
    for address in addresses:
        domains.append(address[1])
    return domains
        
total_domains=get_domains(faculty)

def unique_domains(domains):
    unique=[]
    for domain in domains:
        if domain not in unique:
            unique.append(domain)
    return unique

print "Q1, Degree Titles and Frequencies", count_occur(unique_degrees,total_degrees)

print "Q2, Position Titles and Frequencies", count_titles(positions, total_positions)

print "Q3, List of Emails", emails(faculty)

print "Q4, Unique Domains", unique_domains(total_domains)
```
