import csv;


from AmazonSearch.models import KeyWord, Search, Title





sea = open('../search.csv', encoding='utf-8')
searchReader = csv.reader(sea, delimiter=',')
for row in searchReader:
    s = Search(keyword_text=row[0], date=row[1], page=row[2], position=row[3], title_text=row[4], author=row[5], publisher=row[6], pages=row[7], publication_date=row[8], sales_rank=row[9], image_link=row[10], asin=row[11])
    print(row[0])
    s.save()   

    

tt = open('../title.csv')
titleReader = csv.reader(tt, delimiter=',')
for row in titleReader:
    t = Title(asin=row[0], title_text=row[1], publisher=row[2], marketingservices=row[3], batch=row[4])
    print(row[0])
    t.save()






            


key = open('../keyword.csv')
keyReader = csv.reader(key, delimiter=',')



for row in keyReader:
     k = KeyWord(keyword_text=row[0])
     k.save()

