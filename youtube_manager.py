import json 

def load_data():
     try:
          with open('youtube.txt','r') as file:
             return  json.load(file)
     except FileNotFoundError:
         return []
     
def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos,file)     

def list_all_videos(videos):
    if len(videos) == 0:
        print("No videos available")
    else:    
    # you will be getting videos as json format if exists so to index them you use enumerate
       for index,video in enumerate(videos,start=1):
          print(f"{index}. {video['name']}, Duration : {video['time']}")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name' : name,'time':time})
    save_data(videos)

def update_video(videos):
    list_all_videos(videos) 
    index = int(input("Enter index to be updated: "))
    if 1 <= index <= len(videos):
        name = input("Enter video name: ")
        time = input("Enter video time: ")
        videos[index - 1] = {'name' : name, 'time': time}
        save_data(videos)
    else:
        print("Invalid index selcted")    

def delete_video(videos):
    list_all_videos(videos) 
    index = int(input("Enter index to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data(videos)
    else:
        print("Invalid index selcted") 

def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager  | Choose an option")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video ")
        print("4. Delete a youtube video ")
        print("5. Exit")
        choise = input("Enter your choise: ")

        match choise:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)   
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choise")       


if __name__ ==  "__main__":
         main()                 