import os

dest = [
    "C:\ProgramData\Docker",
    "C:\ProgramData\DockerDesktop",
    "C:\Program Files\Docker",
]

for idx, folder in enumerate(os.listdir("H:\_alt_ProgramFiles\Docker")):
    print(f'mklink /j {dest[idx]} "H:\_alt_ProgramFiles\Docker\\{folder}"')
