import glob, os

#Define root directory
os.chdir("/path")

#Filter .mp3 files from the folder
for file in glob.glob("*.mp3"):

  #print (file)
  if "(320 kbps)" in file:
    file = os.rename(file, file.replace("(320 kbps)", ""))
    #Casting because the os.rename command generates a file with extension none
    file = str(file)

  if "(Official Lyric Video)" in file:
    file = os.rename(file, file.replace("(Official Lyric Video)", ""))
    file = str(file)

  if "(Official Video)" in file:
    file = os.rename(file, file.replace("(Official Video)", ""))
    file = str(file)

  if "(Official HD Video)" in file:
    file = os.rename(file, file.replace("(Official HD Video)", ""))
    file = str(file)

  if "(Official Music Video)" in file:
    file = os.rename(file, file.replace("(Official Music Video)", ""))
    file = str(file)

  if "[Official Music Video]" in file:
    file = os.rename(file, file.replace("[Official Music Video]", ""))
    file = str(file)

  if "(Audio)" in file:
    file = os.rename(file, file.replace("(Audio)", ""))
    file = str(file)