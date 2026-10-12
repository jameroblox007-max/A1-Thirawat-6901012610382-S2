float playerX = 300;
float fruitX = 0;
float fruitY = 0;
int score = 0;
int life = 3;
float speed = 8;
int lastIncrease = 0;
float healfruitX = 0;
float healfruitY = -1000;
boolean healActive = false;

void resetFruit() {
  fruitX = random(30, 1250);
  fruitY = 0;
}

void spawnHealFruit() {
  healfruitX = random(30, 1250);
  healActive = true;
  healfruitY = -3250;
}

void removeHealFruit() {
  healfruitY = -1000;
  healActive = false;
}

void setup() {
  size(1280, 720);
  textAlign(CENTER);
  textSize(20);
  resetFruit();
}

void draw() {
  background(240);

  if (score - lastIncrease >= 10) {
    speed += 2;
    lastIncrease = score;
  }

  playerX = mouseX;
  fill(0, 0, 255);
  rect(playerX - 40, 700, 80, 20);

  fill(255, 0, 0);
  ellipse(fruitX, fruitY, 30, 30);
  fruitY += speed;

  if (healActive) {
    fill(0, 255, 200);
    ellipse(healfruitX, healfruitY, 30, 30);
    healfruitY += speed;
  }

  if (fruitY >= 690 && abs(playerX - fruitX) < 60) {
    score++;
    resetFruit();
    if (!healActive && int(random(1, 26)) == 1) {  // โอกาส 4%
      spawnHealFruit();
    }
  } else if (fruitY > 720) {
    life--;
    resetFruit();
  }

  if (healActive && healfruitY >= 690 && abs(playerX - healfruitX) < 60) {
    if (life < 3) {
      life++;
    }
    removeHealFruit();
  }

  if (healActive && healfruitY > 720) {
    removeHealFruit();
  }

  fill(0);
  textAlign(LEFT);
  text("Score : " + score, 20, 30);
  textAlign(RIGHT);
  text("Life : " + life, 1260, 30);

  if (life <= 0) {
    background(0);
    fill(255);
    textAlign(CENTER);
    textSize(40);
    text("GAME OVER", width/2, height/2 - 20);
    textSize(20);
    text("Score : " + score, width/2, height/2 + 20);
    noLoop();
  }
}
