try:
    with open("sample.txt",'rt') as file:
        i=1
        print('Reading file content:')
        for t in file:
            print(f'Line {i}:',t.strip('\n'))
            i=i+1
        #bwlow is other solution fro same problem statement.
        # while True:
            # line = file.readline()
            # if not line:
            #     break
            # else:
            #     print(f'Line {i}:{line}')
            #     i+=1
except FileNotFoundError:
    print('Error: The File \'sample.txt\' was not found.')







