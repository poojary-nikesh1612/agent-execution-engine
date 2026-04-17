import requests

TOOL_REGISTRY={}

def tool(func):
    action_name=func.__name__
    action_desc=func.__doc__

    TOOL_REGISTRY[action_name]={
        'executable':func,
        'description':action_desc
    }

    return func

@tool
def word_counter(text:str)->dict:
    """
    Counts the frequency of each word in a given text string.

    Args:
        text (str): The input string of text to be analyzed.

    Returns:
        dict: A dictionary where keys are the unique words and values are their counts.
    """
    count={}
    word_list=text.split()
    for word in word_list:
        count[word]=count.get(word,0)+1
    return count

@tool
def save_report(filename:str,content:str)->str:
    """
    Add the given content to the given file and save it.

    Args:
        filename (str): The name of the file where the content will be saved.
        content (str): The information to be written in the file.
    
    Returns:
        str: A statement that says report saved successfully.
    """
    with open(filename,'w') as file:
        file.write(content)
        
    return "Report saved Successfully"

@tool
def get_weather(city:str)->str:
    """
    Fetch the current weather for a given city.

    Args:
        city (str): The name of the city for which to fetch the weather.
    
    Returns:
        str: A sentence containing the weather in Celsius.
    """
    url=f"https://wttr.in/{city}?format=%t"
    response=requests.get(url)
    return response.text

if __name__=='__main__':
    test_string="apple banana apple dog"
    print(word_counter(test_string))

    print(save_report('text.txt',' Nikesh'))
    
    print(TOOL_REGISTRY)
