int F = 2; // frequency of the signal
int Fs = 500; // sampling frequency
int n = 500; // number of samples
float t; // time instance
int sampling_interval;
byte samples[500]; // to store the samples

void setup() {
  pinMode(10, OUTPUT);

  // for each sample n
  for (int n = 0; n < 500; n++)
  {
    t = (float) n / Fs;
    samples[n] = (byte) (127.0 * sin(2 * 3.14 * t) + 127.0 );
  }
  sampling_interval = 1000000 / (F * n);
  //sampling interval Ts = 1/frequency x number of sample (Ts = 1/Fn or Ts = T/n)x1000000 to convert it in microseconds
}

void loop() {
  for (int j = 0; j < 500; j++) {
    analogWrite(10, samples[j]); // output written to pin 10
    delayMicroseconds(sampling_interval); //time interval
  }
}
