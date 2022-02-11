# vtt2clean_srt
Clean and convert vtt to srt

The cleaning vtt duplicate part is based on [Terence Eden's snippet](https://shkspr.mobi/blog/2018/09/convert-webvtt-to-a-transcript-using-python/).

Then, it simply convert vtt to srt and print to stdout.

If the result looks good, then you could save it via pipe.

vtt形式のキャプションファイルを、重複するテキストを除いた上でsrt形式に変換してTerminalに出力します。
ファイルに保存するには > でファイルへとpipeして下さい。

## Example 

```
WEBVTT
Kind: captions
Language: en

00:00:00.560 --> 00:00:02.310 align:start position:0%
 
it's<00:00:00.799><c> always</c><00:00:01.120><c> more</c><00:00:01.360><c> challenging</c><00:00:01.839><c> to</c><00:00:02.000><c> hit</c><00:00:02.159><c> a</c>

00:00:02.310 --> 00:00:02.320 align:start position:0%
it's always more challenging to hit a
 

00:00:02.320 --> 00:00:05.110 align:start position:0%
it's always more challenging to hit a
moving<00:00:02.800><c> target</c><00:00:03.360><c> especially</c><00:00:03.919><c> in</c><00:00:04.080><c> science</c><00:00:04.960><c> by</c>

00:00:05.110 --> 00:00:05.120 align:start position:0%
moving target especially in science by
```

will become

```
1
00:00:00,560 --> 00:00:02,310
it's always more challenging to hit a

2
00:00:02,320 --> 00:00:05,110
moving target especially in science by
```
🕺🏼🕺🏼🕺🏼Yeah!


# Install

Use Python3.x

There is one dependency to install:

    pip install webvtt-py

then git clone or just download the py file.

# Usage

The first arg is the vtt file name.
The second arg (optional) is a flag to choose srt output (0) 
or text only text file (1).

To convert vtt to srt and print to the terminal:

    python vtt2srt.py TheEarthDisaster.vtt

To save it, just send the standard out to a file like via pipe:

    python vtt2srt.py TheEarthDisaster.vtt > TheEarthDisaster.srt

To extract only the text parts

    python vtt2srt.py TheEarthDisaster.vtt 1 > TheEarthDisaster.text
