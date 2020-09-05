# Splitter

A bash script that uses **ffmpeg** to split a full album or a remix to seperate files(songs) based on the input timestamps

## How to use
- create a list of timestamps 
- run ``` ./splitter long_file.mp3 timestamps_list ```

### Timestamp list must have this exact format
` Timestamp Title-Artist ` (**Title and Artist must not have spaces**)
> Example
``` 
00:00:00 Drive-Luca_Giacco
00:03:29 The_Lady_In_Red-The_Cooltrane_Quartet
```
> You can use **youtube-dl** to download something like [this](https://youtu.be/SpQ25QwIlFU) and then run the script 
