from PIL import Image, ImageDraw, ImageFont

image = Image.open(r"C:\Users\swami\Downloads\IMG-20181128-WA0001.png")
font_name = ImageFont.truetype('GreatVibes-Regular.ttf',80)
font_others = ImageFont.truetype('calibri.ttf',21)
draw = ImageDraw.Draw(image)
draw.text(xy=(169,415),text="Sample Name",fill=(0,0,0),font=font_name)
draw.text(xy=(75,510),text="for his cotribution of 400+ hours on open source projects in Java, Spring Boot",fill=(0,0,0),font=font_others)
draw.text(xy=(320,720),text="TalentAccurate - 21 September 2018 - id: 10xZtTX",fill=(0,0,0),font=font_others)

image.save(r"C:\Users\swami\Desktop\certificate.png")

image.show()
