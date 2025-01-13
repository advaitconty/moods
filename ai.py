import anthropic
import api_key
import re

pattern = r"<selected_song>\s*(.*?)\s*</selected_song>.*?<reasoning>\s*(.*?)\s*</reasoning>"

def return_song(MOOD, SONG_LIST):
    client = anthropic.Anthropic(api_key=api_key.ANTHROPIC_API_KEY)

    message = client.messages.create(
     model="claude-3-5-sonnet-20241022",
      max_tokens=4096,
      temperature=0,
      messages=[
          {
              "role": "user",
              "content": [
                  {
                      "type": "text",
                      "text": f"You are an AI assistant tasked with selecting a song from a given list based on a specified mood. You will be provided with two inputs:\n\n<song_list>\n{SONG_LIST}\n</song_list>\n\n<mood>{MOOD}</mood>\n\nFollow these steps to complete the task:\n\n1. Carefully review the list of songs provided in the song_list.\n\n2. Consider the given mood. Think about what musical characteristics or lyrical themes might be associated with this mood.\n\n3. Analyze the songs in the list, considering their titles, artists, and any knowledge you have about their style or content. Look for songs that you believe would match or evoke the specified mood.\n\n4. Select one song from the list that you think best fits the given mood. If multiple songs seem equally suitable, choose the one you believe is the strongest match.\n\n5. Provide your answer in the following format:\n\n<selected_song>\n[Artist] - [Song Title]\n</selected_song>\n\n<reasoning>\nBriefly explain why you chose this song and how it relates to the given mood. Limit your explanation to 2-3 sentences.\n</reasoning>\n\nRemember, you should only select a song that is present in the provided song_list. Do not suggest songs that are not on the list, even if you think they would be a good fit for the mood."
                  }
              ]
          }
      ]
    )

    match = re.search(pattern, message.content[0].text, re.DOTALL)

    if match:
        result = {
            "selected_song": match.group(1).strip(),
            "reasoning": match.group(2).strip()
        }
    else:
        return SystemError("No match found")
    
    return result

if __name__ == "__main__":
    print(return_song("emotional", ["BoyWithUke - Burnout", "BoyWithUke - Trauma", "JVKE - golden hour"])) # Change the mood and song list as needed
