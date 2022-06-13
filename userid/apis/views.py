from userid.google_tools import scrapper
from django.shortcuts import render
import datetime

def home_content_api(request):
    now = datetime.datetime.now()
    
    query= ["twitter","mcu", "india","disney"]
    titles=[]
    links=[]
    times=[]
    descs=[]
    images=[]
    for q in query:
        temp = scrapper.home_content.news_api(q)
        if not temp["title"] == "":
            titles.append(temp["title"])
            links.append(temp["link"])
            times.append(temp["time"])
            descs.append(temp["desc"])
            images.append(temp["image"])
            
    
    content={
        "titles":titles,
        "links":links,
        "times":times,
        "descs":descs,
        "images":images
        
    }     

    content.update({"query":query})  
    content.update({"titles_links_times_descs_images_query": zip(titles,links,times,descs,images,query)})
    diff = datetime.datetime.now() - now
    print(diff.total_seconds())
    return render(request, "home-content.html", content)