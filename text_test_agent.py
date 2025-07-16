# text_test_agent.py
from scheduler_agent import ask_agent
from calendar_utils import get_available_slots

def main():
    print("SmartScheduler AI is ready! Type 'exit' to quit.")
    print("You can ask things like: 'I need to schedule a meeting'")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break

        # Check if user wants to schedule a meeting
            if "schedule" in user_input.lower() and "meeting" in user_input.lower():
                print("Agent: Checking your calendar...")
                slots = get_available_slots(duration_minutes=60, day='Tuesday', time_pref='afternoon')  # You can customize
                print("Agent: I found these available slots:")
                for slot in slots:
                    print(f"  - {slot}")
                continue  

        # Otherwise, send to LLM as usual
            response = ask_agent(user_input)
            print("Agent:", response)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 