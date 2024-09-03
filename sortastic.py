import os
# import configparser

# config_path = "config.ini"
# config = configparser.ConfigParser()

# settings = {}
# for section in config.sections():
#     settings[section] = {}
#     for key, value in config[section].items():
#         settings[section][key] = value

directoryPath = "C:\\Users\\Denim Admin\\Downloads"
directoryContents = os.listdir(directoryPath)

extensionDirectories = {
    'xlsx': directoryPath+'\\Spreadsheets',
    'pptx': directoryPath+'\\Presentation',
    # 'exe': directoryPath+'\\exe',
    'json': directoryPath+'\\_',
    'vsix': directoryPath+'\\_',
    'dat': directoryPath+'\\_',
}

textFileDirectory = directoryPath+'\\Documents'
textFileFormats = [
    "docx", "txt", "rtf", "pdf", "odt", 
    "html", "epub", "md", "tex", "doc"
]

archivesDirectory = directoryPath+'\\Archives'
archiveFormats = [
    "zip", "rar", "7z", "tar", "cab", "arj", "lha"
]

imageDirectory = directoryPath+'\\Images'
imageFormats = [
    "jpg", "jpeg", "png", "gif", "bmp", "tiff",
    "svg", "eps", "ai", "psd", "heic", "webp",
    "jfif"
]

extensionDirectories = {
    **extensionDirectories, 
    **dict(zip(imageFormats, [imageDirectory]*len(imageFormats))),
    **dict(zip(textFileFormats, [textFileDirectory]*len(textFileFormats))),
    **dict(zip(archiveFormats, [archivesDirectory]*len(archiveFormats))),
}

extNotFound = []
for i in range(len(directoryContents)):
    item = directoryContents[i]
    ext = item.split(".")[-1]
    if os.path.isfile(os.path.join(directoryPath, item)) and ext in extensionDirectories.keys():
        # print(directoryContents[i],extensionDirectories[ext])
        pass
    elif os.path.isfile(os.path.join(directoryPath, item)):
        # print("Extension not found", ext)
        if ext not in extNotFound:
            extNotFound.append(ext)

print(extNotFound)
