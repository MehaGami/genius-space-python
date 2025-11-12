import requests

site = "https://jsonplaceholder.typicode.com/posts"
filename = "output.txt"
post_number = input("Write posts number for get: ")
output = requests.get(url=site + "/" + post_number)
print(output.text)
print("---------------------------")
print(output.headers)
body = {
    "username" : "Vasyl",
    "password" : "12321",
    "body" : "some information"
}
print("---------------------------")
post = requests.post(url=site, json=body)
print(post.status_code)
print(post.reason)
print(post.text)
with open(file=filename, mode="w") as file:
            file.write(post.text)