#!/usr/bin/env python
import requests



# ------------- token gen --------------------------------------------------
#Authentication endpoint
auth_url = "https://partner.api.dailymotion.com/oauth/v1/token"


def get_access_token(client_id, client_secret):
    '''
    Authenticate on the API in order to get an access token
    '''

    response = requests.post(auth_url,
                             data={
                                 'client_id': client_id,
                                 'client_secret': client_secret,
                                 'grant_type': 'client_credentials',
                                 'scope': 'upload_videos read_videos edit_videos delete_videos'
                             },
                             headers={
                                 'Content-Type': 'application/x-www-form-urlencoded'
                             })

    if response.status_code != 200 or not 'access_token' in response.json():
        raise Exception('Invalid authentication response')

    return response.json()['access_token']


#Fill the client_id and client_secret generated in the step 1 and accessible directly from your Partner HQ.
access_token = get_access_token('<Your-client-id>',
                                '<Your-client-secret>')


#Creating a generic header with your access token
authorization_header = { 'Authorization' : 'Bearer ' +  access_token }
# -------------------------- END token gen ----------------------


#Base video endpoint. The full url will looks like https://partner.api.dailymotion.com/rest/video/<your-video-id>
video_url = "https://partner.api.dailymotion.com/rest/video"

#Editing the title of an existing video. You can find the full list of fields you can manipulate here: https://developers.dailymotion.com/api/#video-fields
def edit_video_title(video_id, title):
    '''
    Now that your video has been uploaded, you can publish it to make it visible
    '''
    editing_video_url = video_url + '/' + video_id

    response = requests.post(editing_video_url, data={
        "title": title
    },
        headers= authorization_header
    )

    if response.status_code != 200 or not 'id' in response.json():
        raise Exception('Invalid publish video response')

    return response.json()


#Calling the edit_video_title to modify the title of one of my existing videos
edit_video_title(<your-video-xid>, <your-new-title>)
