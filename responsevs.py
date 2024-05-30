import random
from googlesearch import search
from time import sleep
import datetime

bugün = datetime.datetime.today()

sunucu_link = '0101010.aternos.me:64117'

random_replik = ["Yalnızlık krallığında dolaşıyorum. Bu sessizlikte yankılanan her adım, içimde daha fazla acı uyandırıyor.",
                 "Hayal kırıklığına uykusuz gecelerimi harcıyorum. Umutsuzluğun ağırlığı yüreğimi ezerek nefes almayı bile zorlaştırıyor.",
                 "Hatıralarımın tozlu raflarında kayboluyorum. Her an, kaybettiklerimin izini sürüyor, ama sonuç hep hüsranla sonlanıyor.",
                 "Gözyaşlarımın acı tuzlarıyla yıkanıyorum. Hayatın acı gerçekleri beni derin bir hüzne boğuyor, içimdeki karanlığı hiçbir ışık aydınlatamıyor.",
                 "Kaybettiğim sevdiklerimin anılarına sarılıyorum. Gülümsemeleri, şimdi yalnızca gözlerimin önünde titreyen hayaletler olarak varlıklarını sürdürüyor.",
                 "Gecenin sessizliğinde yalnızlıkla dans ediyorum. Yıldızlarla sohbet ediyorum, sessizliğin içindeki çığlık gibi yankılanan yalnızlıkla.",
                 "Umutsuzluğun soğuk sularında boğuluyorum. Her adım daha derine çekiyor beni, kurtuluşun sesi giderek soluklaşıyor.",
                 "Hayallerim kırık cam parçaları gibi yere saçılmış durumda. Her biri, umutların son nefesini verirken, içimde derin yaralar bırakıyor.",
                 "Kalbimin kırık telleriyle ezgiler söylüyorum. Acının melodisi kulaklarımda yankılanırken, içimdeki boşluk her notada daha da derinleşiyor.",
                 "Gözlerimdeki sis, geçmişin karanlık koridorlarını aydınlatamıyor. İçimdeki sıkıntı, ruhumu yavaşça sararak her umudu solmaya zorluyor.",
                 "Geleceğin karanlık gölgesi beni sarıyor. Her adım daha da belirsizlikle dolu, umutsuzluğun karanlık labirentlerinde kaybolmuşum gibi hissediyorum.",
                 "Kaybolmuş bir çikolata parçası gibi hissediyorum. Bulunmam için çığlıklar atsam da, kimse dinlemiyor.",
                 "Karanlık bulutlarla dans ediyorum, umutsuzluğun ritmiyle eşlik ediyorlar. Yağmur, içimdeki boşluğu doldurmuyor, sadece daha fazla yalnızlık getiriyor.",
                 "Hayat, bir saçma sapan oyunun içinde sıkışıp kalmış gibiyim. Her adım, daha da çıkmaz sokaklara götürüyor, çıkış yolu yok gibi hissediyorum.",
                 "Bir kedi miyim, yoksa bir kum tanesi mi, bilemiyorum. Kaybolmuş bir benlik arayışında, gerçeklik ve hayal arasında sıkışıp kalmışım.",
                 "Gözlerimdeki umutsuzluğun rengi, gökkuşağının en koyu tonlarına karışmış durumda. Renkler soluk, umutlar solmuş, dünya gri bir hüzün içinde yuvarlanıyor.",
                 "Kuşlar bile şarkı söylemiyor artık. Sessizlik, içimdeki çığlıkların yankılandığı tek şey, karanlık ve umutsuz bir senfoni.",
                 "Kendi kabuslarımın içinde kayboluyorum. Gerçeklik ve hayal arasında sıkışmış bir rüyanın içindeyim, uyanmak için çırpınıyorum ama her çaba boşuna.",
                 "Yaşam, tuhaf bir kabusa dönüştü. Gerçeklik, saçmalığın içinde kaybolup gidiyor, her adım daha da belirsizlik ve karmaşıklaşıyor.",
                 "Kendi gölgemle dans ediyorum, ama gölge bile benden kaçıyor. Kendimle yalnızım, ama yalnızlık bile beni kabul etmiyor.",
                 "Dünya, bir çılgınların cenneti gibi hissettiriyor. Herkes mutluluk içindeymiş gibi davranıyor, ama ben bu sahte gülücüklerin arasında yalnızca boşluğu görüyorum.",
                 "Kendi içimde bir labirentte kaybolmuş gibiyim. Her yol çıkmaza çıkıyor, umutlarımın sonu olmayan bir labirentte sonsuza dek kayboluyorum.",
                 "Ruhumun derinliklerinde bir karanlık var, içimi kemiren, yavaş yavaş her hücresini yok eden bir keder. Ne kadar çabalasam da, umutsuzluğun karanlık ellerinden kurtulamıyorum.",
                 "Gözyaşlarım, içimdeki umutsuzluğun acı sularında boğuluyor. Her damla, bir öncekinden daha fazla hüzün taşıyor, yüreğimdeki karanlık daha da derinleşiyor.",
                 "Hayatın anlamsızlığına boğulmuş gibi hissediyorum. Her gün, içimdeki çaresizlik duvarlarını daha da yükseltiyor, umutsuzluğun esaretinde yaşamaya devam ediyorum.",
                 "Ruhum, umutsuzluğun karanlık zindanında hapsolmuş gibi hissediyorum. Her çırpınış, daha da derin bir karanlığa gömülüyor, içimdeki çaresizlik beni yutmaya devam ediyor.",
                 "Yüreğim, umutsuzluğun donmuş topraklarında kaybolmuş gibi hissediyorum. Her atış, daha fazla acı ve yalnızlık taşıyor, içimdeki karanlık beni sarıp sarmalıyor."
                 "Gözlerim, umutsuzluğun sisli perdesiyle kaplı. Her bakış, daha fazla kayıp ve çaresizlik hissi uyandırıyor, içimdeki karanlık beni boğmaya devam ediyor.",
                 "Gözyaşlarımı içime akıtarak günüme başlıyorum.",
                 "Karanlık tarafım her gün biraz daha ağır basıyor.",
                 "Umutsuzluk denizinde boğulmak üzereyim.",
                 "Yalnızlık içimde bir delik açıyor, her gün biraz daha büyüyor.",
                 "Kendi içimde bir savaşın pençesindeyim.",
                 "Yıkıntılar altında kalmış bir şehir gibiyim.",
                 "Uykusuz geceler beni adeta yutup içine çekiyor.",
                 "Gelecekten umut kesilmiş bir gemi gibi sürükleniyorum.",
                 "Karanlık, içimi adeta bir zindan gibi sarıyor.",
                 "Çaresizlik, ruhumun derinliklerindeki kuyuyu kazıyor.",
                 "İçimdeki boşluk, hiçbir şeyi dolduramıyor.",
                 "Sessizlik, kendi acı çığlıklarımı daha da belirginleştiriyor.",
                 "Umutsuzluk, her adımda daha da ağırlaşıyor.",
                 "Ruhum, yıkıntılar altında ezilip kalmış gibi hissediyor.",
                 "Gözlerim, hiçbir umut ışığını göremiyor.",
                 "Sonsuz bir karanlık, içimi adeta yutmak üzere.",
                 "Çaresizlik, karanlığın içinde beni sarmalıyor.",
                 "Kendi yalnızlığım, yavaş yavaş beni tüketiyor.",
                 "Karanlık, içimdeki son umut kırıntılarını bile alıp götürüyor.",
                 "Umutsuzluk, kalbimin her atışında daha da güçleniyor.",
                 "Boşluk, içimdeki en büyük düşmanım gibi görünüyor.",
                 "Sessizlik, çaresizliğimi daha da derinleştiriyor.",
                 "Karanlık, içimdeki en karanlık köşeleri bile aydınlatıyor.",
                 "Umutsuzluk, ruhumun en derinlerinde yankılanıyor.",
                 "Yıkıntılar arasında bir yol bulmaya çalışıyorum.",
                 "Boşluk, içimde her şeyi yok ediyor.",
                 "Sessizlik, kendi acı çığlıklarımı bastırıyor.",
                 "Karanlık, içimi adeta bir zindan gibi sarıyor."
                 "Sessizlik, kendi acı çığlıklarımı daha da belirginleştiriyor.",
                 "Karanlık, içimdeki son umut kırıntılarını bile alıp götürüyor.",
                 "Umutsuzluk, kalbimin her atışında daha da güçleniyor.",
                 "Boşluk, içimdeki en büyük düşmanım gibi görünüyor.",
                 "Sessizlik, çaresizliğimi daha da derinleştiriyor.",
                 "Karanlık, içimdeki en karanlık köşeleri bile aydınlatıyor.",
                 "Umutsuzluk, ruhumun en derinlerinde yankılanıyor.",
                 "Yıkıntılar arasında bir yol bulmaya çalışıyorum.",
                 "Boşluk, içimde her şeyi yok ediyor.",
                 "Sessizlik, kendi acı çığlıklarımı bastırıyor.",
                 "Karanlık, içimi adeta bir zindan gibi sarıyor.",
                 "Gece gökyüzü, yıldızlarla dans ederken, ruhumun derinliklerinde bir çöküş yaşanıyor.",
                 "Kırık dökük hayaller, umut tozlarını rüzgarla savuruyor, umutsuzluğun çölünde kayboluyorum.",
                 "Çayırda kaybolmuş bir çiçek gibi, umutsuzluğun gölgesi altında soluyorum.",
                 "Gözlerim, umutsuzluğun sisli perdesini aralarken, karanlıkla yüzleşiyorum.",
                 "Çaresizliğin soğuk eli, içimi kemirirken, yalnızlıkla dans ediyorum.",
                 "Umutsuzluk, içimde bir yangın gibi, her an biraz daha büyüyerek, ruhumu yakıyor.",
                 "Ruhumun derinliklerinde, çürümüş hayallerin izleri, karanlık bir geçitte kayboluyor.",
                 "Umutsuzluğun sisli perdesi, gerçeği görmemi engelliyor, her adım biraz daha zorlaşıyor.",
                 "Kalbimin en karanlık köşelerinde, bir umut ışığı ararken, karanlık daha da yoğunlaşıyor.",
                 "Yıkıntılar arasında kaybolmuş bir gemi gibi, umutsuzluğun dalgaları arasında sürükleniyorum.",
                 "Boşluğun karanlığı, içimde bir çukur açıyor, hiçbir şeyi dolduramıyor, hiçbir şeyi hissedemiyorum.",
                 "Uykusuz geceler, içimdeki karanlıkla dans ediyor, kabuslarla besleniyor, hiçbir zaman rahat uyuyamıyorum.",
                 "Gözyaşlarım, umutsuzluğun acı sularıyla karışarak, içimdeki karanlıkta kayboluyor, hiçbir zaman durmuyor.",
                 "Her soluk alışımda, umutsuzluğun ağırlığı daha da artıyor, bedenim bu yük altında eziliyor.",
                 "Yalnızlık, içimde bir yarık açıyor, karanlığın içine çekiyor, hiçbir zaman dışarı çıkamıyorum.",
                 "Umutsuzluğun gri bulutları, ruhumu kaplayarak, içimdeki karanlıkla bütünleşiyor, hiçbir zaman ayrılamıyorum.",
                 "Kırık dökük hayallerim, umutsuzluğun çukuruna düşüyor, hiçbir zaman kurtulamıyorum.",
                 "Gece yıldızlarla parlıyor, umutsuzluğun karanlığında kaybolurken, içimdeki fırtına dinmek bilmiyor.",
                 "Ruhum, umutsuzluğun kasvetli ormanında kaybolmuş bir yolcu gibi, hiçbir zaman çıkış yolunu bulamıyorum.",
                 "Uykusuz gecelerim, içimdeki karanlıkla savaşıyor, ama hiçbir zaman galip gelemiyor, hiçbir zaman huzur bulamıyorum.",
                 "Yalnızlık, içimi kemiren bir asit gibi, ruhumu yavaşça eritiyor. Her geçen gün, umutsuzluğun buz gibi elleri daha da sıkı sarıyor, içimdeki boşluk beni adeta yutuyor.",
                 "Gözyaşlarım, içimdeki karanlık okyanusun sonsuz dalgalarında kayboluyor. Her bir damla, bir öncekinden daha fazla acı ve hüzün taşıyor, yüreğimdeki karanlık sonsuza kadar sürüyor.",
                 "Keder, bedenimi saran soğuk bir zincir gibi, ruhumu özgürlüğe kavuşturmadan önce beni tüketiyor. Her an, daha fazla hüsran ve çaresizlik duygularıyla boğuşuyorum, içimdeki karanlık beni adeta sarmalıyor.",
                 "Hayat, içinde kaybolmaktan başka bir şey değil. Her adım, daha fazla umutsuzluk ve yalnızlık getiriyor, içimdeki boşluk beni adeta bir kara deliğin içine çekiyor.",
                 "Umutsuzluk, ruhumun derinliklerinde adeta bir kara delik gibi, her şeyi yutuyor ve geride kalan sadece boşluk kalıyor. Ne kadar çabalasam da, içimdeki karanlık hiçbir ışıkla aydınlanmıyor.",
                 "Gözlerim, içimdeki karanlık labirentte kaybolmuş gibi hissediyorum. Her bakış, daha fazla çaresizlik ve keder getiriyor, içimdeki umutsuzluk beni adeta yutmaya hazır gibi.",
                 "Keder, ruhumun en derin köşelerine kadar işlemiş durumda. Her an, daha fazla hüsran ve umutsuzlukla boğuşuyorum, içimdeki karanlık beni adeta yutacak gibi.",
                 "Umutsuzluk, ruhumun kırılgan yapısını adeta paramparça ediyor. Her an, daha fazla acı ve yalnızlık hissi taşıyorum, içimdeki karanlık beni adeta tüketiyor.",
                 "Yalnızlık, içimi kemiren bir ateş gibi, her geçen gün daha da büyüyor ve ruhumu sarıp sarmalıyor. Her nefes, daha fazla umutsuzluk ve keder getiriyor, içimdeki boşluk beni adeta yutacak gibi.",
                 "Keder, bedenimi adeta bir zindana çevirmiş durumda. Her an, daha fazla hüzün ve çaresizlikle boğuşuyorum, içimdeki karanlık beni adeta bir hayalet gibi sarmalıyor.",
                 "Hayat, her geçen gün biraz daha anlamsızlaşıyor ve içimdeki boşluk giderek derinleşiyor. Ne kadar çabalasam da, umutsuzluğun karanlık sularında boğulmaktan başka bir şey yapamıyorum.",
                 "Gözyaşlarım, yüreğimin karanlık köşelerinde biriktikçe, içimdeki acı ve hüzün daha da artıyor. Her damla, ruhumun derinliklerinde bir yara açıyor ve içimi kanatıyor.",
                 "Keder, ruhumun her köşesine nüfuz etmiş durumda ve içimdeki umutsuzlukla birlikte beni adeta tüketiyor. Ne kadar çabalasam da, karanlığın pençelerinden kurtulamıyorum.",
                 "Yalnızlık, içimi kemiren bir ateş gibi, her geçen gün daha da büyüyor ve ruhumu sarıp sarmalıyor. Her nefes, içimdeki çaresizliği ve kederi artırıyor, adeta bir hayalet gibi beni takip ediyor.",
                 "Umutsuzluk, ruhumun içinde büyüyen bir kara delik gibi, her şeyi yutup yok ediyor. Ne kadar uğraşsam da, içimdeki karanlığı aydınlatamıyor ve sadece çaresizlikle boğuşuyorum.",
                 "Gözlerim, içimdeki karanlık sisin ardında kaybolmuş gibi hissediyorum. Her bakış, daha fazla hüzün ve çaresizlik getiriyor, içimdeki umutsuzluk beni adeta yutmaya hazır gibi.",
                 "Keder, ruhumun en kuytu köşelerine kadar işlemiş durumda. Her an, daha fazla hüsran ve umutsuzlukla boğuşuyorum, içimdeki karanlık beni adeta yutacak gibi.",
                 "Umutsuzluk, ruhumun kırılgan yapısını adeta paramparça ediyor. Her an, daha fazla acı ve yalnızlık hissi taşıyorum, içimdeki karanlık beni adeta tüketiyor.",
                 "Yalnızlık, içimi kemiren bir ateş gibi, her geçen gün daha da büyüyor ve ruhumu sarıp sarmalıyor. Her nefes, daha fazla umutsuzluk ve keder getiriyor, içimdeki boşluk beni adeta yutacak gibi.",
                 "Keder, bedenimi adeta bir zindana çevirmiş durumda. Her an, daha fazla hüzün ve çaresizlikle boğuşuyorum, içimdeki karanlık beni adeta bir hayalet gibi sarmalıyor.",
                 "Karanlık odamda yalnız başıma otururken, içimdeki çaresizlik adeta bir yük gibi üstüme çöküyor.",
                 "Umutsuzluk, ruhumun en derinliklerinde bir yangın gibi her şeyi yakıp kül ediyor, geriye sadece karanlık bir iz bırakıyor.",
                 "Gözlerim, içimdeki karanlık düşüncelerin labirentlerinde kaybolmuş gibi hissediyor, her bir adım daha da derinlere çekiyor beni.",
                 "Keder, içimi saran soğuk bir zincir gibi, bedenimi adeta donduruyor ve ruhumu özgürlükten mahrum bırakıyor.",
                 "Yalnızlık, içimi kemiren bir zehir gibi, her geçen gün daha da derinlere işliyor ve ruhumu adeta parçalıyor.",
                 "Gözyaşlarım, içimdeki umutsuzluğun acı sularında boğuluyor, her damla bir öncekinden daha fazla hüznü ve çaresizliği taşıyor.",
                 "Hayat, sanki içinde kaybolmak için bir labirent gibi, her yöne baktıkça daha da derinlere çekiyor beni, çıkışı bulamıyorum.",
                 "Umutsuzluk, ruhumun derinliklerinde adeta bir kara delik gibi, her şeyi emip yok ediyor ve geride kalan sadece boşluk kalıyor.",
                 "Keder, içimi adeta bir volkan gibi yavaşça eritiyor ve etrafımdaki her şeyi lavlar altında gömüyor, geriye sadece karanlık bir manzara kalıyor.",
                 "Yalnızlık, içimi kemiren bir ateş gibi, her geçen gün daha da büyüyor ve etrafımı sarıp sarmalıyor, kendimi adeta bir çölde kaybolmuş gibi hissediyorum."
                 ]


def get_respones(message: str)-> str:
    p_message = message.lower()
    if 'bayram' in p_message:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : gecmis bayraminiz mubarek olsun\n')
            print('BOT : gecmis bayraminiz mubarek olsun')
        return 'gecmis bayraminiz mubarek olsun'

    if 'selam' in p_message or 'selamun aleykum' in p_message:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : aleykum selam\n')
            print('BOT : aleykum selam')
        return 'aleykum selam'

    if'o7' in p_message:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : o7\n')
            print('BOT : o7')
        return 'o7'

    if 'merhaba' in p_message:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : merhaba\n')
            print('BOT : merhaba')
        return 'merhaba'

    if 'amk' in p_message:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : kufur yok sakin\n')
            print('BOT : kufur yok sakin')
        return 'kufur yok sakin'

    if 'sunucu' in p_message:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : '+sunucu_link+'\n1.20.2\n')
            print('BOT : '+sunucu_link+'\n1.20.2')
        return sunucu_link+'\n1.20.2'

    if 'mc gelc' in p_message:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : Sanal bir dünyada birlikte Minecraft keşiflerine çıkmak gerçekten harika olabilirdi, ama ben sadece bir programım.\n')
            print('BOT : Sanal bir dünyada birlikte Minecraft keşiflerine çıkmak gerçekten harika olabilirdi, ama ben sadece bir programım.')
        return 'Sanal bir dünyada birlikte Minecraft keşiflerine çıkmak gerçekten harika olabilirdi, ama ben sadece bir programım.'

    if 'ara' in p_message:
        links = []
        for i in search(p_message.strip('ara'), tld='co.in', num=10, stop=10, pause=2):
            links.append(i)
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : '+'\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(links[0],links[1],links[2],links[3],links[4],links[5],links[6],links[7],links[8],links[9]))
            print('BOT : '+'\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(links[0],links[1],links[2],links[3],links[4],links[5],links[6],links[7],links[8],links[9]))

        return '\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(links[0],links[1],links[2],links[3],links[4],links[5],links[6],links[7],links[8],links[9])

    if 'kapat' in p_message:
        if "meski132" in p_message.strip('kapat'):
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write('BOT : kapatiliyor\n')
                print('BOT : kapatiliyor\n')
                exit()
        else:
            return 'sifre yanlis'

    if 'sus' in p_message:
        if "<@1234579884483936422>" in p_message.strip('sus'):
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write('BOT : sustum\n')
                print('BOT : sustum\n')
                sleep(60)
                return 'susturma bitti (:'
        else:
            print('')


    if 'nasilsin' in p_message:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : iyi sen nasilsin\n')
            print('BOT : iyi sen nasilsin')
        return 'iyi sen nasilsin'

    if '<@1234579884483936422>' in p_message:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : ABI BEN ANLAMADIM GIF\n')
            print('BOT : ABI BEN ANLAMADIM GIF')
        return 'https://tenor.com/view/abi-ben-anlamad%C4%B1m-gif-27234629'

    if 'hehe' in p_message:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : heheheha GIF\n')
            print('BOT : heheheha GIF')
        return 'https://tenor.com/view/clash-royale-heheheha-grrr-emote-king-gif-24764224'

    if 'esek gif' in p_message:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : esek GIF\n')
            print('BOT : esek GIF')
        return 'https://tenor.com/view/shrek-donkey-shaking-sex-eddie-murphy-gif-17100737'

    if 'neyapi' in p_message or 'ne yapi' in p_message:
        replik = random.choice(random_replik)
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : '+replik+'\n')
            print('BOT : '+replik)
        return replik

    if 'naber' in p_message:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : iyi senden naber\n')
            print('BOT : iyi senden naber')
        return 'iyi senden naber'

    if 'iyi' in p_message:
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : Allah iyilik versin\n')
            print('BOT : Allah iyilik versin')
        return 'Allah iyilik versin'

    if message == 'cinnamoroll' or message == 'roll':
        sayi = random.randint(1, 10)
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : ' + str(sayi) + '\n')
            print('BOT : ' + str(sayi))
        return str(sayi)


    if p_message == '!help':
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write('BOT : [YARDIM MESAJI]\n')
            print('BOT : [YARDIM MESAJI]')
        return ('`roll = 1 ve 10 arasinda rastgele sayi secer\nara {aramak istediginiz sey} = googleda istediginiz seyi aradiginizda ilk cikan 10 seyi listeler\nbayram\nselamun aleykum\nmc gelcen mi\nmerhaba\nnasilsin\nnaber\niyi\n!help = yardim\neger bu komutlarin basina ? koyarsaniz size dm atar`')
