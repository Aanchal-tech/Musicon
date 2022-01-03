import requests

class Music():

    def recommendations(self, label):
        self.auth_token = 'BQCiPWD9lQPZmo_rtCfz9j7oPiQffBBdZwlKLWUspNj8u3cb9pd10qbsXevFUw0Ytf_F_YW_jszFE08nt4JykySNS4XQvAv3KLZGnvh6baN-8QUsBsznIjQqoNXT5xlRW0ApKf0ez5JQZs13HwSYeNXRkQ28Bqp0WS8Mh3fXUnKlxVvDcJwOzJ1GIOf292u3zAaLllkaB3m-VVt_'
        hed = {'Authorization': 'Bearer ' + self.auth_token}
        data = {'app': 'MRBE'}

        url = 'https://api.spotify.com/v1/playlists/'
        if label == "Sad":
            id = "2XlzLiYK5TGoC4ihmJYQWV"
        elif label == "Happy":
            id = "0ySRSWggz1WzI9rPkQTQn9"
        elif label == "Angry":
            id = "4cllWzORlvlwrhZf17mpYN"
        elif label == "Neutral":
            id = "1HYAXEiPSAweKDbx8T2pGC"
        elif label == "Surprised":
            id = "6zxAPdCbKbMHxULOD25qFE"
        elif label == "Fear":
            id = "1cjat0l75mQgSdKzwtjKhW"
        else :
            id == "2dH0S4ytsw35IL5lJSVePU"
        response = requests.get(url + id, headers=hed)
        #print(response)
        resp = response.json()
        print(label, ":", resp['external_urls']['spotify'])

#temp = Music()
#temp.recommendations()
