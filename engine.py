import os
import json
from tools import TOOL_REGISTRY

class ToolExecutor:
    """
    Executes tools from a registry and keeps track of execution history.

    Args:
        history_file (str): Path to the JSON file used to store execution history.

    Returns:
        None
    """
    def __init__(self,history_file="history.json"):
        """
        Initializes the ToolExecutor and loads history from file if it exists.

        Args:
            history_file (str): Path to the history JSON file.

        Returns:
            None
        """
        self.history_file=history_file
        self.history_list=[]

        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as f:
                self.history_list=json.load(f)
    
    def save_history(self,action_name:str,result:str,**kwargs):
        """
        Saves an execution record including action name, arguments, and result.

        Args:
            action_name (str): Name of the executed action.
            result (str): Output returned by the executed function.
            **kwargs: Arguments passed to the function.

        Returns:
            None
        """
        entry={
            "action":action_name,
            "arguments":kwargs,
            "result":result
        }

        self.history_list.append(entry)

        with open(self.history_file,'w') as f:
            json.dump(self.history_list,f,indent=4)

    def execute(self,action_name:str,**kwargs):
        """
        Executes a tool from the TOOL_REGISTRY and records the result.

        Args:
            action_name (str): Name of the tool to execute.
            **kwargs: Arguments to pass to the tool.

        Returns:
            str: Output of the tool execution or an error message if the action is invalid.
        """
        if action_name in TOOL_REGISTRY:
            func=TOOL_REGISTRY[action_name]['executable']
            output=func(**kwargs)
            self.save_history(action_name,output,**kwargs)
            return output
            
        else:
            return f"Error: '{action_name}' is not a valid action."




if __name__=='__main__':
    engine=ToolExecutor()
    # 2. Test Tool 1 (Requires 1 argument)
    print(engine.execute("get_weather", city="Mangaluru"))
    
    # 3. Test Tool 2 (Requires 2 arguments)
    print(engine.execute("save_report", filename="engine_test.txt", content="Engine is live."))
    
    # 4. Test a Fake Tool
    print(engine.execute("hack_nasa"))
