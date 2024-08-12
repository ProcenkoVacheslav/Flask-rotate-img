def verify_ext(filename: str) -> bool:
    """Проверяет файл на возможность работать с ним в программе."""

    ext = filename.rsplit('.', 1)[1]
    if ext in ['png', 'jpg']:
        return True
    return False


angles = {
    'left': 90,
    'right': -90,
    'button': 180,
}
