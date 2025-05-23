# 📷 Leitor de QR Code com Python

Este projeto é um **leitor de QR Code em tempo real**, desenvolvido em Python, que utiliza a webcam do computador para capturar imagens e identificar QR Codes. Ele imprime os dados no console e destaca os QR Codes detectados com um retângulo verde na tela.

## 🧰 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [OpenCV](https://opencv.org/) (`cv2`)
- [pyzbar](https://pypi.org/project/pyzbar/)

## 🚀 Como Usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/leitor-qrcode-python.git
cd leitor-qrcode-python
```

### 2. Instale as dependências

Recomenda-se o uso de um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Se não tiver o requiriments.txt, instale manualmente.**

```bash
pip install opencv-python pyzbar
```

**Obs: O pyzbar pode exigir a instalação da biblioteca zbar no sistema. No Ubuntu/Debian, use:**

```bash
sudo apt install libzbar0
```

### 3. Execute o script

```bash
python leitor_qrcode.py
```

A webcam será ativada e o programa começará a ler QR Codes.

## 🎯 Funcionalidades
- Leitura de QR Codes numéricos usando a webcam.
- Impressão dos dados no terminal.
- Retângulo verde ao redor do QR Code detectado.
- Saída rápida pressionando a tecla q.

## ✍️ Autor

Este projeto foi desenvolvido por **Daniel Santos**, com apoio do **ChatGPT**, utilizando técnicas de **engenharia de prompt** para otimizar o desenvolvimento e a organização do código e da documentação.

Sinta-se à vontade para contribuir ou enviar sugestões!
