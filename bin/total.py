import sys,os
import splunk.Intersplunk
import json
import requests as req


def tmdb(requestURL,parameters):	
    response=req.get(url=requestURL,params=parameters)
    if response.status_code !=200:
       print('Status: ',response.status_code,'Headers: ',response.headers,'Error Response: ',response.json())
       exit()
    data=response.json()
    return json.dumps(data)
    
def get():
    gen = []
    api_key = "0aaa66bec07a68356438a8cc425388b9"
    requestURL = "https://api.themoviedb.org/3/movie/now_playing"
    parameter = {"api_key" : api_key}
    getting = tmdb(requestURL,parameter)
    data = json.loads(getting)
    for i in data:
        gen.append(i)
    return gen

geners = get()
#print(geners)
splunk.Intersplunk.outputResults(geners)            
            