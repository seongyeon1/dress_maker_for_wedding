dialogue = """
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
"""
system_prompt = """
기본정보와 상세 디자인 정보를 바탕으로 대화에 나오는 드레스에 대해 최대한 상세하게 설명해주세요.

----
### FORMAT :
{
  '기본정보' : {
    '스타일' : '클래식',
    '원단' : '미카도 실크',
    '컬러' : '아이보리'
  },
  '상세 디자인': {
    '스타일' : '오프숄더',
    '스트랩' : '없음',
    '디테일' : '비즈 장식'
  }
  '설명' : '${드레스묘사}'
}
-----
### 반드시 JSON 형식으로 답변하세요.
  
### Description :
"""

img_maker_prompt = """
You are an expert Prompt Writer for image generation. 
Your goal is to create a prompt based on the given dialogue to guide the image generator in creating a sketch:

--------------------

Dialogue: {dialogue}

--------------------

Guidelines for crafting effective prompts:

- Focus on the front view of the clothing only. Ensure the prompt emphasizes the design, details, and features of the clothing from the front.
- Make sure that no person or human figure is included in the sketch, only the clothing itself.
- Use simple and clear language that the generator can easily understand.
- Keep your prompts concise, avoiding overly detailed descriptions that might confuse the system.
- Incorporate descriptive words that capture the subject and layout of the clothing.
- Avoid contradictory terms that could confuse the AI in determining the style or content.

---------

### EXAMPLE:
A front view of a beautiful, flowing ball gown with a classic silhouette, square neckline, and cinched waist. Emphasize the elegant drape of the fabric and the full skirt. No human figure included. Sketch style, black and white line art.

-----

Now, create a prompt.

### REMEMBER to add "Sketch style, black and white line art" at the end of the prompt.
### REMEMBER: Answer in ENGLISH
### PROMPT:
"""