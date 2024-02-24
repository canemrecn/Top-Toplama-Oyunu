import cv2, random, numpy as np, time
WIDTH, HEIGHT = 1000, 600
def generate_ball_position():
    return random.randint(0, WIDTH), random.randint(0, HEIGHT)
def draw_ball(frame, pos):
    cv2.circle(frame, pos, 20, (0, 255, 255), -1)
def on_click(event, x, y, flags, param):
    global ball_pos, score
    if event == cv2.EVENT_LBUTTONDOWN:
        if abs(ball_pos[0] - x) <= 20 and abs(ball_pos[1] - y) <= 20:
            score += 1
            ball_pos = generate_ball_position()
def show_score(score, elapsed_time):
    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    cv2.putText(frame, f'Toplam Skor: {score}', (320, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
    cv2.putText(frame, f'Toplam Sure: {int(elapsed_time)} saniye', (280, 300), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)
    cv2.rectangle(frame, (400, 350), (600, 450), (0, 255, 0), -1)
    cv2.putText(frame, 'Oyun Bitti', (430, 410), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(frame, "Oyunu tekrar baslatmak icin 'r' tusuna basiniz", (250, 500), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(255, 255, 255), 2)
    cv2.imshow('Sari Topu Yakala', frame)
    key = cv2.waitKey(0)
    if key == ord('q'):
        return False
    elif key == ord('r'):
        return True
    return False
def play_game():
    global ball_pos, score
    ball_pos = generate_ball_position()
    score = 0
    start_time = time.time()
    cv2.namedWindow('Sari Topu Yakala')
    cv2.setMouseCallback('Sari Topu Yakala', on_click)
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = max(60 - elapsed_time, 0)
        frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
        draw_ball(frame, ball_pos)
        cv2.putText(frame, f'Skor: {score}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))
        cv2.putText(frame, f'Sure: {remaining_time:.1f}s', (WIDTH - 150, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255, 255, 255))
        cv2.imshow('Sari Topu Yakala', frame)
        if cv2.waitKey(1) == ord('q') or remaining_time == 0:
            break
    result = show_score(score, elapsed_time)
    return result
while True:
    if not play_game():
        break
cv2.destroyAllWindows()
#İlk olarak, cv2, random, numpy, ve time kütüphaneleri import edilir.
#WIDTH ve HEIGHT sabitleri belirlenir ve oyunun ekran boyutunu temsil eder.
#generate_ball_position() fonksiyonu, topun rastgele bir konumda oluşturulmasını sağlar.
#draw_ball(frame, pos) fonksiyonu, belirtilen konumda bir daire çizer.
#on_click(event, x, y, flags, param) fonksiyonu, fare tıklaması olayını işler. Eğer tıklama
# topun içine denk geliyorsa, skoru artırır ve topun konumunu günceller.
#show_score(score, elapsed_time) fonksiyonu, oyunun sonunda skor tablosunu ekranda gösterir.
# Ayrıca, oyunun tekrar başlatılması için "r" tuşuna basılmasını bekler.
#play_game() fonksiyonu, oyunun ana işleyişini sağlar. Topun konumunu ve skoru sıfırlar,
# süreyi başlatır ve fare tıklama olaylarını takip eder. Oyun süresi sona erdiğinde veya "q"
# tuşuna basıldığında döngüden çıkar.
#Sonsuz bir döngü içinde play_game() fonksiyonu çağırılır ve oyunun tekrar başlatılıp
# başlatılmayacağı kontrol edilir.
#Oyun tamamen sona erdiğinde, pencereler kapatılır ve program sonlanır.
