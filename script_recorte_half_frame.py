import subprocess
import pandas as pd


df = pd.read_excel('info_exif.xlsx')

path = ''

df.drop(df[df.Recortar!='S'].index, inplace=True)

for i in df.index:
	file = df['File'][i]
	file_path = f'{path}{file}'
	command = ["convert",
	file_path,
	"-crop",
	f"50%x100%",
	f"+repage",
	f"{file_path[:-4]}_crop_%d.jpg"]
	#subprocess.run(command)
	subfolder = file[:8]
	command2 = ["mv",file_path,f"{path}{subfolder}Original/"]
	#subprocess.run(command2)