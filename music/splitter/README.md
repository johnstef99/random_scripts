# Splitter

A bash script that uses **ffmpeg** to split a full album or a remix to seperate files(songs) based on the input timestamps

## How to use
- create a list of timestamps
- run ``` ./splitter long_file.mp3 timestamps_list ```

### Timestamp list must have this exact format
` Timestamp-Artist-Title `
> Example
```
00:00:00-Luca Giacco-Drive
00:03:29-The Cooltrane Quartet-The Lady In Red
```
> You can use **youtube-dl** to download something like [this](https://youtu.be/SpQ25QwIlFU) and then run the script
