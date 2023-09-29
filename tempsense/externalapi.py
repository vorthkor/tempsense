import requests


def notHere():
    url = "https://http.cat/404"
    response = requests.get(url)

    if response.status_code == 200:
        with open("photo.png", mode="wb") as f:
            f.write(response.content)
    else:
        return f'Request failed with status code:{response.status_code}'
    

def catPic():
    url =  'https://cataas.com/cat?json=true'
    url_res = 'https://cataas.com'
    response = requests.get(url)

    if response.status_code == 200:
        img_url = response.json()['url']
        img = url_res+img_url
        res = requests.get(img)
        with open("photo.png", mode="wb") as f:
                f.write(res.content)
    else:
        return f'Request failed with status code:{response.status_code}'


def duckPic():
    url =  'https://random-d.uk/api/v2/random'
    response = requests.get(url)

    if response.status_code == 200:
        img = response.json()['url']
        res = requests.get(img)
        with open("photo.png", mode="wb") as f:
                f.write(res.content)
    else:
        return f'Request failed with status code:{response.status_code}'


def foxPic():
    url =  'https://randomfox.ca/floof/'
    response = requests.get(url)

    if response.status_code == 200:
        img = response.json()['image']
        res = requests.get(img)
        with open("photo.png", mode="wb") as f:
                f.write(res.content)
    else:
        return f'Request failed with status code:{response.status_code}'


def dogPic():
    url =  'https://random.dog/woof.json'
    response = requests.get(url)

    if response.status_code == 200:
        img = response.json()['url']
        res = requests.get(img)
        with open("photo.png", mode="wb") as f:
                f.write(res.content)
    else:
        return f'Request failed with status code:{response.status_code}'


def cafePic():
    url = "https://coffee.alexflipnote.dev/random.json"
    response = requests.get(url)

    if response.status_code == 200:
        res = response.json()['file']
        img = requests.get(res)
        with open("photo.png", mode="wb") as f:
                    f.write(img.content)
    else:
        return f'Request failed with status code:{response.status_code}'

    
def lastMars(opt):
    url = 'https://mars-photos.herokuapp.com/api/v1/rovers/curiosity/latest_photos'
    response = requests.get(url)

    if response.status_code == 200:
        if opt == 1:
            photo = response.json()["latest_photos"][1]["img_src"]
            res = requests.get(photo)
            with open("photo.png", mode="wb") as f:
                f.write(res.content)
        else:
            date = response.json()["latest_photos"][1]["earth_date"]
            rover = response.json()["latest_photos"][1]["rover"]["name"]
            camera = response.json()["latest_photos"][1]["camera"]["full_name"]
            return f'🌠 The last Mars picture was taken by the {camera} camera 📸 from the {rover} rover 🛰️ at {date} ☄️'
    else:
        return f'Request failed with status code:{response.status_code}'


def lastAstro(opt):
    url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
    response = requests.get(url)

    if response.status_code == 200:
        if opt == 1:
            photo = response.json()["url"]
            res = requests.get(photo)
            with open("photo.png", mode="wb") as f:
                f.write(res.content)
        else:
            phrs = response.json()["explanation"]
            date = response.json()["date"]
            return f"🌌 Here's the explanation of the astronomy picture of {date}: \n {phrs} 🔭"
    else:
        return f'Request failed with status code:{response.status_code}'


def bbPhrase():
    url =  'https://api.breakingbadquotes.xyz/v1/quotes'
    response = requests.get(url)

    if response.status_code == 200:
        quote = response.json()[0]['quote']
        author = response.json()[0]['author']
        return f' 🧪 {quote} - {author} 🔫'
    else:
        return f'Request failed with status code:{response.status_code}'


def meowFacts():
    url =  'https://meowfacts.herokuapp.com/'
    response = requests.get(url)

    if response.status_code == 200:
        quote = response.json()['data'][0]
        return f'cat fact 🐱: {quote} 🐈'
    else:
        return f'Request failed with status code:{response.status_code}'


def spacePeople():
    url =  'http://api.open-notify.org/astros.json'
    response = requests.get(url)

    if response.status_code == 200:
        people = response.json()['number']
        return f'🦸 There are {people} people 🧑‍🚀👨‍🚀👩‍🚀 in the space 🚀 right now 🤯'
    else:
        return f'Request failed with status code:{response.status_code}'


def doBored():
    url = 'https://www.boredapi.com/api/activity/'
    response = requests.get(url)

    if response.status_code == 200:
        act = response.json()['activity']
        type = response.json()['type']
        participants = response.json()['participants']
        price = response.json()['price']
        return f'feeling bored? 🤷 you can {act} 😋, it`s {type} 😱, up to {participants} people 👥 and for the price of {price} moneys 🤑'
    else:
        return f'Request failed with status code:{response.status_code}'


def corporate():
    url = "https://corporatebs-generator.sameerkumar.website/"
    response = requests.get(url)

    if response.status_code == 200:
        res = response.json()['phrase']
        return f'corporate bullshit be like: {res}'
    else:
        return f'Request failed with status code:{response.status_code}'


def rndFacts():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    response = requests.get(url)

    if response.status_code == 200:
        res = response.json()['text']
        return f'here some useless fact 🧐: {res}'
    else:
        return f'Request failed with status code:{response.status_code}' 


def techGib():
    url = "https://techy-api.vercel.app/api/json"
    response = requests.get(url)

    if response.status_code == 200:
        res = response.json()['message']
        return f'Gibberish tech 🖥️: {res}'
    else:
        return f'Request failed with status code:{response.status_code}' 


def mathrivia():
    url = "http://numbersapi.com/random/trivia?json"
    response = requests.get(url)

    if response.status_code == 200:
        res = response.json()['text']
        return f'Some random number fact: {res}'
    else:
        return f'Request failed with status code:{response.status_code}' 
