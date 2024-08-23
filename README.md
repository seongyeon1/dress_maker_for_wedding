## 드레스 피팅 시 대화를 바탕으로 드레스를 복원하자

### llm model
- input : 대화 데이터셋
- output : 대화에서 등장하는 드레스의 묘사 (프롬프트의 형식)

### Image Generation
- input : llm model의 output
- output : 내가 입어봤던 드레스

### Example
llm model (`solar`)

#### input :

```text
이 대화를 바탕으로 드레스의 이미지를 묘사해줘
<드레스 착용 전>
실장 : 신부님 피부 톤이 살짝 있으셔서 완전 화이트보다는 살짝 아이보리 톤이 들어가고 광택감이 있는 미카도 실크가 어울리실 것 같아요. 혹시 드레스 선택하실 때 생각했던 디자인 있으실까요?
신부 : 제가 팔뚝 살이 좀 있어서 팔을 좀 가리는 디자인이면 좋겠어요.
실장 : 슬리브 있는 드레스는 오히려 팔을 드러낼 수 있어서 오프숄더 디자인이 오히려 팔이 얇아보이실거에요. 오프숄더 디자인으로 한번 준비해드릴게요.
<드레스 착용 후>
실장 : 너무 잘 어울리세요. 베일도 투 베일로 해서 베일로 시선 집중을 시켜서 팔이 더 얇아보이는 효과가 있어요. 신부님이 키가 있으셔서 살짝 슬림한 A라인으로 떨어지는 디자인이 날씬하게 보이는 효과가 있어요. 혹시 티아라는 하실건가요?
신부 : 아뇨, 티아라는 괜찮아요.
실장 : 맞아요. 이 드레스가 작은 비즈가 촘촘히 박혀있어서, 아래쪽이 화려하다보니 티아라까지 하면 좀 투머치일 수 있어요. 식장은 어디쪽으로 잡으셨어요?
신부 : 빌라드지디 청담으로 잡았어요.
실장 : 빌라드지디가 밝은 홀이라 레이스 없이 깔끔한 이런 디자인이 잘 어울려요. 식장이랑도 잘 어울리겠네요.
```

#### keyword

```text
{
  '기본 정보': {
    '스타일': '클래식',
    '원단': '미카도 실크',
    '색상': '아이보리'
  },
  '상세한 디자인': {
    '실루엣': 'A라인',
    '넥라인': '오프숄더',
    '소매': '없음',
    '트레인': '미기재',
    '디테일': '비즈 장식'
  },
  '설명': '아이보리 색상의 미카도 실크로 만들어진 클래식한 디자인의 드레스입니다. A라인 실루엣으로 슬림한 핏을 연출하며, 오프숄더 네크라인으로 팔을 가리는 효과를 줍니다. 소매는 없으며, 트레인은 언급되지 않았습니다. 비즈 장식이 전체적으로 촘촘히 박혀있어 화려하고 고급스러운 느낌을 줍니다.'
}
```

<br>
아래 페이지에 사용할 정보가 됨

![keyword](https://github.com/user-attachments/assets/728a994c-8d26-4c5a-b354-833ad08e8e69)


### 이미지 생성
</br>

#### 1. 이미지 생성의 input으로 넣을 prompt 생성 : <br>
- input : 전체 대화<br>
- output :<br>

```text
A front view of a bridal dress in a slightly ivory tone with a glossy mikado silk texture. The dress features an off-shoulder design with a slightly slimmer A-line shape that falls gracefully to the floor. The dress has a fitted bodice with a cinched waist, accentuating the bride's figure. The skirt is full and flared, with a small train at the back. The dress has a simple, elegant design, with a subtle pattern of small, 촘촘히 박혀있는 비즈. The dress is paired with a veil that is held up by a headpiece, adding a touch of elegance to the overall look. No human figure included. Sketch style, black and white line art.
```

#### 2. 프롬프트(위의 output)를 바탕으로 이미지 생성<br>
- 결과 :
![img](https://fal.media/files/lion/VxlsjwZ0g1iw8Q-YKFN-C.png)


### Setup

### 사용법
1. terminal에서 보고 싶을 때
```bash
make run-terminal
```

2. fastapi
```bash
make all
```
- http://0.0.0.0:8000 에서 실행

```bash
curl -X 'POST' \
  'http://localhost:8000/generate-dress/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "dialogue": "대화 내용"
}'
```
Response body
```bash
{
  "images": [
    {
      "url": "url",
      "width": 1024,
      "height": 768,
      "content_type": "image/jpeg"
    }
  ],
  "timings": {
    "inference": 2.1728938709711656
  },
  "seed": 207009889,
  "has_nsfw_concepts": [
    false
  ],
  "prompt": "프롬프트 결과"
}
```


### directory
```
.
├── Dockerfile
├── Makefile
├── requirements.txt
├── run.sh
├── app
│   ├── __init__.py
│   ├── app.py
│   ├── main.py
│   └── services
│       ├── conf.py
│       ├── templates.py
│       ├── dress_generation.py
│       └── dialogue_extraction.py
│ 
├── test : 테스트 파일이 있습니다
│   └── make_dress_demo files...
└── .env

```
