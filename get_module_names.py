def get_module_names(requiremnt_file_path: str) -> list[str]:
    module_names = []
    with open(requiremnt_file_path, mode='r') as file:
        modules = file.readlines()
        for module in modules:
            name, _ = module.split('==')
            if 'cuda' in name:
                continue
            module_names.append(name)
    return module_names


module_names = get_module_names('requirements.txt')

with open('requiremnet_new.txt', mode='w') as file:
    file.write('\n'.join(module_names))
