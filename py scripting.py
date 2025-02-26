# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(description)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import pandas as pd
import openai
import time

# Set your OpenAI API key


# Define a function to call the OpenAI API for classifying the ticket
def classify_ticket(ticket_text):
    # Construct the prompt to extract the software or site name
    prompt = (
        "Extract the software or site that experienced a problem from the following ticket description. "
        "If nothing is clear, return 'Unknown'.\n\nTicket Description:\n" + ticket_text
    )
    
    try:
        # Call the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # or your preferred engine
            prompt=prompt,
            max_tokens=20,              # adjust as needed for concise responses
            temperature=0.0,            # low temperature for deterministic output
            n=1,
            stop=None
        )
        # Parse and return the result, ensuring that only the text is returned
        software_site = response.choices[0].text.strip()
        # Basic cleaning: if empty, mark as Unknown
        if not software_site:
            return "Unknown"
        return software_site
    except Exception as e:
        # If there's an error (e.g., API rate limit), return a placeholder and optionally log the error
        return "Error"

# Assuming 'dataset' is the DataFrame automatically loaded by Power BI with your data
# and that it contains a column named 'Ticket Description'

# Create a new column 'Software/Site' by applying the classify_ticket function to each ticket description
dataset['Software/Site'] = dataset['Ticket Description'].apply(classify_ticket)

# Optional: If you have many records, consider adding a delay to avoid rate limits
# for index, row in dataset.iterrows():
#     dataset.at[index, 'Software/Site'] = classify_ticket(row['Ticket Description'])
#     time.sleep(1)  # wait one second between calls, adjust as needed

# The DataFrame 'dataset' with the new 'Software/Site' column is returned to Power BI
result = dataset
