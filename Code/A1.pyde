playerX = 300
fruitX = 0
fruitY = 0
score = 0
life = 3
speed = 8
lastIncrease = 0
healfruitX = 0
healfruitY = -1000
healActive = False

def resetFruit():
    global fruitX, fruitY
    fruitX = random(30, 1250)
    fruitY = 0

def spawnHealFruit():
    global healfruitX, healfruitY, healActive
    healfruitX = random(30, 1250)
    healActive = True
    healfruitY = -3250

def removeHealFruit():
    global healfruitY, healActive
    healfruitY = -1000
    healActive = False

def setup():
    size(1280, 720)
    textAlign(CENTER)
    textSize(20)
    resetFruit()

def draw():
    global playerX, fruitY, score, life, speed, lastIncrease, healfruitY, healActive

    background(240)

    if score - lastIncrease >= 10:
        speed += 2
        lastIncrease = score

    playerX = mouseX
    fill(0, 0, 255)
    rect(playerX - 40, 700, 80, 20)

    fill(255, 0, 0)
    ellipse(fruitX, fruitY, 30, 30)
    fruitY += speed

    if healActive:
        fill(0, 255, 200)
        ellipse(healfruitX, healfruitY, 30, 30)
        healfruitY += speed

    if fruitY >= 690 and abs(playerX - fruitX) < 60:
        score += 1
        resetFruit()
        if not healActive and int(random(1, 26)) == 1:  # โอกาส 4%
            spawnHealFruit()
    elif fruitY > 720:
        life -= 1
        resetFruit()

    if healActive and healfruitY >= 690 and abs(playerX - healfruitX) < 60:
        if life < 3:
            life += 1
        removeHealFruit()

    if healActive and healfruitY > 720:
        removeHealFruit()

    fill(0)
    textAlign(LEFT)
    text("Score : " + str(score), 20, 30)
    textAlign(RIGHT)
    text("Life : " + str(life), 1260, 30)

    if life <= 0:
        background(0)
        fill(255)
        textAlign(CENTER)
        textSize(40)
        text("GAME OVER", width/2, height/2 - 20)
        textSize(20)
        text("Score : " + str(score), width/2, height/2 + 20)
        noLoop()
