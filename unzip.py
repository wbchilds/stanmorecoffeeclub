# python unzip

import libarchive

with libarchive.file_reader('sample_submission.csv.zip') as e:
    for entry in e:
        with open('/tmp/' + str(entry), 'wb') as f:
            for block in entry.get_blocks():
                f.write(block)