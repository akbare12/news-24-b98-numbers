import os
from PIL import Image, ImageDraw, ImageFont
W,H=1024,1024
OUT=os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR','out'),'entry.png')
def F(s,b=False,ser=False):
    p='/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf' if ser else ('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if b else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
    try: return ImageFont.truetype(p,s)
    except Exception: return ImageFont.load_default()
def wrap(t,f,w):
    ls=[];cur=''
    for wd in t.split():
        s=(cur+' '+wd).strip()
        if f.getlength(s)<=w or not cur: cur=s
        else: ls.append(cur);cur=wd
    if cur: ls.append(cur)
    return ls
def block(d,x,y,ls,f,fill,ld):
    for i,l in enumerate(ls): d.text((x,y+i*ld),l,font=f,fill=fill)
def chip(d,x,y,s,c):
    f=F(8,True);w=f.getlength(s)+10;d.rounded_rectangle([x,y,x+w,y+12],radius=3,fill=c);d.text((x+5,y+1),s,font=f,fill='white');return w
RED='#b3392e';NAVY='#1f3557';INK='#111111';PAPER='#f7f2e7';GREY='#5a5a5a';GREEN='#2e7d32';BLUE='#1f5fa8';REP='#5a6b7d'
HEROES=[('1 RIYADH · MIDDLE EAST','CONFIRMED',GREEN,"Houthi drone hits Riyadh's tallest tower again, 11 hurt","A Houthi drone hits the PIF tower, the tallest in Riyadh, for the second time in a week and hurts 11 people.",'Saudi officials','tower','11'),('2 SHANGHAI · ASIA','OFFICIAL',BLUE,"China probes Shanghai party chief Chen Jining","Shanghai party chief Chen Jining, 62, is probed for serious violations as the fourth Politburo member to fall.",'CCDI','gate','62'),('3 NEW YORK · US / TECH','CONFIRMED',GREEN,"Huawei guilty on 10 of 12 counts","A US jury finds Huawei guilty on 10 of 12 counts, including trade-secret theft and bank fraud.",'US court','court','10/12')]
CARDS=[('4 ZAPORIZHZHIA · EUROPE','REPORTED',REP,"Russian attacks kill 9 across Ukraine in a day","Russia kills 9 and wounds 81 in a day as 96 drones fly and 73 are downed.",'Ukrainian officials','drone'),('5 CAS · AFRICA / SPORT','OFFICIAL',BLUE,"CAS hands Senegal back the AFCON title","CAS restores the AFCON title to Senegal after Morocco forfeit 3-0.",'CAS','trophy'),('6 HORMUZ · MIDDLE EAST','REPORTED',REP,"IRGC attacks container ship in Hormuz","IRGC attacks a container ship in Hormuz and cuts its navigation.",'UKMTO','ship'),('7 NEW YORK · MARKETS','CONFIRMED',GREEN,"Dow closes above 50,000 for the first time","Dow closes at 50,018, above 50,000 for the first time, as Taiex jumps 8.99%.",'NYSE','chart'),('8 REDMOND · TECH','REPORTED',REP,"Microsoft declares Code Red after historic outage","Microsoft declares Code Red after a historic 24-hour outage and targets a 1-hour recovery.",'Reuters','server'),('9 ESKISEHIR · EUROPE','REPORTED',REP,"Turkish military helicopter crash kills 5","A Turkish military helicopter crashes in Eskisehir and kills 5.",'Turkish officials','heli'),('10 CARTAGENA · AMERICAS','REPORTED',REP,"Supermarket hostages: 25 held in Cartagena","Gunmen hold 25 hostages in a Cartagena supermarket and free 5 elderly women.",'Colombian officials','shop'),('11 ADEN · MIDDLE EAST','REPORTED',REP,"Houthis advance within 60 km of Aden","Houthi forces advance to within 60 km of Aden in Yemen.",'Wires','arrow'),('12 LAHJ · MIDDLE EAST','REPORTED',REP,"Saudi strikes kill 25, wound 6 in Yemen","Saudi strikes in Lahj kill 25 and wound 6 in Yemen.",'Yemeni officials','strike'),('13 JIUQUAN · SPACE','OFFICIAL',BLUE,"China names first foreign astronaut for Tiangong","China names Tang Hongbo, Wu Yi and Muhammad Zeeshan Ali, the first foreign astronaut on Tiangong.",'CMSA','rocket')]
ALSO=["14 Ankara: Haftar visits Turkey for the first time. [REPORTED]","15 London: UK sanctions Houthis + 4 officials. [OFFICIAL]","16 Villavicencio: Car bomb injures 23. [REPORTED]","17 Gaza: Israel kills Hamas security chief + 6. [REPORTED]","18 Baghdad: Iraq takes federal control of Kurdish oilfields. [OFFICIAL]","19 Gaza: Meningitis alert, 272 cases in October. [OFFICIAL]","20 DR Congo: Cessna 208 missing, rebels claim shootdown. [CLAIM]","21 Hanoi: Hot-pot blast kills 6+, injures 10+. [REPORTED]","22 Gulf of Finland: Ukraine hits Russian ship Sparta II. [REPORTED]","23 Kuala Lumpur: Malaysia to return migrants to Myanmar. [OFFICIAL]","24 Ulleungdo: S. Korea shelter order as Russian jets enter ADIZ. [OFFICIAL]","25 Dhaka: Hasina plans return on 16 Dec. [REPORTED]","26 The Hague: 14 nations back ICJ Myanmar ruling 9-6. [REPORTED]","27 Jakarta: Indonesia nominates 2 VP candidates. [OFFICIAL]","28 Beijing: China sentences official Ma to death for spying. [OFFICIAL]","29 Brussels: NATO vows defence against space threat. [OFFICIAL]","30 Mexico City: US drone aided weekend capture of El Chapo Isidro. [REPORTED]","31 San Salvador: Bukele names 3 soldiers killed in Haiti. [OFFICIAL]","32 Ottawa: Pentagon says only 41.9% of air fleet ready. [REPORTED]","33 Washington: US adds Megaspeed to trade blacklist. [OFFICIAL]","34 Kyiv: Zelensky urges Ukraine-Russia-US-Europe talks soon. [REPORTED]","35 Ras Al Khaimah: Bus-truck crash kills 13. [REPORTED]","36 London: England record 5,258 heat deaths in summer 2026. [OFFICIAL]","37 Kourou: Ariane 6 lofts 36 Amazon satellites. [OFFICIAL]","38 Cikande: Factory-fire toll rises to 26. [REPORTED]"]
NUMBERS=[('11','hurt in Riyadh'),('9','killed in Ukraine'),('50,018','Dow closes'),('+8.99%','Taiex record'),('25','killed in Yemen'),('26','Cikande toll'),('10/12','Huawei counts'),('96','drones at Ukraine')]
UTC="02:15 NATO vows space defence · 08:16 Hanoi blast · 10:42 Saudi strikes Yemen · 14:27 Riyadh tower hit · 16:51 Houthis 60 km from Aden · 18:58 Hormuz ship attack · 20:41 Huawei guilty"
NA=[(-168,66),(-150,70),(-135,69),(-125,71),(-115,68),(-105,68),(-95,69),(-85,66),(-80,73),(-70,62),(-60,55),(-55,47),(-60,44),(-65,44),(-70,42),(-74,39),(-76,35),(-80,32),(-81,26),(-84,30),(-90,29),(-95,29),(-97,26),(-94,19),(-90,21),(-86,16),(-83,15),(-90,14),(-95,16),(-100,18),(-105,20),(-110,24),(-115,29),(-120,34),(-124,40),(-124,48),(-130,54),(-140,60),(-150,59),(-158,58),(-165,60)]
SA=[(-80,9),(-77,4),(-80,-3),(-81,-6),(-77,-12),(-72,-18),(-70,-23),(-70,-30),(-72,-37),(-73,-44),(-70,-50),(-66,-55),(-68,-52),(-62,-45),(-57,-38),(-52,-32),(-48,-28),(-41,-23),(-35,-9),(-35,-6),(-43,-3),(-50,0),(-55,5),(-60,8),(-68,11),(-75,10)]
EU=[(-10,36),(-9,43),(-2,48),(-5,50),(0,51),(3,53),(8,57),(10,59),(18,56),(21,55),(24,59),(30,60),(30,65),(25,70),(18,69),(12,65),(5,60),(5,58),(8,55),(10,54),(5,53),(0,50),(-2,49),(-5,48),(-2,43),(-1,38),(-6,36)]
AF=[(-6,35),(0,36),(10,37),(11,34),(20,32),(32,31),(34,28),(35,23),(37,18),(39,15),(43,12),(48,11),(51,10),(46,5),(41,0),(40,-5),(40,-12),(36,-18),(33,-26),(28,-33),(20,-35),(17,-32),(15,-27),(12,-18),(13,-12),(12,-6),(9,4),(4,6),(-8,5),(-13,8),(-17,15),(-17,20),(-15,25),(-10,30)]
AS=[(30,65),(40,68),(55,68),(70,72),(85,74),(100,76),(115,76),(130,72),(145,72),(160,70),(170,66),(178,65),(170,60),(162,58),(158,52),(150,59),(142,55),(140,50),(135,45),(130,42),(127,40),(122,38),(120,32),(122,28),(118,25),(110,20),(108,12),(105,8),(100,8),(98,12),(95,16),(92,21),(90,22),(86,20),(80,15),(77,8),(75,12),(72,20),(68,23),(62,25),(58,26),(56,27),(52,28),(50,29),(48,30),(44,29),(42,27),(40,22),(39,21),(43,17),(45,13),(48,14),(52,16),(56,22),(58,25),(60,25),(60,30),(55,35),(48,38),(42,42),(38,45),(35,48),(30,55)]
AU=[(114,-22),(114,-30),(115,-35),(120,-34),(125,-32),(130,-32),(135,-35),(140,-38),(145,-38),(150,-37),(153,-32),(153,-27),(150,-22),(146,-19),(142,-15),(142,-11),(137,-12),(135,-15),(132,-12),(130,-13),(126,-14),(122,-17),(118,-20)]
JP=[(130,31),(132,33),(135,34),(137,35),(140,36),(141,39),(142,42),(144,44),(142,45),(140,43),(138,38),(136,36),(133,34)]
CONT=[NA,SA,EU,AF,AS,AU,JP]
PINS=[(1,24.71,46.68,0,0),(2,31.23,121.47,0,0),(3,40.71,-74.01,-10,-8),(4,47.84,35.14,0,0),(5,14.69,-17.44,0,0),(6,26.50,56.00,8,-8),(7,40.71,-74.01,12,10),(8,47.67,-122.12,0,0),(9,39.77,30.52,-10,8),(10,10.39,-75.51,0,0),(11,12.79,45.03,0,0),(12,13.05,44.88,16,10),(13,39.73,98.49,0,0)]
LEGEND=["1 Riyadh — PIF tower hit","2 Shanghai — Chen Jining probed","3 New York — Huawei guilty 10/12","4 Zaporizhzhia — 9 killed","5 Dakar — Senegal regain AFCON title","6 Hormuz — IRGC hits container ship","7 New York — Dow above 50,000","8 Redmond — Microsoft Code Red","9 Eskisehir — helicopter crash kills 5","10 Cartagena — 25 hostages","11 Aden — Houthis 60 km away","12 Lahj — Saudi strikes kill 25","13 Jiuquan — first foreign astronaut named"]
def scene(d,x,y,w,h,k):
    bg={'tower':'#16233d','gate':'#7d1f1f','court':'#3a3a44','drone':'#1c2f4a','trophy':'#1e5c34','ship':'#14425e','chart':'#123f2a','server':'#5c1010','heli':'#4a3b22','shop':'#5e2a4a','arrow':'#6b3a12','strike':'#4a1f1f','rocket':'#0e2a4a'}.get(k,'#223344')
    d.rectangle([x,y,x+w,y+h],fill=bg)
    if k=='tower':
        d.rectangle([x+w*0.44,y+16,x+w*0.60,y+h],fill='#c8a24a');d.rectangle([x+w*0.20,y+34,x+w*0.34,y+h],fill='#2c4a6b');d.rectangle([x+w*0.68,y+30,x+w*0.84,y+h],fill='#2c4a6b')
        for j in range(5): d.rectangle([x+w*0.46,y+22+j*12,x+w*0.58,y+30+j*12],fill='#ffe9a8')
        d.ellipse([x+w*0.60,y+6,x+w*0.72,y+20],fill='#9aa5b1');d.ellipse([x+w*0.66,y+2,x+w*0.80,y+16],fill='#c7cfd6');d.ellipse([x+w*0.12,y+8,x+w*0.20,y+15],fill='#e8e8e8')
    elif k=='gate':
        d.rectangle([x,y+h*0.62,x+w,y+h],fill='#3d0f0f');d.polygon([(x+w*0.15,y+h*0.62),(x+w*0.5,y+h*0.30),(x+w*0.85,y+h*0.62)],fill='#a83226');d.rectangle([x+w*0.38,y+h*0.62,x+w*0.62,y+h],fill='#e8d9b0');d.rectangle([x+w*0.66,y+h*0.55,x+w*0.92,y+h*0.85],fill='#f2ead0');d.line([x+w*0.70,y+h*0.63,x+w*0.88,y+h*0.63],fill=RED,width=2);d.line([x+w*0.70,y+h*0.70,x+w*0.88,y+h*0.70],fill=RED,width=2)
    elif k=='court':
        d.rectangle([x,y+h*0.72,x+w,y+h],fill='#22222a');d.rectangle([x+w*0.08,y+h*0.30,x+w*0.92,y+h*0.40],fill='#d8d2c0');d.polygon([(x+w*0.05,y+h*0.32),(x+w*0.5,y+h*0.08),(x+w*0.95,y+h*0.32)],fill='#b8b09a')
        for j in range(4): d.rectangle([x+w*(0.16+j*0.20),y+h*0.40,x+w*(0.24+j*0.20),y+h*0.72],fill='#e8e2d0')
    elif k=='chart':
        d.rectangle([x,y+h*0.55,x+w,y+h],fill='#0d2f1e');d.line([(x+6,y+h*0.80),(x+w*0.35,y+h*0.62),(x+w*0.55,y+h*0.70),(x+w*0.85,y+h*0.18)],fill='#4ade80',width=3);d.line([(x+6,y+h*0.30),(x+w,y+h*0.30)],fill='#e8b93c',width=2);d.text((x+6,y+4),'50,000',font=F(9,True),fill='#e8b93c')
    elif k=='rocket':
        d.polygon([(x+w*0.5,y+4),(x+w*0.38,y+h*0.55),(x+w*0.62,y+h*0.55)],fill='#e8e8e8');d.polygon([(x+w*0.38,y+h*0.45),(x+w*0.26,y+h*0.70),(x+w*0.38,y+h*0.60)],fill=RED);d.polygon([(x+w*0.62,y+h*0.45),(x+w*0.74,y+h*0.70),(x+w*0.62,y+h*0.60)],fill=RED);d.polygon([(x+w*0.44,y+h*0.55),(x+w*0.5,y+h*0.92),(x+w*0.56,y+h*0.55)],fill='#f5a623');d.ellipse([x+w*0.78,y+6,x+w*0.94,y+20],fill='#e8e8e8')
    elif k=='trophy':
        d.ellipse([x+w*0.32,y+6,x+w*0.68,y+34],fill='#f2c230');d.rectangle([x+w*0.44,y+h*0.55,x+w*0.56,y+h*0.72],fill='#f2c230');d.rectangle([x+w*0.30,y+h*0.72,x+w*0.70,y+h*0.88],fill='#c89a1e');d.ellipse([x+w*0.24,y+8,x+w*0.36,y+22],fill='#f2c230');d.ellipse([x+w*0.64,y+8,x+w*0.76,y+22],fill='#f2c230')
    elif k=='ship':
        d.rectangle([x,y+h*0.62,x+w,y+h],fill='#0a2f47');d.polygon([(x+w*0.08,y+h*0.55),(x+w*0.92,y+h*0.55),(x+w*0.82,y+h*0.82),(x+w*0.18,y+h*0.82)],fill='#5a3a22');d.rectangle([x+w*0.20,y+h*0.28,x+w*0.38,y+h*0.55],fill='#c0392b');d.rectangle([x+w*0.42,y+h*0.28,x+w*0.60,y+h*0.55],fill='#2e86c1');d.rectangle([x+w*0.64,y+h*0.28,x+w*0.82,y+h*0.55],fill='#e8b93c')
    elif k=='server':
        for j in range(3): d.rectangle([x+w*0.14+j*0.28,y+6,x+w*0.36+j*0.28,y+h-6],fill='#2a2a30',outline='#555555')
        for j in range(3):
            for r in range(3): d.ellipse([x+w*(0.18+j*0.28),y+10+r*12,x+w*(0.22+j*0.28),y+14+r*12],fill='#4ade80' if r<2 else RED)
    elif k=='heli':
        d.ellipse([x+w*0.20,y+h*0.30,x+w*0.72,y+h*0.62],fill='#d8c890');d.ellipse([x+w*0.66,y+h*0.34,x+w*0.86,y+h*0.52],fill='#a8c4d8');d.line([(x+w*0.08,y+h*0.26),(x+w*0.92,y+h*0.26)],fill='#222222',width=3);d.line([(x+w*0.72,y+h*0.46),(x+w*0.95,y+h*0.30)],fill='#222222',width=2);d.rectangle([x+w*0.42,y+h*0.62,x+w*0.52,y+h*0.78],fill='#222222')
    elif k=='shop':
        d.rectangle([x,y,x+w,y+h*0.30],fill='#e8e8e8')
        for j in range(5): d.rectangle([x+j*w/5,y,x+(j+1)*w/5,y+h*0.30],fill=RED if j%2==0 else '#f2ead0')
        d.rectangle([x+w*0.30,y+h*0.30,x+w*0.70,y+h*0.85],fill='#3a5a7a');d.text((x+w*0.36,y+h*0.45),'25',font=F(14,True),fill='white')
    elif k=='arrow':
        d.line([(x+8,y+h*0.70),(x+w-8,y+h*0.30)],fill='#f5a623',width=3);d.polygon([(x+w-8,y+h*0.30),(x+w-26,y+h*0.30),(x+w-8,y+h*0.52)],fill='#f5a623');d.ellipse([x+w-22,y+h*0.18,x+w-8,y+h*0.34],fill=RED)
    elif k=='strike':
        for j in range(6): d.line([(x+w*0.5,y+h*0.5),(x+w*(0.15+0.14*j),y+h*0.12 if j%2==0 else y+h*0.88)],fill='#f5a623',width=2)
        d.ellipse([x+w*0.38,y+h*0.30,x+w*0.62,y+h*0.70],fill='#e8b93c')
    elif k=='drone':
        for j in range(3): d.ellipse([x+w*(0.18+j*0.30),y+h*0.18,x+w*(0.28+j*0.30),y+h*0.38],fill='#222222');d.line([(x+w*(0.14+j*0.30),y+h*0.28),(x+w*(0.32+j*0.30),y+h*0.28)],fill='#bbbbbb',width=2)
        d.rectangle([x,y+h*0.62,x+w,y+h],fill='#0f1e33');d.rectangle([x+w*0.15,y+h*0.70,x+w*0.35,y+h],fill='#c8a24a');d.rectangle([x+w*0.60,y+h*0.70,x+w*0.82,y+h],fill='#2c4a6b')
    else: d.ellipse([x+w*0.35,y+h*0.25,x+w*0.65,y+h*0.75],fill='#e8b93c')
img=Image.new('RGB',(W,H),PAPER);d=ImageDraw.Draw(img)
d.text((10,6),'THE WORLD ON ONE DAY',font=F(11,True),fill=RED);rt='38 STORIES · 6 REGIONS · 13 FIELDS';d.text((1014-F(11,True).getlength(rt),6),rt,font=F(11,True),fill=INK)
d.text((10,22),'Tuesday 24 November 2026',font=F(30,True,True),fill=INK);d.text((10,56),'Riyadh tower hit again · Shanghai party chief probed · Huawei guilty on 10 of 12 counts.',font=F(11),fill=RED);d.line([(10,72),(1014,72)],fill=INK,width=2)
REG=[('Europe',9,'#2b4c7e'),('Middle East',8,'#b3392e'),('Asia',8,'#d98e00'),('Africa',2,'#4a7c59'),('Americas',7,'#6a4a8a'),('World/Space',4,'#333333')];rx=10
for nm,n,c in REG:
    sw=1004*n/38;d.rectangle([rx,76,rx+sw,94],fill=c);t=f'{nm} {n}';d.text((rx+sw/2-F(9,True).getlength(t)/2,80),t,font=F(9,True),fill='white');rx+=sw
d.text((10,98),'THE DAY IN UTC',font=F(9,True),fill=RED);block(d,10,110,wrap(UTC,F(9),1004),F(9),INK,12)
d.text((10,134),'THE DAY IN NUMBERS',font=F(9,True),fill=RED);nx=10
for v,lab in NUMBERS:
    d.text((nx,146),v,font=F(20,True),fill=RED);block(d,nx,168,wrap(lab,F(8),120),F(8),GREY,10);nx+=125.5
for i,(kick,chp,col,head,deck,src,kind,giant) in enumerate(HEROES):
    x=10+i*338;w=328;d.rectangle([x,186,x+w,380],outline='#999999');scene(d,x,186,w,96,kind);gf=F(48,True) if len(giant)<=2 else F(32,True);gw=gf.getlength(giant);d.text((x+w-gw-10,200),giant,font=gf,fill='white',stroke_width=2,stroke_fill='#000000')
    d.text((x+8,290),kick,font=F(10,True),fill=NAVY);block(d,x+8,304,wrap(head,F(13,True),w-16),F(13,True),INK,15);block(d,x+8,336,wrap(deck,F(10),w-16),F(10),INK,12);cw=chip(d,x+8,364,chp,col);d.text((x+16+cw,366),'('+src+')',font=F(8),fill=GREY)
for r in range(2):
    for c in range(5):
        it=CARDS[r*5+c];x=10+c*202;w=196;y=388+r*140;d.rectangle([x,y,x+w,y+136],outline='#999999');scene(d,x,y,w,48,it[6]);d.text((x+6,y+52),it[0],font=F(8,True),fill=NAVY);block(d,x+6,y+64,wrap(it[3],F(10,True),w-12),F(10,True),INK,12);block(d,x+6,y+88,wrap(it[4],F(9),w-12),F(9),INK,10);cw=chip(d,x+6,y+122,it[1],it[2]);d.text((x+12+cw,y+124),'('+it[5]+')',font=F(8),fill=GREY)
MX0,MY0,MW,MH=10,686,550,150
def P(lon,lat): return (MX0+(lon+180)/360*MW,MY0+(75-lat)/130*MH)
d.text((10,668),'THE WORLD · 13 STORIES PINNED',font=F(10,True),fill=RED);d.rectangle([MX0,MY0,MX0+MW,MY0+MH],fill='#dceef5',outline='#999999')
for poly in CONT:
    d.polygon([P(lo,la) for lo,la in poly],fill='#cfe0b8',outline='#7a9a6a')
for lo,la in [(95,5),(105,-5),(115,-7),(125,-8),(135,-4),(140,-3)]:
    ex,ey=P(lo,la);d.ellipse([ex-4,ey-2,ex+4,ey+2],fill='#cfe0b8',outline='#7a9a6a')
ex,ey=P(174,-41);d.ellipse([ex-4,ey-8,ex+4,ey+8],fill='#cfe0b8',outline='#7a9a6a')
for n,la,lo,dx,dy in PINS:
    tx,ty=P(lo,la);px,py=tx+dx,ty+dy
    if dx or dy: d.line([(tx,ty),(px,py)],fill=GREY,width=1)
    d.ellipse([px-7,py-7,px+7,py+7],fill=RED,outline='white');t=str(n);d.text((px-F(8,True).getlength(t)/2,py-5),t,font=F(8,True),fill='white')
d.text((575,686),'WHERE THE STORIES ARE',font=F(10,True),fill=RED)
for i,t in enumerate(LEGEND):
    lx=575 if i<7 else 800;ly=702+(i%7)*19;d.text((lx,ly),t,font=F(9),fill=INK)
d.text((10,840),'ALSO ON TUESDAY — 25 MORE STORIES',font=F(11,True),fill=RED)
for i,t in enumerate(ALSO):
    cx=10+(i//9)*338;cy=856+(i%9)*10;d.text((cx,cy),t,font=F(8),fill=INK)
d.rectangle([10,950,1014,984],fill='#fdeceb',outline=RED,width=2);pre='DATE CHECK — ';d.text((16,954),pre,font=F(9,True),fill=RED);d.text((16+F(9,True).getlength(pre),954),'All stories above happened or were first reported on Tuesday 24 November 2026. Wires read up to 23:00 UTC.',font=F(9),fill=INK)
d.text((16,968),'LEFT OUT (not 24 Nov): Hormuz mine claims · Nvidia CEO return · EU sanctions 22 · COP31 no deal · El Chapo arrest Fri 20 Nov · Cikande fire Sat 21 Nov. NOT YET: Shenzhou-24 launch 25 Nov · Huawei sentencing Sep 2027.',font=F(8),fill=INK)
d.text((10,988),'Sources: Saudi officials · CCDI · US court · Ukrainian officials · CAS · UKMTO · NYSE · Reuters · Turkish officials · Colombian officials · Yemeni officials · CMSA · wires.',font=F(8),fill=GREY)
d.text((10,1001),'CONFIRMED = 2+ outlets · OFFICIAL = on record · REPORTED = one outlet · CLAIM = one side\u2019s claim. Scenes are drawn in code, not photographs.',font=F(8),fill=GREY)
os.makedirs(os.path.dirname(OUT) or '.',exist_ok=True);img.save(OUT)
print('saved',OUT,os.path.getsize(OUT))
