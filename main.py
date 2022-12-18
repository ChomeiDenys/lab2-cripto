from pprint import pprint
import numpy as np

UKR_ALP = [
    'а', 'б', 'в', 'г', 'ґ', 'д', 'е',
    'є', 'ж', 'з', 'и', 'і', 'ї', 'й',
    'к', 'л', 'м', 'н', 'о', 'п', 'р',
    'с', 'т', 'у', 'ф', 'х', 'ц', 'ч',
    'ш', 'щ', 'ь', 'ю', 'я'
]


def find_dims(alphabet):
    max_dim = 100
    for x in range(max_dim):
        for y in range(x + 1):
            if x * y >= len(alphabet):
                return x, y


def create_square(alphabet):
    dim_x, _ = find_dims(alphabet)

    square = np.asarray(create_matrix_the_text(alphabet, dim_x))
    return square


def polyb_squar_encode(alphabet, text_in: str) -> str:
    square = create_square(alphabet)

    rows = []
    cols = []
    for ch in text_in:
        location = np.where(square == ch)
        if location:
            row, col = location[0][0], location[1][0]
            rows.append(row)
            cols.append(col)

    inds = rows + cols
    encoded_text = "".join(square[inds[i], inds[i + 1]] for i in range(0, len(inds), 2))

    return encoded_text


def polyb_squar_decode(alphabet, encoded_text: str) -> str:
    square = create_square(alphabet)

    all_coords = []
    for ch in encoded_text:
        coords = np.where(square == ch)
        if coords:
            all_coords.append((coords[0][0], coords[1][0]))

    half = len(all_coords) // 2
    hor_coords = all_coords[:half]
    vert_coords = all_coords[half:]

    text_out = "".join(square[hor[0], vert[0]] + square[hor[1], vert[1]] for hor, vert in zip(hor_coords, vert_coords))
    return text_out


if __name__ == '__main__':
    pprint("квадрат Полібія")
    text_in = "шифрування"

    pprint(f"Текст, що кодується: {text_in}")
    encod_text = polyb_squar_encode(UKR_ALP, "шифрування")
    pprint(f"кодування: {encod_text}")
    pprint(f"розкодування: {polyb_squar_decode(UKR_ALP, encod_text)}")
