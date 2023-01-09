from secret import key
import requests
import json
def get_images(search='river'):
    url_base = "https://api.pexels.com/v1/search"
    headers = {
        'Authorization': key,
    }

    params = {
        'query': search,
    }

    response = requests.get(url_base, params=params, headers=headers)
    

    json_response = response.json()
    list_photos = json_response["photos"]

    return [photo["src"]["portrait"] for photo in list_photos]
    
    
def get_one_image(url_img, path_folder):

    # for save images
    new_path_image = path_folder + "/temp.jpeg"
    
    with open(new_path_image, "wb") as image:
            
        img_response = requests.get(url_img)
        image.write(img_response.content)
        
        # path of file
        return  new_path_image





    # print("ready")

    #print(json.dumps(response.json(), indent=4))

    
# def main():
#     get_images()
# if __name__=="__main__":
#     main()