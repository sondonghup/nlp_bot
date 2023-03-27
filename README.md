# RECA bot

### summary
```
.
├── README.md
├── apis
│   ├── chat_deploy.py
│   ├── configs
│   │   ├── v0.0.1-chat.json
│   │   └── v0.0.1-sent.json
│   ├── models
│   │   ├── chat.py
│   │   └── sent.py
│   └── sent_deploy.py
├── bot.py
└── funcs
    ├── food_func.py
    └── weather_func.py
```

### func
- #### sent
<img width="605" alt="image" src="https://user-images.githubusercontent.com/42092560/228042014-b444cfaf-5b77-4aec-bb73-52d62f2f1806.png">

```
$sent [대화 내용]
```

- #### chat
![image](https://user-images.githubusercontent.com/42092560/228039447-dd4b7ae3-451b-4e34-b1cd-d157a3dd4fe3.png)

```
$chat [대화 내용]
```

- #### youtube music
<img width="827" alt="image" src="https://user-images.githubusercontent.com/42092560/228041016-25e402db-0510-4010-af6a-d12b66d21d3c.png">

```
$join

$play [노래 제목]
```

- #### weather alert
<img width="588" alt="image" src="https://user-images.githubusercontent.com/42092560/228042254-0b97c201-d6de-454a-bea5-85d6026756ef.png">

```
$weather [전국]
```

<img width="616" alt="image" src="https://user-images.githubusercontent.com/42092560/228042475-f29f74b9-bb24-413e-aa95-9786706d3204.png">

```
$weather [주소]
```

- #### food alert
<img width="624" alt="image" src="https://user-images.githubusercontent.com/42092560/228043214-548c2952-bb61-4bcf-8b8e-7eaac5b0fd79.png">

```
$food [주소]
```

### uses
```
$ python3 bot.py
$ python3 /apis/chat_deploy.py
$ python3 /apis/sent_deploy.py
```
