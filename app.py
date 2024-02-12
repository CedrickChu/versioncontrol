input_file = 'input.txt'
output_file = 'output.txt'

try:
    with open(input_file, 'r') as f_in:
        content = f_in.read()
        print(f"Read file: {content}")
except IOError as e:
    print(f"Input file I/O error({e.errno}): {e.strerror}")
except Exception as e:
    print(f"Unexpected error: {e}")

try:
    with open(output_file, 'w') as f_out:
        output_text = input('Enter your text: ')
        f_out.write(output_text)
        print(f"text has been written to {output_file}")
except IOError as e:
    print(f"Output file I/O error({e.errno}): {e.strerror}")
except Exception as e:
    print(f"Unexpected error: {e}")