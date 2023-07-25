import subprocess
from glob import glob
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="input file names")
    parser.add_argument("-o", "--output", required=True, help="output file name")
    args = parser.parse_args()

    print("Input files")
    input_files = glob(args.input)
    print(input_files)
    cmd = f'cflow {args.input}'
    print(f"Executing command {cmd}")

    cflow_out = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    called_functions = cflow_out.stdout.split('\n')
    called_functions = called_functions[:-1]
    max_calls = 0

    sequences = []
    pairs = []
    for func in called_functions:
        strip_func = func.lstrip()
        call_len = ((len(func) - len(strip_func)) // 4) + 97
        if len(sequences) == 0 or call_len > sequences[-1]:
            sequences.append(call_len)
        func_name, data = strip_func.split('()',1)
        func_name = func_name + '()'
        if data == '':
            file = 'UNKNOWN'
            implement = func_name
            line_number = 'UNKNOWN'
            path = 'UNKNOWN'
        else:
            implement, data = data.split(' at ')
            implement = implement[2:]
            data1, data2 = data.split('>')
            file, line_number = data1.split(':')
            path, file = file.rsplit('/', 1)
            comment = data2.strip().replace(':', '')
        pairs.append([call_len, f'{func_name}\\n{file}:{line_number}'])

    sequences = list(map(chr,sequences))
    out_data = [','.join(sequences)]

    for seq, func in pairs:
        out_data.append(f'{chr(seq)}->{chr(seq+1)}:{func}')

    out_data = ';\n'.join(out_data) + ';'

    with open(args.output + '.signalling', 'w') as f:
        f.write(out_data)


if __name__ == "__main__":
    main()
