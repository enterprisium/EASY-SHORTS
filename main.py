from voice_gen import *
from gpt_entries import *
from video_make import *
from add_subs import *

if __name__ == "__main__":
    niche = input("choose your niche eg. 'making money': ")
    ideas = gpt_entry(niche)
    ideas = [x for x in ideas if x != ""]
    
    if not ideas:
        print("No ideas were generated. Please try again with a different niche.")
    else:
        for i, part in enumerate(ideas, 1):
            print(f"{i}. {part}")
        
        while True:
            try:
                choice = int(input(f'pick your desired video (from 1 to {len(ideas)}): '))
                if 1 <= choice <= len(ideas):
                    break
                else:
                    print(f'wrong input, type in value between 1 and {len(ideas)}')
            except ValueError:
                print("Please enter a valid number.")
        
        script = gpt_reformat(ideas[choice - 1])
        generate_voice_over(script)
        make_vid(niche)
        add_subtitles('voice_over.mp3')
