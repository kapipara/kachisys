/* サーボ群のピン設定 */
const int sv1 = 33;   /* 黒板 */
const int sv2 = 25;   /* 真ん中 */
const int sv3 = 26;   /* 廊下側 */
const int sv4 = 27;   /* 窓側 */

/* サーボの回転角設定 */
const int sv1_ON  = 60;
const int sv1_OFF = 170;
const int sv1_nomal = (sv1_ON + sv1_OFF) / 2;
const int sv2_ON  = 40;
const int sv2_OFF = 110;
const int sv2_nomal = (sv2_ON + sv2_OFF) / 2;
const int sv3_ON  = 120;
const int sv3_OFF = 30;
const int sv3_nomal = (sv3_ON + sv3_OFF) / 2;
const int sv4_ON  = 110;
const int sv4_OFF = 30;
const int sv4_nomal = (sv4_ON + sv4_OFF) / 2;

/* 全消しスイッチのピン設定 */
const int sw = 32;

uint32_t servoDegreeToDuty(double degree);  /* ぐり作デューティ比変換関数 */
void svRotate(int svNum, bool cond);        /* サーボ操作関数 */

void setup(){
  /* サーボ周りのセットアップ */
  ledcSetup(0,50,16); // 0 channel, 50 Hz, 16 bit
  ledcSetup(1,50,16);
  ledcSetup(2,50,16);
  ledcSetup(3,50,16);
  ledcAttachPin(sv1,0);
  ledcAttachPin(sv2,1);
  ledcAttachPin(sv3,2);
  ledcAttachPin(sv4,3);
  ledcWrite(0,servoDegreeToDuty(sv1_nomal));
  ledcWrite(1,servoDegreeToDuty(sv2_nomal));
  ledcWrite(2,servoDegreeToDuty(sv3_nomal));
  ledcWrite(3,servoDegreeToDuty(sv4_nomal));

  /* スイッチのセットアップ */
  pinMode(sw, INPUT);
}

void loop(){
  static bool now = 0;
  if(digitalRead(sw)){
    svRotate(5,!now);
    delay(1000);
    now = !now;
  }
}

uint32_t servoDegreeToDuty(double degree){
    if(degree < 0) degree = 0;
    if(degree > 180) degree = 180;
    return (uint32_t)(((degree / 180.0 ) * 0.0928 + 0.0272) * 65536.0);
}

void svRotate(int svNum, bool cond){
  switch(svNum){
    case 1:
      if(cond){
        ledcWrite(0,servoDegreeToDuty(sv1_ON));
        delay(500);
      }else{
        ledcWrite(0,servoDegreeToDuty(sv1_OFF));
        delay(500);
      }
      ledcWrite(0,servoDegreeToDuty(sv1_nomal));
      break;
      
    case 2:
      if(cond){
        ledcWrite(1,servoDegreeToDuty(sv2_ON));
        delay(500);
      }else{
        ledcWrite(1,servoDegreeToDuty(sv2_OFF));
        delay(500);
      }
      ledcWrite(1,servoDegreeToDuty(sv2_nomal));
      break;
      
    case 3:
      if(cond){
        ledcWrite(2,servoDegreeToDuty(sv3_ON));
        delay(500);
      }else{
        ledcWrite(2,servoDegreeToDuty(sv3_OFF));
        delay(500);
      }
      ledcWrite(2,servoDegreeToDuty(sv3_nomal));
      break;
      
    case 4:
      if(cond){
        ledcWrite(3,servoDegreeToDuty(sv4_ON));
        delay(500);
      }else{
        ledcWrite(3,servoDegreeToDuty(sv4_OFF));
        delay(500);
      }
      ledcWrite(3,servoDegreeToDuty(sv4_nomal));
      break;
      
    case 5:
      if(cond){
        ledcWrite(0,servoDegreeToDuty(sv1_ON));
        delay(5);
        ledcWrite(1,servoDegreeToDuty(sv2_ON));
        delay(5);
        ledcWrite(2,servoDegreeToDuty(sv3_ON));
        delay(5);
        ledcWrite(3,servoDegreeToDuty(sv4_ON));
        delay(5);
      }else{
        ledcWrite(0,servoDegreeToDuty(sv1_OFF));
        delay(5);
        ledcWrite(1,servoDegreeToDuty(sv2_OFF));
        delay(5);
        ledcWrite(2,servoDegreeToDuty(sv3_OFF));
        delay(5);
        ledcWrite(3,servoDegreeToDuty(sv4_OFF));
        delay(5);
      }
      delay(500);
      ledcWrite(0,servoDegreeToDuty(sv1_nomal));
      ledcWrite(1,servoDegreeToDuty(sv2_nomal));
      ledcWrite(2,servoDegreeToDuty(sv3_nomal));
      ledcWrite(3,servoDegreeToDuty(sv4_nomal));
      break;
      
    default:
      break;
  }
}
