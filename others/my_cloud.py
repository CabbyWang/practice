# -*- coding: utf-8 -*-
__author__ = 'cabbyw'
import requests
from pathlib import Path


pageToken = "Tm1Ia19JRmpObDFza1VzeElYR0dOWW95REFnM1cxMzdhR1ZlVWpEaw"

authorization1 = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlFUQkdPVFJCUWtJd01EQkNPRVE1UWpoQk5FSTBNRFl6T1RZMU5rUTJNRGs1TkVZNE5FSTVOUSJ9.eyJodHRwczovL3dkYy5jb20vYXV0aDAvY2xhaW1zIjp7ImF1dGhfaWQiOiJhZmNkMjlkMi05Nzk4LTRjNzgtODQ0OS03MWQwYzZhOTZkMzQifSwiaXNzIjoiaHR0cHM6Ly93ZGMuYXV0aDAuY29tLyIsInN1YiI6Ik5KVXg4T2VaMjJ3ZG1Yc2o5Ymo0dTYzSFJqYlJ0U29jQGNsaWVudHMiLCJhdWQiOiJteWNsb3VkLmNvbS9wdWJsaWNfc2hhcmUiLCJpYXQiOjE1NjEwNDY1MjYsImV4cCI6MTU2MTEzMjkyNiwiYXpwIjoiTkpVeDhPZVoyMndkbVhzajliajR1NjNIUmpiUnRTb2MiLCJzY29wZSI6ImF1dGhfZ2V0X3VzZXJpbmZvIG5hc19yZWFkX3dyaXRlIG5hc19yZWFkX29ubHkgcmVhZC13cml0ZSByZWFkLW9ubHkiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.iRZLPzglpYPYMVL1OvANYteP9Doq2FxYcojPmwngyR5xvbWOcWqkJcrJTK7j1M1QiE7LjV8ZoE-zUIiPGCE70lnKg5qWOLnKZHnnrvH6ycr6gxG6gNwYUlrZrZI3Jbb4TujGZAWx-rllMAJGzAm2OG9pz4Uyw0ZG-mNK9CfQwcTVz61YayZwyRkdN93RsPmXMv-a05guRipXPhWsupNcrQM8-6eTi-Li-ttNqMbKo6ztu_KbVhyDqkmVGSM9U768G-U3gsiRYPpqoTE5a35LhsVye3AMUWEV6TuRxunr6z-HZO8vmvtl25Zq7XycDO4UdgnZgRG4pfxaKa4U5OMOFQ"
authorization2 = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlFUQkdPVFJCUWtJd01EQkNPRVE1UWpoQk5FSTBNRFl6T1RZMU5rUTJNRGs1TkVZNE5FSTVOUSJ9.eyJodHRwczovL3dkYy5jb20vYXV0aDAvY2xhaW1zIjp7ImF1dGhfaWQiOiJhZmNkMjlkMi05Nzk4LTRjNzgtODQ0OS03MWQwYzZhOTZkMzQifSwiaXNzIjoiaHR0cHM6Ly93ZGMuYXV0aDAuY29tLyIsInN1YiI6Ik5KVXg4T2VaMjJ3ZG1Yc2o5Ymo0dTYzSFJqYlJ0U29jQGNsaWVudHMiLCJhdWQiOiJteWNsb3VkLmNvbS9wdWJsaWNfc2hhcmUiLCJpYXQiOjE1NjEwNDY1MjYsImV4cCI6MTU2MTEzMjkyNiwiYXpwIjoiTkpVeDhPZVoyMndkbVhzajliajR1NjNIUmpiUnRTb2MiLCJzY29wZSI6ImF1dGhfZ2V0X3VzZXJpbmZvIG5hc19yZWFkX3dyaXRlIG5hc19yZWFkX29ubHkgcmVhZC13cml0ZSByZWFkLW9ubHkiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.iRZLPzglpYPYMVL1OvANYteP9Doq2FxYcojPmwngyR5xvbWOcWqkJcrJTK7j1M1QiE7LjV8ZoE-zUIiPGCE70lnKg5qWOLnKZHnnrvH6ycr6gxG6gNwYUlrZrZI3Jbb4TujGZAWx-rllMAJGzAm2OG9pz4Uyw0ZG-mNK9CfQwcTVz61YayZwyRkdN93RsPmXMv-a05guRipXPhWsupNcrQM8-6eTi-Li-ttNqMbKo6ztu_KbVhyDqkmVGSM9U768G-U3gsiRYPpqoTE5a35LhsVye3AMUWEV6TuRxunr6z-HZO8vmvtl25Zq7XycDO4UdgnZgRG4pfxaKa4U5OMOFQ"

url1 = "https://prod-2775dfd1468e8c2.mycloud.com/6fb3b63d-1e3b-46b3-8b31-a6945adfc840/sdk/v2/filesSearch/parents?ids=HWkk6iL28xjHIeD0DFOMVbLv4QocGeobH_ShIBbz&fields=pageToken,id,cTime,mTime,mimeType,name,parentID,extension,size,publiclyShared,privatelyShared,video,image,family&limit=50&pretty=false&orderBy=name&order=asc"
url2 = "https://prod-2775dfd1468e8c2.mycloud.com/6fb3b63d-1e3b-46b3-8b31-a6945adfc840/sdk/v2/filesSearch/parents?ids=HWkk6iL28xjHIeD0DFOMVbLv4QocGeobH_ShIBbz&fields=pageToken,id,cTime,mTime,mimeType,name,parentID,extension,size,publiclyShared,privatelyShared,video,image,family&limit=50&pretty=false&orderBy=name&order=asc&pageToken=Tm1Ia19JRmpObDFza1VzeElYR0dOWW95REFnM1cxMzdhR1ZlVWpEaw"
url3 = "https://prod-2775dfd1468e8c2.mycloud.com/6fb3b63d-1e3b-46b3-8b31-a6945adfc840/sdk/v2/filesSearch/parents?ids=HWkk6iL28xjHIeD0DFOMVbLv4QocGeobH_ShIBbz&fields=pageToken,id,cTime,mTime,mimeType,name,parentID,extension,size,publiclyShared,privatelyShared,video,image,family&limit=50&pretty=false&orderBy=name&order=asc&pageToken=SG9sQ3J3UnFVUHhfWHF3dFNCb3pPOTNyNXk4ZHJyY2N3VGRPV1hIWA"

dl_url = "https://prod-2775dfd1468e8c2.mycloud.com/6fb3b63d-1e3b-46b3-8b31-a6945adfc840/sdk/v2/files/gDYxacRPKCgAvthJz2wf3rnytm2iqf_ywpd9sLiW/content?download=true&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlFUQkdPVFJCUWtJd01EQkNPRVE1UWpoQk5FSTBNRFl6T1RZMU5rUTJNRGs1TkVZNE5FSTVOUSJ9.eyJodHRwczovL3dkYy5jb20vYXV0aDAvY2xhaW1zIjp7ImF1dGhfaWQiOiJhZmNkMjlkMi05Nzk4LTRjNzgtODQ0OS03MWQwYzZhOTZkMzQifSwiaXNzIjoiaHR0cHM6Ly93ZGMuYXV0aDAuY29tLyIsInN1YiI6Ik5KVXg4T2VaMjJ3ZG1Yc2o5Ymo0dTYzSFJqYlJ0U29jQGNsaWVudHMiLCJhdWQiOiJteWNsb3VkLmNvbS9wdWJsaWNfc2hhcmUiLCJpYXQiOjE1NjEwNDY1MjYsImV4cCI6MTU2MTEzMjkyNiwiYXpwIjoiTkpVeDhPZVoyMndkbVhzajliajR1NjNIUmpiUnRTb2MiLCJzY29wZSI6ImF1dGhfZ2V0X3VzZXJpbmZvIG5hc19yZWFkX3dyaXRlIG5hc19yZWFkX29ubHkgcmVhZC13cml0ZSByZWFkLW9ubHkiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.iRZLPzglpYPYMVL1OvANYteP9Doq2FxYcojPmwngyR5xvbWOcWqkJcrJTK7j1M1QiE7LjV8ZoE-zUIiPGCE70lnKg5qWOLnKZHnnrvH6ycr6gxG6gNwYUlrZrZI3Jbb4TujGZAWx-rllMAJGzAm2OG9pz4Uyw0ZG-mNK9CfQwcTVz61YayZwyRkdN93RsPmXMv-a05guRipXPhWsupNcrQM8-6eTi-Li-ttNqMbKo6ztu_KbVhyDqkmVGSM9U768G-U3gsiRYPpqoTE5a35LhsVye3AMUWEV6TuRxunr6z-HZO8vmvtl25Zq7XycDO4UdgnZgRG4pfxaKa4U5OMOFQ"
dl_url = "https://prod-2775dfd1468e8c2.mycloud.com/6fb3b63d-1e3b-46b3-8b31-a6945adfc840/sdk/v2/files/RLBKdIcHXFPVcSn2Kjw0apJO9Q3yt1c66qTlFNJy/content?download=true&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlFUQkdPVFJCUWtJd01EQkNPRVE1UWpoQk5FSTBNRFl6T1RZMU5rUTJNRGs1TkVZNE5FSTVOUSJ9.eyJodHRwczovL3dkYy5jb20vYXV0aDAvY2xhaW1zIjp7ImF1dGhfaWQiOiJhZmNkMjlkMi05Nzk4LTRjNzgtODQ0OS03MWQwYzZhOTZkMzQifSwiaXNzIjoiaHR0cHM6Ly93ZGMuYXV0aDAuY29tLyIsInN1YiI6Ik5KVXg4T2VaMjJ3ZG1Yc2o5Ymo0dTYzSFJqYlJ0U29jQGNsaWVudHMiLCJhdWQiOiJteWNsb3VkLmNvbS9wdWJsaWNfc2hhcmUiLCJpYXQiOjE1NjEwNDY1MjYsImV4cCI6MTU2MTEzMjkyNiwiYXpwIjoiTkpVeDhPZVoyMndkbVhzajliajR1NjNIUmpiUnRTb2MiLCJzY29wZSI6ImF1dGhfZ2V0X3VzZXJpbmZvIG5hc19yZWFkX3dyaXRlIG5hc19yZWFkX29ubHkgcmVhZC13cml0ZSByZWFkLW9ubHkiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.iRZLPzglpYPYMVL1OvANYteP9Doq2FxYcojPmwngyR5xvbWOcWqkJcrJTK7j1M1QiE7LjV8ZoE-zUIiPGCE70lnKg5qWOLnKZHnnrvH6ycr6gxG6gNwYUlrZrZI3Jbb4TujGZAWx-rllMAJGzAm2OG9pz4Uyw0ZG-mNK9CfQwcTVz61YayZwyRkdN93RsPmXMv-a05guRipXPhWsupNcrQM8-6eTi-Li-ttNqMbKo6ztu_KbVhyDqkmVGSM9U768G-U3gsiRYPpqoTE5a35LhsVye3AMUWEV6TuRxunr6z-HZO8vmvtl25Zq7XycDO4UdgnZgRG4pfxaKa4U5OMOFQ"

file_url = "https://prod-2775dfd1468e8c2.mycloud.com/6fb3b63d-1e3b-46b3-8b31-a6945adfc840/sdk/v2/files/{id}/content?download=true&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlFUQkdPVFJCUWtJd01EQkNPRVE1UWpoQk5FSTBNRFl6T1RZMU5rUTJNRGs1TkVZNE5FSTVOUSJ9.eyJodHRwczovL3dkYy5jb20vYXV0aDAvY2xhaW1zIjp7ImF1dGhfaWQiOiJhZmNkMjlkMi05Nzk4LTRjNzgtODQ0OS03MWQwYzZhOTZkMzQifSwiaXNzIjoiaHR0cHM6Ly93ZGMuYXV0aDAuY29tLyIsInN1YiI6Ik5KVXg4T2VaMjJ3ZG1Yc2o5Ymo0dTYzSFJqYlJ0U29jQGNsaWVudHMiLCJhdWQiOiJteWNsb3VkLmNvbS9wdWJsaWNfc2hhcmUiLCJpYXQiOjE1NjEwNDY1MjYsImV4cCI6MTU2MTEzMjkyNiwiYXpwIjoiTkpVeDhPZVoyMndkbVhzajliajR1NjNIUmpiUnRTb2MiLCJzY29wZSI6ImF1dGhfZ2V0X3VzZXJpbmZvIG5hc19yZWFkX3dyaXRlIG5hc19yZWFkX29ubHkgcmVhZC13cml0ZSByZWFkLW9ubHkiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMifQ.iRZLPzglpYPYMVL1OvANYteP9Doq2FxYcojPmwngyR5xvbWOcWqkJcrJTK7j1M1QiE7LjV8ZoE-zUIiPGCE70lnKg5qWOLnKZHnnrvH6ycr6gxG6gNwYUlrZrZI3Jbb4TujGZAWx-rllMAJGzAm2OG9pz4Uyw0ZG-mNK9CfQwcTVz61YayZwyRkdN93RsPmXMv-a05guRipXPhWsupNcrQM8-6eTi-Li-ttNqMbKo6ztu_KbVhyDqkmVGSM9U768G-U3gsiRYPpqoTE5a35LhsVye3AMUWEV6TuRxunr6z-HZO8vmvtl25Zq7XycDO4UdgnZgRG4pfxaKa4U5OMOFQ"

image_dir = ""


if __name__ == "__main__":
    url = "https://prod-2775dfd1468e8c2.mycloud.com/6fb3b63d-1e3b-46b3-8b31-a6945adfc840/sdk/v2/filesSearch/parents?ids=HWkk6iL28xjHIeD0DFOMVbLv4QocGeobH_ShIBbz&fields=pageToken,id,cTime,mTime,mimeType,name,parentID,extension,size,publiclyShared,privatelyShared,video,image,family&limit=632&pretty=false&orderBy=name&order=asc"
    res = requests.get(url, headers={"Authorization": authorization1})
    result = res.json()
    files = result.get("files")
    ids = [i.get("id") for i in files[316:]]
    for i in files[316:]:
    # for i in files:
        id = i.get('id')
        name = i.get('name')
        f_url = file_url.format(id=id)
        a = requests.get(f_url)
        if a.status_code == 200:
            content = a.content
            # dir_name = Path(__file__).cwd().parent
            with open(str(image_dir / name), "wb") as f:
                f.write(content)
