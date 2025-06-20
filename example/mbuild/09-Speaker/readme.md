# MakeBlock Speaker Module

The MakeBlock Speaker Module is a versatile component designed to bring sound to your MakeBlock projects. It offers two primary functionalities:

  * **Playing Preset Sounds:** The module comes pre-loaded with a variety of sounds, allowing for quick and easy integration of audio cues into your creations without needing to upload custom files.
  * **Playing Sounds from Speaker Storage:** For more customized applications, the speaker also supports playing sounds that you've stored directly on its internal memory. This feature enables you to incorporate unique audio effects, voice recordings, or music into your projects.

-----

## Module Parameters

  * **Dimensions:** 24 × 36 mm
  * **Total Memory Size:** 16MB
  * **Supported Audio Format:** MP3
  * **Connector Type:** Micro-USB
  * **Rated Operating Current:** 400 mA

-----

## Store User-Defined Audio Files

1.  **Connect the module to a PC.**
    Connect the speaker module to your PC using a Micro USB cable. Use the Micro USB port on the module and a standard USB port on your PC. After a successful connection, your PC will display the module's disk. You can then open the disk to view the files stored on it.

2.  **Store an audio file.**
    Drag the audio file you want the speaker to play onto the module's disk. The disk space of the module is limited, so large files may fail to store. It is recommended that you compress large files before storing them on the disk.

3.  **Change the file name (*important step*).**
    Due to hardware design, the speaker module can only identify an audio file by the first four characters (English letters, numbers, or punctuation marks) of its file name. To play an audio file, you need to change the file name to this special format: a 4-character combination of English letters, numbers, or punctuation marks.

    The table below provides examples to help you rename files. The names on the left are the original ones, and those on the right are the names after the change.

    | Original File Name | 4-Digit File Name |
    |---|---|
    | example.mp3 | exam.mp3 |
    | happy birth day.mp3 | hbd1.mp3 |
    | sound effect1.mp3 | sfx1.mp3 |

    After renaming the audio files, you can play them using the corresponding blocks or code on mBlock 5.

-----

## Play Sound Using Python

To play an audio file in the module's storage, use the following methods:

```python
# Replace "0001" with your actual 4-digit file name in your storage module
mbuild.speaker.play_melody("0001", 1)
```

```python
# Replace "0001" with your actual 4-digit file name in your storage module
mbuild.speaker.play_melody_until_done('0001', 1)
```

**Note:** You need to remove the USB cable from the speaker module before playing the audio file.

-----

## Restore the Speaker's Default Audio Files

Misoperations may damage the preset sound library, causing the preset sounds to fail. Below is the latest compressed package of the default sound files. You can download and decompress it onto the speaker's disk to replace the damaged files. Follow these steps:

1.  Connect the speaker to the computer with a USB cable (the speaker will be recognized as a USB drive).
2.  Format the USB drive.
3.  Download and decompress the [preset sounds](https://www.google.com/search?q=) package, then copy all its audio files to the USB root directory.
4.  Select 'Safely eject USB drive' and then unplug the speaker module from the computer.
