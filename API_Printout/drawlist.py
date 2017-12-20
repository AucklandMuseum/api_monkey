from PIL import Image, ImageDraw, ImageFont
import math, json, sys

count = 0
maxTextWidth = 250

font = ImageFont.truetype('/usr/share/fonts/truetype/arial.ttf', 10)

height = 20000 + 9
width = maxTextWidth * 40

print(height,width)

canvas = Image.new('RGBA', (width,height), (255,255,255,255))
draw = ImageDraw.Draw(canvas)

currentCol = 0
currentHeight = 0
titlesPerCol = 0

for line in open('all.txt'):
	line = line.strip()
	if line == '':
		continue

	#if it is less then 95 chars then it is likely not longer than 500px
	if len(line) <= 95:
		fontWidth, fontHeight = 500, 10
	else:
		fontWidth, fontHeight = font.getsize(line)

	if fontWidth > maxTextWidth:
		newLine = line
		while fontWidth > maxTextWidth:
			newLine = newLine[:-2]			
			fontWidth, fontHeight = font.getsize(newLine + '...')

		if newLine != line:
			line = newLine+'...'

	#force 10 px
	fontHeight = 10

	draw.text((currentCol, currentHeight), text=line, font=font, fill=(0, 0, 0,200))

	titlesPerCol = titlesPerCol + 1
	currentHeight = currentHeight + fontHeight

	if (currentHeight + 10 >height):
		currentHeight = 0
		currentCol = currentCol + maxTextWidth
		print("Fit",titlesPerCol,"lines into this col #", currentCol/maxTextWidth )
		titlesPerCol = 0
		
	count += 1
	#print(count, end="\r")

print("writing out file")
canvas.save('allNew.png', "PNG")
print(count, " total")
