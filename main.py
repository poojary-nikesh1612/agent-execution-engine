from engine import ToolExecutor

engine=ToolExecutor()

while True:
    user_input=input("System Ready>")

    if user_input.lower()=='exit':
        print("System shutdowning...")
        break

    input_list=user_input.split()

    action_name=input_list[0]
    arguments={}

    for item in input_list[1:]:
        key,value=item.split('=')
        arguments[key]=value
    
    print(engine.execute(action_name,**arguments))