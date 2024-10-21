# Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript
import re
import csv

with open('./data/hacker_news.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    python_count = 0
    javascript_count = 0
    java_count = 0

    for row in csv_reader:
        for sentence in row:
            matches_python = re.findall(r'[Pp]ython', sentence)
            matches_javascript = re.findall(r'JavaScript|javascript|Javascript', sentence)
            matches_java = re.findall(r'\bJava\b', sentence)
            if matches_python:
                python_count += 1
            if matches_javascript:
                javascript_count += 1
            if matches_java:
                java_count += 1
        
    print(f'Lines containing python or Python: {python_count}') # 266
    print(f'Lines containing JavaScript, javascript or Javascript: {javascript_count}') # 241
    print(f'Lines containing Java: {java_count}') # 52