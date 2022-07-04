import os
from PIL import Image
from zipfile import ZipFile

for file in os.listdir():
	if file.endswith(".png") or file.endswith(".bmp"):
		im = Image.open(file)
		head = im.crop((0, 0, 18, 16))
		im = im.crop((0, 16, 18, 32))
		head.save("h"+file)
		im.save(file)
	elif file.endswith(".zip"):
		with ZipFile(file) as archieve:
			adder = 0
			for entry in archieve.infolist():
				with archieve.open(entry) as fp:
					im = Image.open(fp)
					head = im.crop((0, 0, 18, 16))
					im = im.crop((0, 16, 18, 32))
					head.save(f"h{adder}.png")
					im.save(f"{adder}.png")
				adder += 1
		new_zip = ZipFile(file, "w")
		head_zip = ZipFile("h"+file, "w")
		for i in range(adder):
			new_zip.write(f"{i}.png")
			head_zip.write(f"h{i}.png")
			os.remove(f"{i}.png")
			os.remove(f"h{i}.png")
		new_zip.close()
		head_zip.close()
