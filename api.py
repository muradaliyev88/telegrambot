import requests as reqs

class Connection:
    
    def __init__(self,url,data) -> None:
        self.url = url
        self.data = data
    
    async def response_post(self):
        response = await reqs.post(self.url,self.data)
        if response.status_code == reqs.codes.ok:
            print('Request was successful')
            print(response.json())
        else:
            print('Request failed with status code:', response.status_code)

