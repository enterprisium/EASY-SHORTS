import google.generativeai as genai

# Set the API key directly in the file
genai.api_key = 'AIzaSyC6N1MVe9WmAFjWMNuXjlaLnYa8eO813tY'

def gpt_entry(niche):
    ideas = []
    try:
        response = genai.generate_text(
            model="gemini-pro",
            prompt=f"You are a YouTube content creator. You are making videos about {niche}. I need 5 title ideas for my YouTube channel about {niche}. Format the titles into 5 bullet points."
        )
        results = response.result.splitlines()
        for result in results:
            ideas.append(result)
    except Exception as e:
        print(f"Error generating video ideas: {e}")
    return ideas

def gpt_script(subject):
    try:
        response = genai.generate_text(
            model="gemini-pro",
            prompt=f"You are creating voice-overs for short videos (about 1 minute long), you sound very clever and also funny. I need short voice-over text for about 1500 characters about: {subject}. I don't need any instructions according to video and anything else."
        )
        script = response.result
    except Exception as e:
        print(f"Error generating script: {e}")
        script = ""
    return script

def gpt_reformat(subject):
    script = gpt_script(subject)
    try:
        response = genai.generate_text(
            model="gemini-pro",
            prompt=f"{script} reformat this script into one paragraph remove any instructions to the video, I need just pure text."
        )
        reformatted_script = response.result
    except Exception as e:
        print(f"Error reformating script: {e}")
        reformatted_script = script
    return reformatted_script
