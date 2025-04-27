import json

def helper(videos):
    with open('video_maneger.txt', 'w') as file:
        json.dump(videos, file)


def load_data():
    try:
        with open('video_data.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return[]
 
    
def list_all_video(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate (videos, start=1):
        print(f"{index}.Video: {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 70)


def add_video(videos):
    name = input('Enter Video Name : ')
    time = input('Enter Video Time : ')
    videos.append({'name':name ,'time':time})
    helper(videos)


def update_video(videos):
    list_all_video(videos)
    index = int(input("Enter the video number to update : "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name : ")
        time = input("Enter the new video time : ")
        videos[index-1] = {'name':name, 'time': time}
        helper(videos)
    else:
        print("Invalid index selected")


def delete_video(videos):
    list_all_video(videos)
    index = int(input("Enter the video number to be deleted : "))
    if 1<= index <= len(videos):
        del videos[index-1]
        helper(videos)
    else:
        print("Invalid video index selected")


def main():
    videos = load_data()
    while (True):
        print("\n Video Maneger | Choies an Option")
        print("01: List all videos")
        print("02: Add a Video")
        print("03: Update a Video")
        print("04: Delete a Video")
        print("05: Exit ")
        choies = input("Enter a Choies : ")
        
        match choies:
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choies")
    


if __name__ == "__main__":
    main()
    