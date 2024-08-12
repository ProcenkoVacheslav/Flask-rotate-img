from PIL import Image

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
)

from app.__init__ import app
from app.settings import angles, verify_ext


@app.route('/')
def index():
    return render_template('index.html', title='главная')


@app.route('/rotate')
def rotate():
    return render_template('rotate_img.html', title='повернуть изображение')


@app.route('/download')
def download():
    filename = f'rotated-{session.get("filename")}'

    return render_template('download_img.html', file=filename, title='скачать изображение')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        img = request.files['img_file']
        img_name = img.filename

        if img and verify_ext(img_name):

            with open(f'app/static/user_imgs/{img_name}', 'wb') as file:
                file.write(img.read())
                session['filename'] = img_name

            flash('Картинка успешно загружена', 'success')
            return redirect(url_for('rotate'))

        flash('Картинка не загружена, попробуйте снова.', 'error')
        return redirect(url_for('index'))


@app.route('/do_rotate/<direction>')
def do_rotate(direction):
    angle = angles.get(direction)

    with Image.open(f'app/static/user_imgs/{session.get("filename")}') as img:
        rotated_img = img.rotate(angle, expand=True)
        rotated_img.save(f'app/static/rotated_imgs/rotated-{session.get("filename")}')

    flash('Картинка успешно изменена.', 'success')
    return redirect(url_for('download'))


if __name__ == "__main__":
    app.run()
