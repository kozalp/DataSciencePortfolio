#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 09:17:23 2021

@author: mk

Tutorial link: https://www.youtube.com/watch?v=XVv6mJpFOb0
"""
from bs4 import BeautifulSoup

# 1. READ A .html FILE FROM A DIRECTORY. Some notes...
# 'r': means read-only
with open('/Users/mk/Documents/web_scraping/home.html','r') as html_file:
    content = html_file.read()

# To make the output more readable. This essentially
# justifies lines and puts website content on separate lines.
# It might do more but the file we have has a pretty simple elements.    
    soup = BeautifulSoup(content, "lxml")
#     # tags = soup.find('h5')

# # 2. FIND SPECIFIC INFORMATION IN A WEBSITE
# # The "find" method only finds the first element. To change that,
# # use find_all

#     courses_html_tags = soup.find_all("h5")

# # Now, this returns a list. We can separate the values
# # using a loop.

#     for course in courses_html_tags:
#         print(course.text)

# 3. PULL COURSE NAME AND PRICE INFORMATION
# A few pretty important notes for this section.
# THe information we want is in a specific type of "div"
# whose class is "cards". It is great that we can give this
# information to Python for search.
# One important thing, though, is that "class" is a native
# function of Python. Therefore, we use "class_" (with underscore(_))
# to define the class of the div container.
    course_cards = soup.find_all("div", class_= "card")
    
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        
        print(f'{course_name} costs {course_price}')

        
        
        
        
        