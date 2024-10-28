def insertMarkerToConfirmTheBuildsValidity(file_path, line_identifier, insert_str, append_str):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Flag to check if the identifier is found
        identifier_found = False

        # Open the file in write mode
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line)
                
                # Check if the current line contains the line identifier
                if line_identifier in line and not identifier_found:
                    file.write(insert_str + '\n')
                    identifier_found = True
            
            # After writing all lines, append the append_str to the end of the file
            file.write('\n' + append_str + '\n')
        
        print(f"File '{file_path}' modified successfully.")

    except Exception as e:
        print(f'An error occurred: {e}')

# Usage example:
if __name__ == '__main__':
    modName = 'zm_test1'
    message = f'{modName} built successfully!'

    append_str = f"""post() {{  // Phils-Hub - Stock-Map Script-Placer v1.1.0
    flag_wait("all_players_connected");
    wait 1;
    iPrintLn( "{message}" );
}}"""

    wawRootDir = r'C:\Users\Phil-\Documents\MEGA\__Workbase__\Phils-Hub\Github\cod_waw.stock_map.script_placer\Tests\nazi_zombie_factory.gsc'  # test file
    insertMarkerToConfirmTheBuildsValidity(
        file_path=rf'{wawRootDir}nazi_zombie_factory.gsc',
        line_identifier=r'maps\_zombiemode::main(',
        insert_str='\n	thread post();  // Phils-Hub - Stock-Map Script-Placer v1.1.0',
        append_str=append_str
    )
