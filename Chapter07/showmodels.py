def print_models(unprinted_designs,completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移动到列表completed_models
    """
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print("Printeing model: "+current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for  completed_model in completed_models:
        print(completed_model)

unprinted_designs=['iphone cse','robot pendant','dodecahedron']
completed_designs=[]
print_models(unprinted_designs[:],completed_designs)
show_completed_models(completed_designs)
print(unprinted_designs)