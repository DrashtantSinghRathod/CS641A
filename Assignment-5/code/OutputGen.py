#ciphertext generation
import pexpect

def execute_remote_commands():
    # Spawn a new SSH session to the remote system
    editor = pexpect.spawn('ssh student@172.27.26.188')
    # Wait for the password prompt and enter the password
    editor.expect('student@172.27.26.188\'s password:')
    editor.sendline('cs641')
    # Wait for the group name prompt and enter the group name and password
    editor.expect('Enter your group name: ')
    editor.sendline('crypt_on_ela')
    editor.expect('Enter password: ')
    editor.sendline('straightAs')
    # Wait for the level selection prompt and select level 5
    editor.expect('\r\n\r\n\r\nYou have solved 5 levels so far.\r\nLevel you want to start at: ', timeout=1)
    editor.sendline('5')
    # Perform a series of actions by sending commands and waiting for responses
    editor.expect('.*')
    editor.sendline('go')
    editor.expect('.*')
    editor.sendline('wave')
    editor.expect('.*')
    editor.sendline('dive')
    editor.expect('.*')
    editor.sendline('go')
    editor.expect('.*')
    editor.sendline('read')
    # Open the inputs and outputs files
    inputs_file = open('input.txt', 'r')
    outputs_file = open('outputs.txt', 'w')
    # Loop over each line in the inputs file
    for line in inputs_file:
        # Split the line into individual inputs
        inputs = line.strip().split(' ')
        # Loop over each input and send it to the remote system
        for inp in inputs:
            editor.sendline(inp)
            
            print(editor.before)
            
            # Wait for the response and extract the output
            editor.expect('The text in the screen vanishes!')
            output = editor.before[48:64]
            # Write the output to the outputs file
            outputs_file.write(output + ' ')
        outputs_file.write('\n')
    # Close the files and the SSH session
    inputs_file.close()
    outputs_file.close()
    editor.close()

execute_remote_commands()