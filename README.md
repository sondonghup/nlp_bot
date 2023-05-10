# RECA bot
***
I added several nlp tasks and other necessary functions to the discord bot by api.
If I think of any fun features, I will continue to add them.

### summary
```
.
├── README.md
├── apis
│   ├── chat_deploy.py
│   ├── configs
│   │   ├── v0.0.1-chat.json
│   │   ├── v0.0.1-sent.json
│   │   └── v0.0.1-summarize.json
│   ├── models
│   │   ├── chat.py
│   │   ├── sent.py
│   │   └── summarize.py
│   ├── sent_deploy.py
│   └── summarize_deploy.py
├── bot.py
└── funcs
    ├── food_func.py
    └── weather_func.py
```

### func
- #### sent
It is a function that classifies seven emotions.
[중립], [행복], [당황], [분노], [불안], [슬픔], [혐오]

```
$sent 너무 짜증나
> 분노
$sent 너무 무서워..
> 불안
```

- #### chat
It is a chatbot produced by learning KakaoTalk group chat conversation through gpt2.
There's still a lot to be fixed.
```
$chat 안녕
> ㅋㅋㅋㅋ 안녕 롤 ㄱ?
```

- #### youtube music
It plays the most popular video by searching for songs on YouTube.

```
$join
> join 일반 channel
$play 하늘바라기
```

- #### weather alert
It tells you the weather and temperature of the country.

```
$weather 전국
>[울릉/독도] 기온 : 8.0 | 날씨 : 흐림
[제주] 기온 : 13.0 | 날씨 : 흐림
[안동] 기온 : 9.6 | 날씨 : 흐림
[수원] 기온 : 14.4 | 날씨 : 흐림
[부산] 기온 : 14.1 | 날씨 : 흐림
[전주] 기온 : 11.4 | 날씨 : 맑음
[울산] 기온 : 10.9 | 날씨 : 흐림
[광주] 기온 : 11.6 | 날씨 : 구름많음
[대전] 기온 : 11.3 | 날씨 : 흐림
[춘천] 기온 : 15.5 | 날씨 : 흐림
[서울] 기온 : 14.9 | 날씨 : 맑음
[여수] 기온 : 12.1 | 날씨 : 구름많음
[청주] 기온 : 11.1 | 날씨 : 흐림
[목포] 기온 : 10.6 | 날씨 : 구름많음
[강릉] 기온 : 10.2 | 날씨 : 흐림
[대구] 기온 : 12.0 | 날씨 : 흐림
[백령] 기온 : 6.9 | 날씨 : 맑음
```


```
$weather 대구 광역시 달서구
>[2023년 3월 23일 목요일] 날씨 : 흐림/비/안개 | 최저 온도 : 14.5 | 최고 온도 : 16.4
[2023년 3월 24일 금요일] 날씨 : 흐림/안개/황사 | 최저 온도 : 9.9 | 최고 온도 : 15.3
[2023년 3월 25일 토요일] 날씨 : 흐림/황사 | 최저 온도 : 9.0 | 최고 온도 : 12.4
[2023년 3월 26일 일요일] 날씨 : 구름조금/비 | 최저 온도 : 7.6 | 최고 온도 : 18.4
[2023년 3월 27일 월요일] 날씨 : 맑음 | 최저 온도 : 4.1 | 최고 온도 : 16.7
```


```
$weekweather 상인동
>[3.30. 오늘] 
오전 강수율 : 0% | 오후 강수율 : 10% | 최저 기온 : 8° | 최고 기온 : 24° | 오전 날씨 : 맑음 | 오후 날씨 : 맑음
[3.31. 내일] 
오전 강수율 : 10% | 오후 강수율 : 0% | 최저 기온 : 10° | 최고 기온 : 25° | 오전 날씨 : 맑음 | 오후 날씨 : 맑음
[4.01. 토] 
오전 강수율 : 0% | 오후 강수율 : 0% | 최저 기온 : 9° | 최고 기온 : 24° | 오전 날씨 : 맑음 | 오후 날씨 : 맑음
[4.02. 일] 
오전 강수율 : 0% | 오후 강수율 : 0% | 최저 기온 : 10° | 최고 기온 : 21° | 오전 날씨 : 맑음 | 오후 날씨 : 맑음
[4.03. 월] 
오전 강수율 : 0% | 오후 강수율 : 0% | 최저 기온 : 9° | 최고 기온 : 21° | 오전 날씨 : 맑음 | 오후 날씨 : 맑음
[4.04. 화] 
오전 강수율 : 30% | 오후 강수율 : 60% | 최저 기온 : 9° | 최고 기온 : 21° | 오전 날씨 : 구름많음 | 오후 날씨 : 흐리고 비
[4.05. 수] 
오전 강수율 : 60% | 오후 강수율 : 60% | 최저 기온 : 12° | 최고 기온 : 18° | 오전 날씨 : 흐리고 비 | 오후 날씨 : 흐리고 비
[4.06. 목] 
오전 강수율 : 30% | 오후 강수율 : 30% | 최저 기온 : 12° | 최고 기온 : 20° | 오전 날씨 : 흐림 | 오후 날씨 : 흐림
[4.07. 금] 
오전 강수율 : 30% | 오후 강수율 : 30% | 최저 기온 : 10° | 최고 기온 : 18° | 오전 날씨 : 흐림 | 오후 날씨 : 흐림
[4.08. 토] 
오전 강수율 : 0% | 오후 강수율 : 0% | 최저 기온 : 7° | 최고 기온 : 19° | 오전 날씨 : 맑음 | 오후 날씨 : 맑음
```

- #### food alert
It shows 10 restaurants and ratings close to the entered address.

```
$food 고아읍
>[덕수파스타-선산점] 평점 : 4.9 거리 : 4.2km
[홍찜닭선산점] 평점 : 4.8 거리 : 4.5km
[소담-문성점] 평점 : 5.0 거리 : 5.8km
[유화선] 평점 : 4.1 거리 : 6.4km
[신대장떡볶이-봉곡도량점] 평점 : 5.0 거리 : 6.7km
[배고플땐오리다-원호점] 평점 : 5.0 거리 : 6.7km
[메가MGC커피-구미봉곡점] 평점 : 4.9 거리 : 6.9km
[용공장제육배달전문점-구미문성점] 평점 : 4.9 거리 : 7.3km
[동대문엽기떡볶이-구미원평점] 평점 : 4.7 거리 : 9.1km
[하삼동커피-신평점] 평점 : 5.0 거리 : 10.3km
```


- #### summarize
This is a generation summary model produced by fine tuning news data to the t5 model.

```
$summary 그동안 AI가 블루칼라 일자리를 파괴하고 대체할 것이라는 예측이 있어 왔다. 그런나 최근 펜실베이니아대와 챗GPT 개발사 오픈AI의 연구 결과 블루칼라만이 아니라 창작 글쓰기부터 소프트웨어 코딩에 이르기까지 거의 모든 일자리가 AI에 의해 어떤 형태로든 변화할 것으로 전망됐다고 WSJ은 소개했다.

대기업 임원들과 애널리스트들도 그런 변화가 이미 일어나고 있으며, 챗GPT와 같은 첨단 기술을 이용해 노동자들이 지루한 단순노동에서 벗어날 수 있는 방법을 찾게 됐다고 입을 모았다. 식품기업 크래프트 하인즈의 최고인사책임자(CPO) 멜리사 워넥 부사장은 “AI는 차세대 혁명이며 되돌릴 수 없다”고 밝혔다.
> AI가 블루칼라 일자리를 파괴하고 대체할 것이라는 예측이 있었으나 펜실베이니아대와 오픈AI의 연구 결과 거의 모든 일자리가 AI에 의해 변화할 것으로 전망됐다.
```

### uses
```
$ python3 bot.py
$ python3 /apis/chat_deploy.py
$ python3 /apis/sent_deploy.py
```
