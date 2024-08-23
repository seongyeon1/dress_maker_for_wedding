# main.py

from services.dialogue_extraction import extract_dress_info
from services.dress_generation import generate_dress

def main():
    # Sample data
    dialogue = input()

    print('Extracting dress information from the dialogue...')
    dress_prompt = extract_dress_info(dialogue)
    print(f'Generated prompt for the dress: {dress_prompt}')

    print('Generating dress image...')
    dress_image = generate_dress(dress_prompt)
    print('Dress image generated successfully!')
    print(dress_image)

if __name__ == "__main__":
    main()