
from podcast_chatbot.data import parsed, episode_summary, parsed_summary
from llama_index import Document


print(episode_summary[:100])



print(parsed_summary[:100])

start_of_transcript = [x.text for x in parsed_summary].index("Transcript") + 1
print(f"First line of the transcript: {start_of_transcript}")

