# vtt2clean_srt
Clean and convert vtt to srt

The cleaning vtt duplicate part is based on [Terence Eden's snippet](https://shkspr.mobi/blog/2018/09/convert-webvtt-to-a-transcript-using-python/).

Then, it simply convert vtt to srt and print to stdout.

If the result looks good, then you could save it via pipe.

vtt形式のキャプションファイルを、重複するテキストを除いた上でsrt形式に変換してTerminalに出力します。
ファイルに保存するには > でファイルへとpipeして下さい。


(Install)
Use Python3.x

There is one dependency to install:

    pip install webvtt-py

then git clone or just download the py file.

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
