import csv
import os
import django
import sys

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# 현재 디렉토리 경로 표시
os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

# 프로젝트명.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings_r")
django.setup()

from pybo.models import *

def book():
    # csv 파일 경로
    CSV_PATH = './data/book.csv'	
    
    # encoding 설정 필요
    with open(CSV_PATH, newline='', encoding='utf-8-sig') as csvfile:	
        data_reader = csv.DictReader(csvfile)
    
        for row in data_reader:
            # print(row)
            Book.objects.create(	
                category = row['category'],
                major=row['major'],
                title=row['title'],
                author=row['author'],
                publisher=row['publisher'],
                content=row['contents'],
                keywords=row['keywords']
             )
            print(row)

def paper():
    # csv 파일 경로
    CSV_PATH = './data/paper.csv'	
    
    # encoding 설정 필요
    with open(CSV_PATH, newline='', encoding='utf-8-sig') as csvfile:	
        data_reader = csv.DictReader(csvfile)
    
        for row in data_reader:
            # print(row)
            Book.objects.create(	
                category = row['category'],
                major=row['major'],
                title=row['title'],
                author=row['author'],
                abstract=row['abstract'],
                keywords=row['keywords']
             )
            print(row)
            
def ted():
    # csv 파일 경로
    CSV_PATH = './data/ted.csv'	
    
    # encoding 설정 필요
    with open(CSV_PATH, newline='', encoding='utf-8-sig') as csvfile:	
        data_reader = csv.DictReader(csvfile)
    
        for row in data_reader:
            # print(row)
            Book.objects.create(	
                category = row['category'],
                major=row['major'],
                title=row['title'],
                link=row['link'],
                subjects=row['subjects'],
                content=row['contents'],
                keywords=row['keywords']
             )
            print(row)
            
def article():
    # csv 파일 경로
    CSV_PATH = './data/article.csv'	
    
    # encoding 설정 필요
    with open(CSV_PATH, newline='', encoding='utf-8-sig') as csvfile:	
        data_reader = csv.DictReader(csvfile)
    
        for row in data_reader:
            # print(row)
            Book.objects.create(	
                category = row['category'],
                major=row['major'],
                title=row['title'],
                link=row['link'],
                subjects=row['subjects'],
                content=row['contents'],
                keywords=row['keywords']
             )
            print(row)
            
if __name__== '__main__':
    if sys.argv[1]=='book':
        book()
    elif sys.argv[1]=='paper':
        paper()
    elif sys.argv[1]=='ted':
        ted()
    elif sys.argv[1]=='article':
        article()
    elif sys.argv[1]=='all':
        book()
        paper()
        ted()
        article()
    else:
        print("invalid input!!")