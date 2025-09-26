import os

def build(main_class, modules_path, module_dir, is_build_path):

    build_sources = main_class.build_sources

    for input_file_name in build_sources:
        output_file_name = build_sources[input_file_name]

        # Paths relative to the module directory
        module_input_file = os.path.normpath(f"{module_dir}/{input_file_name}")
        module_output_file = os.path.normpath(f"{module_dir}/{output_file_name}")

        # Absolute Paths
        full_path_input_file = f"{modules_path}/{module_input_file}"
        full_path_output_file = f"{modules_path}/{module_output_file}"

        # Build with GCC
        print(f"[*] Compilation: {module_input_file}")

        response_code = os.system(f"gcc -w -o {full_path_output_file} {full_path_input_file}")

        if response_code == 0:
            print(f"[v] Success: {module_output_file}")
        else:
            print(f"[x] Fail: {module_output_file}")

    # Create a flag file to indicate that the module's dependencies have been collected
    with open(is_build_path, "w") as f:
        pass
