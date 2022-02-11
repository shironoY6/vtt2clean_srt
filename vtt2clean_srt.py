import sys

import webvtt


'''
Convert vtt to clean srt with no duplicated lines.

based off Terence Eden's snippet at:
https://shkspr.mobi/blog/2018/09/convert-webvtt-to-a-transcript-using-python/

(Install)
Use Python3.
There is one dependency:

    pip install webvtt-py

(Usage)
The first arg is the vtt file name.
The second arg (optional) is a flag to choose srt output (0) 
or text only text file (1).

To convert vtt to srt and print to the terminal:

   python vtt2srt.py TheEarthDisaster.vtt

To save it, just send the standard out to a file like via pipe:

   python vtt2srt.py TheEarthDisaster.vtt > TheEarthDisaster.srt

To extract only the text parts

   python vtt2srt.py TheEarthDisaster.vtt 1 > TheEarthDisaster.text

'''


if __name__ == '__main__':

    # setting up parameters
    vtt_file = sys.argv[1]   # vtt file to convert
    only_text = 0 if len(sys.argv) < 3 else sys.argv[2]  # 0 or 1

    # read vtt
    vtt = webvtt.read(vtt_file)

    transcript = ""  # for text only ouput
    lines = []
    for n,line in enumerate(vtt):
        lines.extend(
            [(n,l) for l in line.text.strip().splitlines()]
            )

    previous = ''
    srt_segment = 0
    start_line = []
    for n,line in lines:
        if line == previous:
           continue
        transcript += " " + line
        previous = line
        srt_segment += 1

        if not only_text:
            start_ = vtt[n].start.replace('.', ',')
            end_ = vtt[n].end.replace('.', ',')
            print(f'{srt_segment}\n{start_} --> {end_}\n{line}\n')

    if only_text:
        print(transcript)
