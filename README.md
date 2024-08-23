## 드레스 피팅 시 대화를 바탕으로 드레스를 복원하자

### llm model
- input : 대화 데이터셋
- output : 대화에서 등장하는 드레스의 묘사 (프롬프트의 형식)

### Image Generation
- input : llm model의 output
- output : 내가 입어봤던 드레스

### Example
llm model (`solar`)

input :
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
output :
```text
Prompt:
Create a detailed illustration of a bride wearing an elegant Jamie Bridal gown made of off-shoulder, sleeveless, and slightly slimmer A-line silhouette with a pure feminine style.
The dress should be made of a luxurious and opulent Mikado silk fabric with a slight ivory tone and a subtle sheen.
The dress should have a high-quality, well-crafted look, with intricate details such as delicate beading and embroidery.
The bride should have a natural, glowing makeup look, with her hair styled in a sophisticated updo.
The background should be a lush garden setting with vibrant greenery and flowers, with a soft, natural lighting effect.
The overall mood of the illustration should be romantic, elegant, and timeless.
```

Image Generation :
![image](https://github.com/user-attachments/assets/438cd7ce-eadd-48c5-80d5-a1354abaa195)

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
└── .env
```