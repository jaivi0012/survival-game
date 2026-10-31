import pygame
import math
import sys, os


if hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)
else:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.mixer.set_num_channels(32)
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Survival Game")

maceX = 50
maceY = 20
x = 0
y = 500
oldX = 0

message = None

orcsX = [750, 740, 730, 720, 710, 700, 690, 680]
orcsY = [500, 500, 500, 500, 500, 500, 500, 500]

orcsVelocityX = [0, 0, 0, 0, 0, 0, 0, 0]
friction = 0.9
orcTopSpeed = [3, 2, 1, 2.5, 3.2, 3.9, 1.3, 1.6]
accel = [0,0,0,0,0,0,0,0]
orcsVelocityY = [0,0,0,0,0,0,0,0]
tntX = [0, 90, 180, 270, 360, 450, 540, 630, 720]

tntDistances = []

gameFont = pygame.font.Font(None, 36)
fightStarted = False
orc1Rect = pygame.Rect(0, 0, 0, 0)
orc2Rect = pygame.Rect(0, 0, 0, 0)
orc3Rect = pygame.Rect(0, 0, 0, 0)
orc4Rect = pygame.Rect(0, 0, 0, 0)
orc5Rect = pygame.Rect(0, 0, 0, 0)
orc6Rect = pygame.Rect(0, 0, 0, 0)
orc7Rect = pygame.Rect(0, 0, 0, 0)
orc8Rect = pygame.Rect(0, 0, 0, 0)

velocityY = 0
Orc1VelocityY = 0
Orc2VelocityY = 0
Orc3VelocityY = 0
Orc4VelocityY = 0
Orc5VelocityY = 0
Orc6VelocityY = 0
Orc7VelocityY = 0
Orc8VelocityY = 0

currentMessage = 1

# --- Cutscene Lists ---
introDialogue = [
    'what a HUMAN ? In my DOMAIN',
    'HOW DARE YOU ENTER MY DOMAIN !!!!',
    'YOU WILL FACE MY WRATH !!',
    'but im kinda sleepy',
    'YOU WILL FACE MY ARMY OF ORCS !!',
    'i will sleep till then :)',
    'zzzzzzzZzzzzzzZZzzzzzZzZZzZ'
]

midFightDialogue = [
    'HOW DID YOU KILL MY ORCS',
    'A WEAK HUMAN LIKE YOU KILLED MY ORCS',
    'I WILL TAKE CAR OF YOU MYSELF',
    'I WILL BRING MY ARMY BACK FROM DEAD',
    ' YOU STAND NO CHANCE AGAINST US',
    'where is this main character music coming from ?',
    ' WELL PREPARE YOUR SELF HUMAN'
]

bossDefeatDialogue = [
    'NO I CANT LOSE ver ',
    'Someday Somehow I will Defeat You',
    'I have lost to you little one ',
    'now you may do whateyou want in this DOMAIN',
    'you can exit this domain if you like ',
    'ORC KING DIES',
    'you have defeated the orc king',
    'an exit has appeared'
]

orcBossSpawn = False


activeDialogueList = introDialogue  
dialogueIndex = 0
dialogueState = 'intro'  
showDialogue = True

orcDamege = -20

orcBossHelth = 6000
orcBossAttackDamage = 150
orcHelth = [150, 100, 100, 100, 100, 100, 100, 100]
playerHelth = 3000

tntVelocity = 0

clock = pygame.time.Clock()

maceHit = pygame.mixer.Sound('survivalGame/Sounds/mace.wav')
lungeSfx = pygame.mixer.Sound('survivalGame/Sounds/spear.wav')
tntSfx = pygame.mixer.Sound('survivalGame/Sounds/tnt.wav')
damageSfx = pygame.mixer.Sound('survivalGame/Sounds/damage.wav')
tntY = 0

running = True
doubleJump = True
inAir = False
playerDir = 'Right'
rodPulled = False
attack = False
playerAnim = False
PlayerMoving = False
exploded = False

waves = True
tntPlayed = False

orbital = True
orcClear = True
waveOver = False
waveCounter = 0

orcBossX = 750
orcBossY = 430  
orcBossRect = pygame.Rect(0, 0, 0, 0)
orcBossVelocityX = 0
orcBossSpeed = 1.5  

orcSpawn1 = False
orcSpawn2 = False
orcSpawn3 = False
orcSpawn4 = False
orcSpawn5 = False
orcSpawn6 = False
orcSpawn7 = False
orcSpawn8 = False

orcsClear = True
bossSpawn = False
gameBegin = False
menuButtonPress = True
showDialogue = True
lunge = False
override = False
enter = 0
lungeCounter = 0
begin = False
currentMusic = None



next = 0
dialogueCounter = 0
knockback = 20
jumpCount = 0
jumpHeight = -15
maceJump = -25
gravity = 0.9
base = 500
speed = 8
Power = 20
enterCounter = 0
orcSpeed = 3
counter = 0
count = 0
cycles = 0
PlayerImg = None

gameMenu = pygame.image.load('survivalGame/frontMenu.png').convert()
playButton = pygame.image.load('survivalGame/playButton.png').convert()
exitButton = pygame.image.load('survivalGame/exitButton.png').convert()
DialogueBoxOG = pygame.image.load('survivalGame/dialogueBox.png').convert_alpha()
DialogueBox = pygame.transform.scale(DialogueBoxOG, (700, 80))

orc1OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orc2OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orc3OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orc4OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orc5OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orc6OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orc7OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orc8OG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()
orcBossOG = pygame.image.load('survivalGame/Orc1.png').convert_alpha()


maceOG = pygame.image.load('survivalGame/mace.png').convert_alpha()
spearOG = pygame.image.load('survivalGame/Diamond_Spear.png').convert_alpha()
fishingRodOG = pygame.image.load('survivalGame/Fishing_Rod.png').convert_alpha()

tnt1OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt2OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt3OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt4OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt5OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt6OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt7OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt8OG = pygame.image.load('survivalGame/tnt.jpeg').convert()
tnt9OG = pygame.image.load('survivalGame/tnt.jpeg').convert()

platform1OG = pygame.image.load('survivalGame/platform.png').convert_alpha()
platform2OG = pygame.image.load('survivalGame/platform.png').convert_alpha()
platform3OG = pygame.image.load('survivalGame/platform.png').convert_alpha()
platform4OG = pygame.image.load('survivalGame/platform.png').convert_alpha()
platform5OG = pygame.image.load('survivalGame/platform.png').convert_alpha()
platform6OG = pygame.image.load('survivalGame/platform.png').convert_alpha()


playerWalk = [ pygame.image.load('survivalGame/SoldierWalk/Soldier_Walk1.png').convert_alpha(),
               pygame.image.load('survivalGame/SoldierWalk/Soldier_Walk2.png').convert_alpha(),
               pygame.image.load('survivalGame/SoldierWalk/Soldier_Walk3.png').convert_alpha(),
               pygame.image.load('survivalGame/SoldierWalk/Soldier_Walk4.png').convert_alpha(),
               pygame.image.load('survivalGame/SoldierWalk/Soldier_Walk5.png').convert_alpha(),
               pygame.image.load('survivalGame/SoldierWalk/Soldier_Walk6.png').convert_alpha(),
               pygame.image.load('survivalGame/SoldierWalk/Soldier_Walk7.png').convert_alpha(),
               pygame.image.load('survivalGame/SoldierWalk/Soldier_Walk8.png').convert_alpha()
               ]

playerIdle = pygame.image.load('survivalGame/SoldierWalk/Soldier_Walk8.png').convert_alpha()

playerAnimationIndex = 0
playerAnimationCount = 0
playerAnimationSpeed = 2


orc1 = pygame.transform.scale(orc1OG,(70,70))
orc2 = pygame.transform.scale(orc2OG,(70,70))
orc3 = pygame.transform.scale(orc3OG,(70,70))
orc4 = pygame.transform.scale(orc4OG,(70,70))
orc5 = pygame.transform.scale(orc5OG,(70,70))
orc6 = pygame.transform.scale(orc6OG,(70,70))
orc7 = pygame.transform.scale(orc7OG,(70,70))
orc8 = pygame.transform.scale(orc8OG,(70,70))

orcBoss = pygame.transform.scale(orcBossOG, (150,150))

# weapon image load --------------------------------------------------------------------------------
mace = pygame.transform.scale(maceOG,(30,30))
maceFlipped = pygame.transform.flip(mace, True, False)
spear = pygame.transform.scale(spearOG,(30,30))
spearFlipped = pygame.transform.flip(spear, True, False)
fishingRod = pygame.transform.scale(fishingRodOG,(30,30))
fishingRodFlipped = pygame.transform.flip(fishingRod, True, False)
currentWeapon = 'Mace'

currentWeaponHold = maceFlipped
# ---------------------------------------------------------------------------------------------------

tnt1 = pygame.transform.scale(tnt1OG,(30,30))
tnt2 = pygame.transform.scale(tnt2OG,(30,30))
tnt3 = pygame.transform.scale(tnt3OG,(30,30))
tnt4 = pygame.transform.scale(tnt4OG,(30,30))
tnt5 = pygame.transform.scale(tnt5OG,(30,30))
tnt6 = pygame.transform.scale(tnt6OG,(30,30))
tnt7 = pygame.transform.scale(tnt7OG,(30,30))
tnt8 = pygame.transform.scale(tnt8OG,(30,30))
tnt9 = pygame.transform.scale(tnt9OG,(30,30))

platform = pygame.transform.scale(platform1OG,(150,50))

platform2 = pygame.transform.scale(platform2OG,(150,50))
platform3 = pygame.transform.scale(platform3OG,(150,50))
platform4 = pygame.transform.scale(platform4OG,(150,50))
platform5 = pygame.transform.scale(platform5OG,(150,50))
platform6 = pygame.transform.scale(platform6OG,(150,50))




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if gameBegin == False:
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    enter = 1
                if event.key == pygame.K_UP:
                    menuButtonPress = True
                if event.key == pygame.K_DOWN:
                    menuButtonPress = False
     
          

        if gameBegin == True:
            if event.type == pygame.KEYDOWN:
                PlayerMoving = False
                if event.key == pygame.K_SPACE and doubleJump == True:
                    velocityY = jumpHeight  
                    jumpCount += 1


                if event.key == pygame.K_d:
                    attack = True
                    currentWeapon = 'Mace'

                if event.key == pygame.K_LCTRL and showDialogue == True:
                    dialogueIndex += 1

                if dialogueIndex > 6 and dialogueState == 'middle':
                    dialogueIndex = 0
                    dialogueState = 'end'
                    waves = False          
                    orcBossSpawn = True    
                    showDialogue = False   

                if dialogueState == 'end':
                    activeDialogueList = bossDefeatDialogue

                if dialogueState == 'intro' and dialogueIndex > 6:
                    dialogueState = 'middle'
                    dialogueIndex = 0
                    showDialogue = False
                    waves = True
                    begin = True
                    orcsClear = False
                if event.key == pygame.K_s:
                    rodPulled = True
                    cycles = 0
                    count = 0
                    currentWeapon = 'FishingRod'
                    

                if event.key == pygame.K_a:
                    lunge = True

    helthText = gameFont.render(f'Helth :- {playerHelth} ', False , (255,255,255))
    if orcBossSpawn == True:
        bossHealthText = gameFont.render(f'Orc King Health :- {orcBossHelth}', False, (255, 0, 0))
    if lunge == True:
        lungeCounter += 1
        currentWeapon = 'Spear'
    if lungeCounter == 4:
        lungeCounter = 0
        lunge = False
        
    if attack == True:
        counter += 1

    if counter >= 15:
        attack = False  
        counter = 0   

    if showDialogue == True:
        message = activeDialogueList[dialogueIndex]

    if dialogueState == 'middle':
        activeDialogueList = midFightDialogue
        waves = True
  
   
    playerRect = pygame.Rect(x + 21, y+ 22, 30, 40)
    
    maceRect = pygame.Rect(x + 25,y + 45,20,80)
    

    if gameBegin == True and waves == True:
        orc1Rect = pygame.Rect(orcsX[0] + 13, orcsY[0] + 25, 30, 35)
        orc2Rect = pygame.Rect(orcsX[1] + 13, orcsY[1] + 25, 30, 35)
        orc3Rect = pygame.Rect(orcsX[2] + 13, orcsY[2] + 25, 30, 35)
        orc4Rect = pygame.Rect(orcsX[3] + 13, orcsY[3] + 25, 30, 35)
        orc5Rect = pygame.Rect(orcsX[4] + 13, orcsY[4] + 25, 30, 35)
        orc6Rect = pygame.Rect(orcsX[5] + 13, orcsY[5] + 25, 30, 35)
        orc7Rect = pygame.Rect(orcsX[6] + 13, orcsY[6] + 25, 30, 35)
        orc8Rect = pygame.Rect(orcsX[7] + 13, orcsY[7] + 25, 30, 35)

        
    keys = pygame.key.get_pressed()

    if enter == 1:
        enterCounter += 1

    if enterCounter == 15:
        enter = 0
        enterCounter = 0
    if gameBegin == True:
        if keys[pygame.K_LEFT]:
            x -= speed
        if keys[pygame.K_RIGHT]:
            x += speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
            PlayerMoving = True
        if lunge == True and playerDir == 'Right':
            x += Power
            lungeSfx.play()
        if lunge == True and playerDir == 'Left':
            x -= Power
            lungeSfx.play()
    if jumpCount >= 2:
        doubleJump = False

    if jumpCount <= 0:
        doubleJump = True

    if y == base:
        jumpCount = 0    

    if y >= 450:
        inAir = False

    if y < 500:
        inAir = True    

  
    if currentWeapon == 'Mace' and playerDir == 'Right':
        currentWeaponHold = maceFlipped
    if currentWeapon == 'Mace' and playerDir == 'Left':
            currentWeaponHold = mace
    if currentWeapon == 'Spear' and playerDir == 'Right':
        currentWeaponHold = spear
    if currentWeapon == 'Spear' and playerDir == 'Left':
        currentWeaponHold = spearFlipped
    if currentWeapon == 'FishingRod' and playerDir == 'Right':
        currentWeaponHold = fishingRod
    if currentWeapon == 'FishingRod' and playerDir == 'Left':
            currentWeaponHold = fishingRodFlipped

    if orcsClear == True:
        waves = False
    if x > oldX:
        playerDir = 'Right'
        maceX = 50
        playerAnim = True
    if x < oldX:
        
        playerDir = 'Left'
        maceX = -15
        playerAnim = True

    if x == oldX:
        playerAnim = False
    
    if x < 0:
        x = 0

    if x > 750:
        x = 750    

    if y > 500:
        y = 500
    
    if playerHelth <= 0:
        
        deathText = gameFont.render('YOU DIED', True, (255, 0, 0))
        screen.blit(deathText, (340, 280))
        pygame.display.flip()
        pygame.time.delay(1000)
        pygame.event.clear()          

        pygame.mixer.stop()           

       
        x = 0
        y = 500
        oldX = 0
        velocityY = 0
        playerHelth = 3000
        playerDir = 'Right'
        maceX = 50
        currentWeapon = 'Mace'
        currentWeaponHold = maceFlipped
        attack = False
        counter = 0
        lunge = False
        lungeCounter = 0
        jumpCount = 0
        doubleJump = True
        PlayerMoving = False
        playerAnim = False
        playerAnimationIndex = 0
        playerAnimationCount = 0

        
        orcsX = [750, 740, 730, 720, 710, 700, 690, 680]
        orcsY = [500, 500, 500, 500, 500, 500, 500, 500]
        orcsVelocityX = [0, 0, 0, 0, 0, 0, 0, 0]
        orcsVelocityY = [0, 0, 0, 0, 0, 0, 0, 0]
        orcHelth = [150, 100, 100, 100, 100, 100, 100, 100]
        orcSpawn1 = False
        orcSpawn2 = False
        orcSpawn3 = False
        orcSpawn4 = False
        orcSpawn5 = False
        orcSpawn6 = False
        orcSpawn7 = False
        orcSpawn8 = False

      
        orcBossHelth = 6000
        orcBossX = 750
        orcBossY = 430
        orcBossSpawn = False

        fightStarted = False
        waves = True
        orcsClear = True
        waveOver = False
        begin = False
        dialogueState = 'intro'
        activeDialogueList = introDialogue
        dialogueIndex = 0
        dialogueCounter = 0
        showDialogue = True
        exitOpen = False

        
        rodPulled = False
        count = 0
        cycles = 0
        tntY = 0
        tntVelocity = 0
        tntPlayed = False

        
        gameBegin = False
        enter = 0
        enterCounter = 0
        menuButtonPress = True

    wantedMusic = None
    if gameBegin == True:
        if dialogueState == 'intro':
            wantedMusic = 'intro'     
        if dialogueState == 'middle' and waveOver == False:
            wantedMusic = 'intro'     
        if dialogueState == 'middle' and waveOver == True and showDialogue == True:
            wantedMusic = 'mid'      
        if dialogueState == 'end' and orcBossSpawn == True:
            wantedMusic = 'mid'
    if wantedMusic != currentMusic:
        if wantedMusic == 'intro':
            pygame.mixer.music.load('survivalGame/Sounds/playfulMassacre.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        if wantedMusic == 'mid':
            pygame.mixer.music.load('survivalGame/Sounds/cahosConstruct.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)
        if wantedMusic == None:
            pygame.mixer.music.fadeout(1000)
        currentMusic = wantedMusic


    velocityY += gravity
    y += velocityY
     
    if y > base:
        y = base
        velocityY = 0

    if gameBegin == True and orcBossSpawn == True:
 
        orcBossRect = pygame.Rect(orcBossX + 35, orcBossY + 25, 80, 100)

      
        if x > orcBossX:
            orcBossX += orcBossSpeed
        if x < orcBossX:
            orcBossX -= orcBossSpeed
 
        if playerRect.colliderect(orcBossRect):
            playerHelth -= 2  

        if maceRect.colliderect(orcBossRect) and attack == True:
            fallspeed = max(velocityY, 0)
            damage = 10 + fallspeed * 4
            orcBossHelth -= damage
            if y < base:
                velocityY = maceJump
                maceHit.play()   
            if y >= base:
                damageSfx.play()               
            attack = False
        if orcBossSpawn == True and orcBossHelth <= 0:
            orcBossSpawn = False
            showDialogue = True
            dialogueState = 'victory'
            activeDialogueList = bossDefeatDialogue
            dialogueIndex = 0

    if gameBegin == True and waves == True:

        if maceRect.colliderect(orc1Rect) and attack == True and orcSpawn1 == True:
            fallspeed = max(velocityY, 0)
            damage = 10 + fallspeed * 4
            orcHelth[0] -= damage
            if y < base:
                velocityY = maceJump
                maceHit.play()   
            if y >= base:
                damageSfx.play()               
            if playerDir == 'Left':
                orcsVelocityX[0] -= knockback
            if playerDir == 'Right':
                orcsVelocityX[0] += knockback
            attack = False
            
    

            
     

        if maceRect.colliderect(orc2Rect) and attack == True and orcSpawn2 == True:
            fallspeed = max(velocityY, 0)
            damage = 10 + fallspeed * 4
            orcHelth[1] -= damage
            if y < base:
                velocityY = maceJump 
                maceHit.play()   
            if y >= base:
                damageSfx.play()               
            if playerDir == 'Left':
                orcsVelocityX[1] -= knockback
            if playerDir == 'Right':
                orcsVelocityX[1] += knockback              
            attack = False
        

        

        if maceRect.colliderect(orc3Rect) and attack == True and orcSpawn3 == True:
            fallspeed = max(velocityY, 0)
            damage = 10 + fallspeed * 4
            orcHelth[2] -= damage
            if y < base:
                velocityY = maceJump                  
                maceHit.play() 
            if y >= base:
                damageSfx.play()               
            if playerDir == 'Left':
                orcsVelocityX[2] -= knockback
            if playerDir == 'Right':
                orcsVelocityX[2] += knockback 
            attack = False
            
        

        if maceRect.colliderect(orc4Rect) and attack == True and orcSpawn4 == True:
            fallspeed = max(velocityY, 0)
            damage = 10 + fallspeed * 4
            orcHelth[3] -= damage
            if y < base:
                velocityY = maceJump                   
                maceHit.play()
            if y >= base:
                damageSfx.play()               
            if playerDir == 'Left':
                orcsVelocityX[3] -= knockback
            if playerDir == 'Right':
                orcsVelocityX[3] += knockback
            attack = False
                
            

        

        if maceRect.colliderect(orc5Rect) and attack == True and orcSpawn5 == True:
            fallspeed = max(velocityY, 0)
            damage = 10 + fallspeed * 4
            orcHelth[4] -= damage
            if y < base:
                velocityY = maceJump   
                maceHit.play()  
            if y >= base:
                damageSfx.play()               
            if playerDir == 'Left':
                orcsVelocityX[4] -= knockback
            if playerDir == 'Right':
                orcsVelocityX[4] += knockback               
            attack = False
            
            


        
        

        if maceRect.colliderect(orc6Rect) and attack == True and orcSpawn6 == True:
            fallspeed = max(velocityY, 0)
            damage = 10 + fallspeed * 4
            orcHelth[5] -= damage
            if y < base:
                velocityY = maceJump 
                maceHit.play() 
            if y >= base:
                damageSfx.play()               
            if playerDir == 'Left':
                orcsVelocityX[5] -= knockback
            if playerDir == 'Right':
                orcsVelocityX[5] += knockback                 
            attack = False
            

        

        if maceRect.colliderect(orc7Rect) and attack == True and orcSpawn7 == True:
            fallspeed = max(velocityY, 0)
            damage = 10 + fallspeed * 4
            orcHelth[6] -= damage
            if y < base:
                velocityY = maceJump 
                maceHit.play()
            if y >= base:
                damageSfx.play()               
            if playerDir == 'Left':
                orcsVelocityX[6] -= knockback
            if playerDir == 'Right':
                orcsVelocityX[6] += knockback                  
            attack = False
        

        
       
        

        if maceRect.colliderect(orc8Rect) and attack == True and orcSpawn8 == True:
            fallspeed = max(velocityY, 0)
            damage = 10 + fallspeed * 4
            orcHelth[7] -= damage
            if y < base:
                velocityY = maceJump 
                maceHit.play() 
            if y >= base:
                damageSfx.play()               
            if playerDir == 'Left':
                orcsVelocityX[7] -= knockback
            if playerDir == 'Right':
                orcsVelocityX[7] += knockback                  
            attack = False 
            

        if playerRect.colliderect(orc1Rect) and orcSpawn1 == True:
            playerHelth -= 10

        if playerRect.colliderect(orc2Rect) and orcSpawn2 == True:
            playerHelth -= 10

        if playerRect.colliderect(orc3Rect) and orcSpawn3 == True:
            playerHelth -= 10

        if playerRect.colliderect(orc4Rect) and orcSpawn4 == True:
            playerHelth -= 10

        if playerRect.colliderect(orc5Rect) and orcSpawn5 == True:
            playerHelth -= 10

        if playerRect.colliderect(orc6Rect) and orcSpawn6 == True:
            playerHelth -= 10

        if playerRect.colliderect(orc7Rect) and orcSpawn7 == True:
            playerHelth -= 10

        if playerRect.colliderect(orc8Rect) and orcSpawn8 == True:
            playerHelth -= 10

        if orcSpawn1 == True and waves == True:
            accel[0] = orcTopSpeed[0] * (1 - friction)

            if x > orcsX[0]:
                orcsVelocityX[0] += accel[0]
            if x < orcsX[0]:
                orcsVelocityX[0] -= accel[0]

            orcsVelocityX[0] *= friction

            orcsX[0] += orcsVelocityX[0]

        if orcSpawn2 == True and waves == True:

            accel[1] = orcTopSpeed[1] * (1- friction)

            if x > orcsX[1]:
                orcsVelocityX[1] += accel[1]
            if x < orcsX[1]:
                orcsVelocityX[1] -= accel[1]

            orcsVelocityX[1] *= friction

            orcsX[1] += orcsVelocityX[1]


        if orcSpawn3 == True and waves == True:
            accel[2] = orcTopSpeed[2] * (1- friction)
            
            if x > orcsX[2]:
                orcsVelocityX[2] += accel[2]
            if x < orcsX[2]:
                orcsVelocityX[2] -= accel[2]
            
            orcsVelocityX[2] *= friction
            
            orcsX[2] += orcsVelocityX[2]
            
        if orcSpawn4 == True and waves == True:
    
            accel[3] = orcTopSpeed[3] * (1- friction)
            
            if x > orcsX[3]:
                orcsVelocityX[3] += accel[3]
            if x < orcsX[3]:
                orcsVelocityX[3] -= accel[3]
            
            orcsVelocityX[3] *= friction
            
            orcsX[3] += orcsVelocityX[3]

        if orcSpawn5 == True and waves == True:
            accel[4] = orcTopSpeed[4] * (1- friction)
                
            if x > orcsX[4]:
                orcsVelocityX[4] += accel[4]
            if x < orcsX[4]:
                orcsVelocityX[4] -= accel[4]
                
            orcsVelocityX[4] *= friction
                
            orcsX[4] += orcsVelocityX[4]

        if orcSpawn6 == True and waves == True:

            accel[5] = orcTopSpeed[5] * (1- friction)
                
            if x > orcsX[5]:
                orcsVelocityX[5] += accel[5]
            if x < orcsX[5]:
                orcsVelocityX[5] -= accel[5]
                
            orcsVelocityX[5] *= friction
                
            orcsX[5] += orcsVelocityX[5]

        if orcSpawn7 == True and waves == True:

            accel[6] = orcTopSpeed[6] * (1- friction)
                
            if x > orcsX[6]:
                orcsVelocityX[6] += accel[6]
            if x < orcsX[6]:
                orcsVelocityX[6] -= accel[6]
                
            orcsVelocityX[6] *= friction
                
            orcsX[6] += orcsVelocityX[6]

        if orcSpawn8 == True and waves == True:

            accel[7] = orcTopSpeed[7] * (1- friction)
                
            if x > orcsX[7]:
                orcsVelocityX[7] += accel[7]
            if x < orcsX[7]:
                orcsVelocityX[7] -= accel[7]
                
            orcsVelocityX[7] *= friction
                
            orcsX[7] += orcsVelocityX[7]

      



# playerMovingAnimation
# playerAnimationIndex = 0
# playerAnimationCount = 0
# playerAnimationSpeed = 8



        if PlayerMoving == True:
            playerAnimationCount += 1

        if playerAnimationCount > playerAnimationSpeed:
            playerAnimationIndex += 1
            playerAnimationCount = 0

        if playerAnimationIndex > 7:
            playerAnimationIndex = 0

   
    if begin == True:
        orcSpawn1 = True
        orcSpawn2 = True
        orcSpawn3 = True
        orcSpawn4 = True
        orcSpawn5 = True
        orcSpawn6 = True
        orcSpawn7 = True
        orcSpawn8 = True
        begin = False
        fightStarted = True          

    
    if fightStarted == True and orcSpawn1 == False and orcSpawn2 == False and orcSpawn3 == False and orcSpawn4 == False and orcSpawn5 == False and orcSpawn6 == False and orcSpawn7 == False and orcSpawn8 == False and waveOver == False:
        orcsClear = True
        showDialogue = True
        waveOver = True
        dialogueState = 'middle'
        activeDialogueList = midFightDialogue
        dialogueIndex = 0

# --------------------------------------------------------------------------------------------------------------------------
    oldX = x

    if gameBegin == True:
        screen.blit(currentWeaponHold, (x + maceX, y + maceY))  # Draw the mace image at the player's position

        if playerAnim == False:
            PlayerImg = playerIdle

        if playerDir == 'Left' and playerAnim == True or playerDir == 'Right' and playerAnim == True:
            PlayerImg = playerWalk[playerAnimationIndex]
        PlayerImg = pygame.transform.scale(PlayerImg, (70, 70))
        if playerDir == 'Left':
            PlayerImg = pygame.transform.flip(PlayerImg, True, False)
        if playerDir == 'Right':
            PlayerImg = pygame.transform.flip(PlayerImg, False, False)

        if showDialogue == True:
            dialogueCounter += 1

        if dialogueCounter >= 180:
            dialogueCounter = 0

        screen.blit(PlayerImg, (x, y))

        if orcSpawn1 == True:
            screen.blit(orc1, (orcsX[0], orcsY[0]))  # Draw the orc image at a fixed position
        if orcSpawn2 == True:
            screen.blit(orc2, (orcsX[1], orcsY[1]))  # Draw the orc image at a fixed position
        if orcSpawn3 == True:
            screen.blit(orc3, (orcsX[2], orcsY[2]))  # Draw the orc image at a fixed position
        if orcSpawn4 == True:
            screen.blit(orc4, (orcsX[3], orcsY[3]))  # Draw the orc image at a fixed position
        if orcSpawn5 == True:
            screen.blit(orc5, (orcsX[4], orcsY[4]))  # Draw the orc image at a fixed position
        if orcSpawn6 == True:
            screen.blit(orc6, (orcsX[5], orcsY[5]))  # Draw the orc image at a fixed position
        if orcSpawn7 == True:
            screen.blit(orc7, (orcsX[6], orcsY[6]))  # Draw the orc image at a fixed position
        if orcSpawn8 == True:
            screen.blit(orc8, (orcsX[7], orcsY[7]))  # Draw the orc image at a fixed position

        if gameBegin == True and orcBossSpawn == True:
            screen.blit(orcBoss, (orcBossX, orcBossY))

    playButtonRect = pygame.Rect(175, 235, 450, 100)
    exitButtonRect = pygame.Rect(175, 385, 450, 100)


    if gameBegin == False:
        if menuButtonPress == True:  
            pygame.draw.rect(screen,'red', playButtonRect)
        if menuButtonPress == False:
            pygame.draw.rect(screen,'red',exitButtonRect)

    if gameBegin == False:
        screen.blit(gameMenu, (150, 50))


    if enter == 1 and menuButtonPress == True:
        gameBegin = True
    if enter == 1 and menuButtonPress == False:
        running = False

    if gameBegin == False:
        screen.blit(playButton,(200, 250))
        screen.blit(exitButton,(200, 400))

    screen.blit(platform, (0, 560))  # Draw the platform image

    if rodPulled == True:
        count += 1
        
    if count >= 60:
        count = 0

    if count > 30:
        activation = True

    if count <= 0:
        activation = False
        cycles += 1

    if rodPulled == True:
        if tntPlayed == False:
            tntSfx.play()
        tntPlayed = True
    

    if rodPulled == False and tntPlayed == True:
        tntPlayed = False 

    if rodPulled == True and activation == False and orbital == True:

        
    
        screen.blit(tnt1, (0, tntY))  # Draw the TNT image at a fixed position
        screen.blit(tnt2, (90, tntY))  # Draw the second TNT image at a fixed position
        screen.blit(tnt3, (180, tntY))  # Draw the third TNT image at a fixed position
        screen.blit(tnt4, (270, tntY))  # Draw the fourth TNT image at a fixed position
        screen.blit(tnt5, (360, tntY))  # Draw the fifth TNT image at a fixed position
        screen.blit(tnt6, (450, tntY))  # Draw the sixth TNT image at a fixed position
        screen.blit(tnt7, (540, tntY))  # Draw the seventh TNT image at a fixed position
        screen.blit(tnt8, (630, tntY))  # Draw the seventh TNT image at a fixed position
        screen.blit(tnt9, (720, tntY))  # Draw the seventh TNT image at a fixed position

        tntVelocity += gravity
        tntY += tntVelocity

    if tntY > 528:
        tntY = 528
        tntVelocity = 0    


    if orcHelth[0] <= 0:
        orcHelth[0] = 150
        orcsX[0] = 750
        orcsY[0] = 500
        orcSpawn1 = False
    if orcHelth[1] <= 0:
        orcHelth[1] = 100
        orcsX[1] = 740
        orcsY[1] = 500
        orcSpawn2 = False
    if orcHelth[2] <= 0:
        orcHelth[2] = 100
        orcsX[2] = 730
        orcsY[2] = 500
        orcSpawn3 = False
    if orcHelth[3] <= 0:
        orcHelth[3] = 100
        orcsX[3] = 720
        orcsY[3] = 500    
        orcSpawn4 = False
    if orcHelth[4] <= 0:
        orcHelth[4] = 100
        orcsX[4] = 710
        orcsY[4] = 500
        orcSpawn5 = False
    if orcHelth[5] <= 0:
        orcHelth[5] = 100
        orcsX[5] = 700
        orcsY[5] = 500
        orcSpawn6 = False
    if orcHelth[6] <= 0:
        orcHelth[6] = 100
        orcsX[6] = 690
        orcsY[6] = 500
        orcSpawn7 = False
    if orcHelth[7] <= 0:
        orcHelth[7] = 100
        orcsX[7] = 680
        orcsY[7] = 500
        orcSpawn8 = False
    if cycles >= 3:
        if rodPulled == True and orbital == True:
            for i in range(len(tntX)):
                ax = tntX[i] + 15
                ay = tntY + 15

                for l in range(len(orcsX)):
                    bx = orcsX[l] + 35
                    by = orcsY[l] + 35

                    distance = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
                    tntDistances.append(distance)

                    if distance < 65:
                        orcHelth[l] -= 200
        cycles = 0
        rodPulled = False
        tntY = 0
        tntVelocity = 0
        activation = False


    screen.blit(platform2, (150, 560))  # Draw the second platform image
    screen.blit(platform3, (301, 560))  # Draw the third platform image
    screen.blit(platform4, (450, 560))  # Draw the fourth platform image
    screen.blit(platform5, (600, 560))  # Draw the fifth platform image
    screen.blit(platform6, (750, 560))  # Draw the sixth platform image
   # pygame.draw.rect(screen, (139, 69, 19), (0, 570, 800, 50))  # Draw a brown rectangle
   # pygame.draw.rect(screen, (255, 0, 0), maceRect)  # Draw the red rectangle for the mace
   # pygame.draw.rect(screen, 'red', orc1Rect)
   # pygame.draw.rect(screen, 'red', playerRect)
    if rodPulled == True and activation == True and orbital == True:

          
            
            pygame.draw.rect(screen, ("white"), (0, tntY, 30, 30))  # Draw a red rectangle for the TNT
            pygame.draw.rect(screen, ("white"), (90, tntY, 30, 30))
            pygame.draw.rect(screen, ("white"), (180, tntY, 30, 30))
            pygame.draw.rect(screen, ("white"), (270, tntY, 30, 30))
            pygame.draw.rect(screen, ("white"), (360, tntY, 30, 30))
            pygame.draw.rect(screen, ("white"), (450, tntY, 30, 30))
            pygame.draw.rect(screen, ("white"), (540, tntY, 30, 30))
            pygame.draw.rect(screen, ("white"), (630, tntY, 30, 30))
            pygame.draw.rect(screen, ("white"), (720, tntY, 30, 30))
            tntVelocity += gravity
            tntY += tntVelocity
    screen.blit(helthText, (20, 20))
   # pygame.draw.rect(screen, ('white'), (750, 100, 50, 50))
    if orcBossSpawn == True:
        screen.blit(bossHealthText, (450, 20))
 
    if showDialogue == True and gameBegin == True:
            screen.blit(DialogueBox, (50, 510))
            currentDialogue = message
            textSurface = gameFont.render(currentDialogue, True, (255, 255, 255))
            screen.blit(textSurface, (80, 535))
   
    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS
    screen.fill((0, 0, 0))  # Fill the screen with black


pygame.quit()