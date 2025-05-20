# Este código lê QR Codes usando a webcam e imprime os dados no console.

# importando as bibliotecas necessárias
import cv2
from pyzbar.pyzbar import decode

# Inicializando a captura de vídeo (liga a camera)
cap = cv2.VideoCapture(0)

# Instrução para o usuário saber como sair do programa
print("Pressione 'q' para sair.")

# Loop para capturar os frames da câmera
# e decodificar os QR Codes
while True:
    # Captura um frame da câmera
    # e verifica se a captura foi bem-sucedida
    ret, frame = cap.read()
    if not ret:
        break
    
    # Decodifica os QR Codes presentes no frame
    codes = decode(frame)
    
    # Para cada QR Code detectado, imprime os dados
    # e desenha um retângulo ao redor do QR Code
    for code in codes:
        data = code.data.decode('utf-8')
        if data.isnumeric():
            print(f"QR Code detectado: {data}")
            pts = code.polygon
            if len(pts) == 4:
                pts = [(pt.x, pt.y) for pt in pts]
                for i in range(4):
                    cv2.line(frame, pts[i], pts[(i+1) % 4], (0, 255, 0), 2)
            cv2.putText(frame, data, (code.rect.left, code.rect.top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow("Leitor de QR Code", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# Este código lê QR Codes usando a webcam e imprime os dados no console.
# Ele também desenha um retângulo ao redor do QR Code detectado.