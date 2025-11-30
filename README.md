# Quick Start

## Sign in to [X Developer Platform](https://developer.x.com)

1. Edit the *User authentication settings* of Project App in [Dashboard](https://developer.x.com/en/portal/dashboard), set App permissions as Read and write(the rest of settings don't matter)
2. Get the **Access Key and Secret** and **API Key and Secret** of Project App
3. Save them into wherever you like in the format like this:

```
API_KEY=xxxxxxxx
API_SECRET=xxxxxxxxx
ACCESS_TOKEN=xxxxxxx
ACCESS_TOKEN_SECRET=xxxxxxx
```
4. Change the KeyScretPath into your own path in *onlyPush.py*
> eg: "/User/eleph/Documents/OAuth/x.txt"

5. Change the directory into where you want to save your tweet locally in *onlyPush.py*
> eg: "User/eleph/Documents/Tweet/"

6. Start with below:
``` python
Source venv/bin/activate #.fish for fish, .csh for csh
python ./onlyPush.py
deactivate
```
