import private
from googleapiclient.discovery import build
link_prescript="https://www.youtube.com/watch?v="
image_prescript="http://img.youtube.com/vi/"
image_postscript="/0.jpg"
api_service='youtube'
version='v3'
count=50
min_view=0   
best =5      
no_pages=2   


def find_vids(keyword):
   urls=[]
   image_urls=[]
   responses=[]
   video_info=[]
   video_with_bestvalues=[]
   youtube = build(api_service,version,developerKey=private.key)    ## Replace The private.key with your google API key ##
   request=youtube.search().list(q=keyword,
                              part='id',
                              maxResults=count,
                              type='video',
                              relevanceLanguage="en"
                              )
   r =request.execute()
   responses.append(r)
   
   for j in range(no_pages):
      request=youtube.search().list(q=keyword,
                              part='id',
                              maxResults=count,
                              type='video',
                              relevanceLanguage="en",
                              pageToken=r['nextPageToken']
                              )
      r=request.execute()
      responses.append(r)

   
   def count_like_finder(id):
       response2=youtube.videos().list(part='statistics',id=id).execute()
       prefix=response2['items'][0]['statistics']
       try:
        video_info.append([prefix['viewCount'],prefix['likeCount'],id])
       except KeyError:
          pass
          
   

   for response in responses:
    for i in response['items']:
       count_like_finder(i['id']['videoId'])
   for i in video_info:
      if(int(i[0])>min_view and not int(i[1]) ==0):
        rating=float(i[0])/int(i[1])
      else:
         rating=0
      video_with_bestvalues.append([rating,i[2]])
   video_with_bestvalues.sort(reverse=True)
   print(len(video_with_bestvalues))
   for i in range(best):
      vid_id=video_with_bestvalues[i][1]
      url=link_prescript+vid_id
      img_url=image_prescript+vid_id+image_postscript
      urls.append(url)
      image_urls.append(img_url)
   return urls,image_urls

























