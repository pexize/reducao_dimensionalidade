from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import BytesIO


def convert_from_url(url):
    """Baixa uma imagem de uma URL, converte para tons de cinza e binariza."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao baixar a imagem: {e}")
        return None, None, None

    try:
        img_color = Image.open(BytesIO(response.content))
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return None, None, None

    # Converter para tons de cinza
    img_gray = img_color.convert('L')
    img_array = np.array(img_gray)

    # Calcular o limiar como a média dos valores de pixel
    threshold = img_array.mean()
    binary_array = np.where(img_array < threshold, 0, 255).astype(np.uint8)

    # Converter o array binarizado para imagem PIL
    img_binary = Image.fromarray(binary_array)

    return img_color, img_gray, img_binary


def display_images(color_image, gray_image, binary_image):
    """Exibe imagens colorida, em tons de cinza e binarizada lado a lado."""
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.title("Original (Colorida)")
    plt.imshow(color_image)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title("Escala de Cinza")
    plt.imshow(gray_image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title("Preto e Branco")
    plt.imshow(binary_image, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()


def main():
    """Função principal para processar e exibir imagens binarizadas."""
    print("=== Conversor de Imagens Online ===")
    
    while True:
        user_url = input("\nDigite a URL da imagem para binarização: ")

        # Valida se é uma URL antes de prosseguir
        if not user_url.startswith(('http://', 'https://')):
            print("Por favor, insira uma URL válida!")
            continue

        img_color, img_gray, img_binary = convert_from_url(user_url)

        if img_color and img_gray and img_binary:
            display_images(img_color, img_gray, img_binary)
            print("Imagem processada com sucesso!")
        else:
            print("Falha no processamento da imagem.")

        # Perguntar se o usuário deseja continuar
        repeat = input("\nDeseja processar outra imagem? (s/n): ").strip().lower()
        if repeat != 's':
            print("Encerrando o programa. Até mais!")
            break


if __name__ == "__main__":
    main()
