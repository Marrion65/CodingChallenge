# Import libraries

from datetime import datetime

# In memory storage for events
events = []


# Add events

def add_event(title, description, date, time):
    try:
        # Validate date and time format
        event_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        event = {"title": title, "description": description, "datetime": event_datetime}
        events.append(event)
        print("Event has been added successfully.")
    except ValueError:
        print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")

# List all the events        

def list_events():
    if not events:
        print("No events found.")
        return

    # Sort events by date and time
    sorted_events = sorted(events, key=lambda x: x["datetime"])
    
    # Display all events
    for event in sorted_events:
        print(f"\nTitle: {event['title']}\nDescription: {event['description']}\nDate and Time: {event['datetime']}")

# Delete events

def delete_event(title):
    global events
    # Find the index of the event with the specified title
    event_index = next((index for index, event in enumerate(events) if event["title"] == title), None)

    if event_index is not None:
        # Remove the event if found
        del events[event_index]
        print(f"Event '{title}' deleted successfully.")
    else:
        print(f"Event '{title}' not found.")

# Edit events

def edit_event_by_title():
    title_to_edit = input("Enter the title of the event to edit: ")
    for event in events:
        if event['title'] == title_to_edit:
            new_title = input("Enter new event title (leave blank to keep current): ")
            new_description = input("Enter new event description (leave blank to keep current): ")
            new_date = input("Enter new event date and time (YYYY-MM-DD HH:MM) (leave blank to keep current): ")
            new_time = input("Enter new event date and time (YYYY-MM-DD HH:MM) (leave blank to keep current): ")

            if new_title:
                event['title'] = new_title
            if new_description:
                event['description'] = new_description
            if new_date:
                event['date'] = new_date
            if new_time:
                event['time'] = new_time

            print(f"Event '{title_to_edit}' has been edited successfully!")
            return

    print(f"Event with title '{title_to_edit}' not found.")

# Search for existing events    

def search_events():
    search_term = input("Enter search term (date, title, or description): ")
    found_events = []

    for event in events:
        if  (search_term in event['title']) or (search_term in event['description']) or (search_term in event['datetime']):
            found_events.append(event)

    if found_events:
        print("\nFound Events:")
        for found_event in found_events:
            print(f"\nTitle: {event['title']}\nDescription: {event['description']}\nDate and Time: {event['datetime']}")
    else:
        print("No events found.")

# Main

if __name__ == "__main__":
    while True:
        print("\nEvent Scheduler Application Menu:")
        print("1. Add Event")
        print("2. List Events")
        print("3. Delete Event")
        print("4. Edit Event")
        print("5. Search Events")
        print("0. Exit")

        # choice input
    
        choice = input("Enter your choice (1 or 2 or 3 or 4 or 5 or 0): ")

        if choice == "1":
            title = input("Enter event title: ")
            description = input("Enter event description: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            add_event(title, description, date, time)

        elif choice == "2":
            list_events()

        elif choice == "3":
            title = input("Enter title of the event you want to delete: ")
            delete_event(title)

        elif choice == "4":
            edit_event_by_title()

        elif choice == "5":
            search_events()

        elif choice == "0":
            print("Exiting Event Scheduler")
            break

        else:
            print("Invalid option. Please choose a valid option.")


