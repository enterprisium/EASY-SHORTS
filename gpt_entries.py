import google.generativeai as genai

# Set the API key and configure the model
genai.configure(api_key='AIzaSyC6N1MVe9WmAFjWMNuXjlaLnYa8eO813tY')
model = genai.GenerativeModel('gemini-pro')

def gpt_entry(niche):
    ideas = []
    try:
        prompt = f"You are a YouTube content creator. You are making videos about {niche}. I need 5 title ideas for my YouTube channel about {niche}. Format the titles into 5 bullet points."
        response = model.generate_content(prompt)
        results = response.text.splitlines()
        for result in results:
            if result.strip():  # Only add non-empty lines
                ideas.append(result.strip())
    except Exception as e:
        print(f"Error generating video ideas: {e}")
    return ideas

def gpt_script(subject):
    try:
        prompt = f"You are creating voice-overs for short videos (about 1 minute long), you sound very clever and also funny. I need short voice-over text for about 1500 characters about: {subject}. I don't need any instructions according to video and anything else."
        response = model.generate_content(prompt)
        script = response.text
    except Exception as e:
        print(f"Error generating script: {e}")
        script = ""
    return script

def gpt_reformat(subject):
    script = gpt_script(subject)
    try:
        prompt = f"{script} reformat this script into one paragraph remove any instructions to the video, I need just pure text."
        response = model.generate_content(prompt)
        reformatted_script = response.text
    except Exception as e:
        print(f"Error reformating script: {e}")
        reformatted_script = script
    return reformatted_script
