import os
import groq

api_key = os.environ.get("GROQ_KEY")
if not api_key:
    api_key = input("Enter your Groq API Key: ")

client = groq.Groq(api_key=api_key)

def start():
    print("\n🦾 THING OS: LIVE.")
    while True:
        cmd = input("Onesmus >> ")
        if cmd.lower() in ['exit', 'quit']: break
        resp = client.chat.completions.create(
            messages=[{"role": "system", "content": "You are THING."},
                      {"role": "user", "content": cmd}],
            model="llama3-70b-8192")
        print(f"\nTHING: {resp.choices[0].message.content}\n")

if __name__ == "__main__":
    start()
