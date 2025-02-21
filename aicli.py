import openai
import subprocess
import os
from prompt_toolkit import prompt
import shlex

# Replace with your OpenAI API key
OPENAI_API_KEY = "key"

def ask_openai(question):
    """Queries OpenAI and returns the response."""
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": (
                "You are a command-line assistant running in a macOS terminal. "
                "When the user asks for a command, always provide a valid shell command inside a code block like this:\n"
                "```sh\n<command_here>\n```\n"
                "generate the command considering the most human readable outputs"
                "If the user does not ask for a command, answer normally."
            )},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content.strip()

def check_for_command(response):
    """Checks if the AI response contains a command and asks for execution."""
    import re
    match = re.search(r"```sh\s*(.*?)\s*```", response, re.DOTALL)
    if match:
        command = match.group(1).strip()
        print(f"\n🔹 Suggested command: {command}\n")

        confirm = prompt("Do you want to execute this command? (y/N): ").strip().lower()
        if confirm == "y":
            args = shlex.split(command)
            subprocess.run(args)
            print("\nExecuting command...\n")
            subprocess.run(command, shell=True)
        else:
            print("\nCommand execution skipped.")
    else:
        print(response)

def interactive_shell():
    print("\n🚀 AI Terminal - Ask anything (type 'exit' or 'quit' to stop)\n")

    while True:
        try:
            question = prompt("You: ").strip()
            
            if question.lower() in ["exit", "quit"]:
                print("\n👋 Goodbye!\n")
                break

            response = ask_openai(question)
            check_for_command(response)

        except KeyboardInterrupt:
            print("\n\n👋 Exiting... Have a great day!\n")
            break
        except openai.error.OpenAIError as e:
            print(f"\n❌ OpenAI API Error: {e}\n")
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Subprocess Error: {e}\n")
        except KeyboardInterrupt:
            print("\n\n👋 Exiting... Have a great day!\n")
            break
        except Exception as e:
            print(f"\n❌ Unexpected Error: {e}\n")
        except Exception as e:
            print(f"\n❌ Error: {e}\n")

def main():
    interactive_shell()

if __name__ == "__main__":
    main()
