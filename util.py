import os
os.getcwd()
collection = "unprocessed"
for i, filename in enumerate(os.listdir(collection)):
    os.rename("unprocessed/" + filename, "unprocessed/" + str(i) + ".png")

# copied from stackoverflow bc i didnt want to deal with os
# https://stackoverflow.com/a/47105286