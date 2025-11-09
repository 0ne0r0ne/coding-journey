print(''' Welcome the Bear game! 
   ,,,         ,,,
 ;"   ^;     ;'   ",
;    s$$$$$$$s     ;
,  ss$$$$$$$$$$s  ,'
 ;s$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$
$$$$P""Y$$$Y""W$$$$$
$$$$  p"$$$"q  $$$$$
$$$$  .$$$$$.  $$$$
 $$DcaU$$$$$$$$$$$
  "Y$$$"*"$$$Y"
      "$b.$$"
        """ ''')
tercih_0 = input("Hangi yoldan gitmek istersiniz, sağ mı sol mu? ( Sağ = R, Sol = L) \n")

if tercih_0 == "R":
    print("Ayı pençesi yüzünüze denk geldi öldünüz, oyun biti!")
    exit()
elif tercih_0 == "L":
    print("Ayı sizi görmedi, güvenli bir patikadasınız(!)")
    tercih_1 =  input("Yol ayrımındasınız, göl yolu mu (R), yoksa mağaraya çıkan (L) patika mı? \n")
else:
    print(''' Ayının midesindesiniz, oyun bitti!
 {"`-'"}
  (o o)
,--`Y'--.
`-:,-.;-'
  /`_'\
 (_/ \_) ''')
    exit()

tercih_2 = input ("Güvenli patikada ilerlerken karşınıza ayı sineği çıktı, sizi ısırdı. Kaçtınız ve bir klübenin içine girdiniz, klübede önünüzde iki adet kapı var, sağ kapı mı 'R', sol kapı mı 'L', yoksa beklemeyi mi tercih ettiniz? 'Herhangi bir karaktere basınız 'R' ve 'L' dışında' \n ")

if tercih_2 == "R":
    print("Kış uykusuna yatan ayıyı uyandırınız ve ayı sizi yedi, oyun bitti!")
    exit()
elif tercih_2 == "L":
    print("İçeri girdiniz ve kapı arkanızdan kapandı, strese dayanamayıp kendinizi öldürdünüz, oyun bitti!")
    exit()
else:
    print(''' Yeterince beklediniz ve klübenin sahibi olan avcı geldi, size tüfek verdi ve artık ayılar size saldırmama kararı aldı! Kazandınız, mutlu ve huzurlu son!. 
    _________________________________________________________
    |\=========================================================\
    ||                                                         |
    ||        _        __        ___        __        _        |
    ||       ; `-.__.-'. `-.__.-'. .`-.__.-' .`-.__.-' :       |
    ||     _.'. . . . . . . . .,,,,,,,. . . . . . . . .`._     |
    ||   .'. . . . . . . . ,a@@@@@@@@@@@a, . . . . . . . .`.   |
    ||   `. . . . ,a@@@@@a@@@a@@@@@@@@@a@@@a@@@@@a, . . . ,'   |
    ||     ) . . a@@@@@@a@@@@@a@@@@@@@a@@@@@a@@@@@@a . . (     |
    ||   ,' . . .@@@%%%a@@@@@@@@@@@@@@@@@@@@@a%%%@@@  . . `.   |
    ||   `.. . . @@@%%a@@@@@@""@@@@@@@""@@@@@@a%%@@@ . . .,'   |
    ||     ). . . "@@a@@@@@@@@@SSSSSSS@@@@@@@@@a@@" . . .(     |
    ||   ,'. . . . . `@@@@@@@@SSS, ,SSS@@@@@@@@' . . . . .`.   |
    ||   `. . . . . . `@@@@@@@`SSS:SSS'@@@@@@@' . . . . . ,'   |
    ||     ) . . . . . `@@@@@@@sssssss@@@@@@@' . . . . . (     |
    ||   ,' . . . . . ,a@@a@@@@@@@@@@@@@@@a@@a, . . . . . `.   |
    ||   `.. . . . .a@@@a@@@@@a@@@a@@@a@@@@@a@@@a. . . . .,'   |
    ||     ). . . .a@@@@@a@@@@@@@@@@@@@@@@@a@@@@@a. . . .(     |
    ||   ,'. . . . @@@@@@a@@@@'   "   `@@@@a@@@@@@ . . . .`.   |
    ||   `. . . . .@@@@@@@aaaa,       ,aaaa@@@@@@@  . . . ,'   |
    ||     ) . . . `@@@@@@@@@@@@a, ,a@@@@@@@@@@@@' . . . (     |
    ||   ,' . . . . .`@@@@@@@@@@a@a@a@@@@@@@@@@'. . . . . `.   |
    ||   `;;;;;;;;;;;;aaaaaaaaaa@@@@@aaaaaaaaaa;;;;;;;;;;;;'   |
    ||     );;;;;;;,mMMMMMMMm@@@@@@@@@@@mMMMMMMMm,;;;;;;;(     |
    ||   ,;;;;;;;;a@%#%%#%%#%Mm@@@@@@@mM%#%%#%%#%@a;;;;;;;;,   |
    ||   `;;;;;;;;@@%%%%%%%%%%M@@";"@@M%%%%%%%%%%@@;;;;;;;;'   |
    ||     );;;;;;`@a%%%%%%%%mM";;;;;"Mm%%%%%%%%a@';;;;;;(     |
    ||   ,;;;;;;;;;;"@@@@@@@@";;;;;;;;;"@@@@@@@@";;;;;;;;;;,   |
    ||   `;;;;;;;;;;;;"""""";;;;;;;;;;;;;"""""";;;;;;;;;;;;'   |
    ||     );;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;-Catalyst(     |
    ||     `:;;;:-~~~-:;;:-~~~-:;;;;;:-~~~-:;;:,-~~~-:;;;:'    |
    ||       ~~~       ~~        ~~~        ~~        ~~~      |
    ||                     .=============.                     |
    ||                     |   Mr. Bear  :                     |
    ||                     `-------------'                     |
    \|_________________________________________________________| ''')
