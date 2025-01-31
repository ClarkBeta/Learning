/*
 Name:		流水灯.ino
 Created:	2025/1/26 13:23:33
 Author:	clark
*/

// the setup function runs once when you press reset or power the board
void setup() {
	for (int i = 2;i < 8;i++) {
		pinMode(i, OUTPUT);
	}

}
// the loop function runs over and over again until power down or reset
void loop() {
	for (int i = 2;i < 8;i++) {
		digitalWrite(i, HIGH);
		delay(1000);
		digitalWrite(i, LOW);
	}
	for (int i = 7;i < 2;i--) {
		digitalWrite(i, HIGH);
		delay(1000);
		digitalWrite(i, LOW);
	}
}
