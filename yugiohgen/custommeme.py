import os, random, string, uuid, textwrap, sys
from PIL import Image, ImageMath, ImageChops, ImageDraw, ImageFont
from facepy import GraphAPI

font=ImageFont.truetype("/var/www/yugiohgen/title.ttf", 45)
font2=ImageFont.truetype("/var/www/yugiohgen/effect.ttf", 13)
font3=ImageFont.truetype("/var/www/yugiohgen/attack.ttf", 21)

colour=(0,0,0,255)
spell=''
trap=''
xyz=''
folderpath="/var/www/yugiohgen"
attackfilepath=folderpath+"/attack"
defencefilepath=folderpath+"/defence"
effectfilepath=folderpath+"/effect"
namefilepath=folderpath+"/name"
templatefilepath=folderpath+"/templates"
memefilepath=folderpath+"/tempinput"
filename=""
attackfile=random.choice(os.listdir(attackfilepath))
with open ((attackfilepath+"/"+attackfile), "r") as myfile:
    attack=myfile.read()
defencefile=random.choice(os.listdir(defencefilepath))
with open ((defencefilepath+"/"+defencefile), "r") as myfile:
    defence=myfile.read()
effectfile=random.choice(os.listdir(effectfilepath))
with open ((effectfilepath+"/"+effectfile), "r") as myfile:
    effect=myfile.read()
namefile=random.choice(os.listdir(namefilepath))
with open ((namefilepath+"/"+namefile), "r") as myfile:
    name=myfile.read()
templatefile=random.choice(os.listdir(templatefilepath))
#PHP PASS HERE
meme1file=(memefilepath+"/"+sys.argv[1])
#PLS
if "spell" in templatefile: 
   spell=1
if "Trap" in templatefile: 
   trap=1
if "X_" in templatefile: 
   xyz=1
template=Image.open(templatefilepath+"/"+templatefile).convert('RGBA') 
new_template=Image.new('RGBA',template.size)
new_template.paste(template, (0,0))
img=Image.open(templatefilepath+"/"+templatefile)
memesize1=314
memesize2=313
meme=Image.open(meme1file).convert('RGBA')
meme=meme.resize((memesize1, memesize2))
memelocation1=52
memelocation2=114
new_template.paste(meme,(memelocation1, memelocation2))
draw=ImageDraw.Draw(new_template)
namelocationx=50
namelocationy=32
if xyz == 1:
    colour=(255,255,255,255)
draw.text((namelocationx,namelocationy),name,fill=colour, font=font)
effectd=ImageDraw.Draw(new_template)
if xyz == 1:
    effectx=39
    effecty=478
if xyz != 1:
    if spell != 1:
        if trap != 1:
            effectx=39
            effecty=476
if spell == 1:
    effectx=39
    effecty=461
if trap == 1:
    effectx=39
    effecty=461
for line in textwrap.wrap(effect, width=55):
    effectd.text((effectx,effecty),line,fill=(0,0,0,255), font=font2)
    effecty += 12
if spell != 1:
    if trap != 1:
        drawatk=ImageDraw.Draw(new_template)
        drawdef=ImageDraw.Draw(new_template)
        if xyz == 1:
            attacklocationx=258
            attacklocationy=555
            defencelocationx=345
            defencelocationy=555
        if xyz != 1:
            attacklocationx=254
            attacklocationy=554
            defencelocationx=341
            defencelocationy=554
        drawatk.text((attacklocationx,attacklocationy),attack,fill=(0,0,0,255), font=font3)
        drawdef.text((defencelocationx,defencelocationy),defence,fill=(0,0,0,255), font=font3)
filenameruiner=str(uuid.uuid4())
filename=filename+filenameruiner
new_template.save(folderpath+"/tempoutput/"+filename+".png")
print("/tempoutput/"+filename + ".png")
