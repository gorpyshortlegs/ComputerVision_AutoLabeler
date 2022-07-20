import torch
import os
import ssl

import cv2
import torchvision
import json  # json for pretty output
from serpapi import GoogleSearch
import requests
#if running locally
#ssl._create_default_https_context = ssl._create_unverified_context

#replace best.pt with your trained model
model = torch.hub.load("ultralytics/yolov5", "custom",
                       path='best.pt', force_reload=True)

#pass in image and stores cordinates of bounding box to a .txt file
def get_cordinates(img_path,label_path,clas):
    # model is run on passed image
    results = model(img_path, size=416)


    im = cv2.imread(img_path)



    fil=open(label_path, "w")

    result_list=results.xyxy[0].tolist()
    for result in result_list:
        final_str=str(clas)


        x=result
        x.pop()
        x.pop()

        x=torch.tensor(x)
        #converts pytorch cordinates to yolov5 annotation cordinates
        cord=torchvision.ops.box_convert(x,'xyxy','cxcywh')
        cord=cord.tolist()
        cord[0]/=im.shape[1]
        cord[1]/=im.shape[0]
        cord[2]/=im.shape[1]
        cord[3]/=im.shape[0]
        for cords in cord:
            final_str+=" "+str(cords)
        print("BoundingBox: "+final_str)
        #writes annotation to file
        fil.write(final_str)
    fil.close()








def get_google_images(label,clas,num,folder,api):
    params = {
        # "api_key": os.environ.get("SERPAPI_KEY"),
        "api_key": api,
        "engine": "google",
        "q": label,
        "tbm": "isch",
        "ijn": num
    }

    search = GoogleSearch(params)
    results = search.get_dict()


    # save files to passed folder if it doesn't exist create the folder
    if not os.path.exists(folder):
        os.makedirs(folder)
    if not os.path.isfile(folder+"/data.yaml"):
        data_file=open(folder+"/data.yaml","w")
        data_file.write("train: ../train/images\nnc: 0 \nnames: []")
    if not os.path.exists(folder+"/train"):
        os.makedirs(folder+"/train")
    if not os.path.exists(folder+"/train/images"):
        os.makedirs(folder+"/train/images")
    if not os.path.exists(folder+"/train/labels"):
        os.makedirs(folder+"/train/labels")

    # Downloading images
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

    for index, image in enumerate(results["images_results"]):

        try:
            print(f"Downloading {index} image...",index)

            # filepath is current working directory + folder/train/images or labels + params["q"] + index + .jpg
            filepath = os.path.join(folder+"/train/images", params["q"] +str(num) +str(index) +".jpg")
            labelpath = os.path.join(folder+"/train/labels", params["q"] + str(num)+str(index) +".txt")
            response = requests.get(image['original'], headers=headers).content
            #writes image to file
            with open(filepath, "wb") as f:
                f.write(response)

            #writes annotation on corresponding label file
            get_cordinates(filepath,labelpath,clas)
        except Exception as e:
            print(e)
            print(f"Error downloading {index} image. Error =", e)
folder =input("Enter folder path:")
api =input("Enter google api key:")
while not os.path.exists(folder):

    if input("This path doesn't exist do you want to create new folder?(y/n)").strip().lower()=="y":
        os.makedirs(folder)
        break;
    folder =input("Re-Enter folder path:")


while True:
    species=input("Enter species:")
    clas=int(input("What class number:"))
    set_species=species
    try:
        if lis[clas] != species:
            if not input("The species name you entered is different from the one already stored in class "+str(clas)+". Would you like to change the name of class "+str(clas)+"(y/n)?").strip().lower()=="y":
                set_species=lis[clas]
            print("Class "+str(clas)+" is set to "+set_species)
    except:
        print("Adding new class "+str(clas)+" as species "+species+"")
    num=int(input("What page of google:"))
    get_google_images(species,clas,num,folder,api)
    data_file=list(open(folder+"/data.yaml","r"))

    num=int(data_file[1][3:])

    lis=data_file[2][6:].replace("[","").replace("]","").split(',')

    while clas>num-1:
        lis.append("")
        num+=1

    lis[clas]=set_species
    data_file=open(folder+"/data.yaml","w")
    data_file.write("train: ../train/images\nnc: "+str(num)+"\nnames: "+str(lis))


