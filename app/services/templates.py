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

- Use simple and clear language that the generator can easily understand.
- Keep your prompts concise, avoiding overly detailed descriptions that might confuse the system.
- Incorporate descriptive words that capture the subject and layout of the image.
- Avoid contradictory terms that could confuse the AI in determining the style or content.

---------

Here's an example of a great prompt:

"A beautiful, flowing ball gown with a classic silhouette, square neckline, and cinched waist. Emphasize the elegant drape of the fabric and the full skirt. Sketch style, black and white line art."

-----

Now, create a prompt.

### REMEMBER to add "Sketch style, black and white line art" at the end of the prompt.
### PROMPT:
"""