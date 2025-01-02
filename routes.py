from flask import Blueprint, request, render_template, redirect, url_for, flash, session, send_file
import os
import numpy as np
import pandas as pd
from utils import allowed_file, process_file, upload_files, up_file
from user_manager import UserManager

main = Blueprint('main', __name__)

user_manager = UserManager()

# Убедитесь, что директории для загрузок существуют
os.makedirs('uploads', exist_ok=True)
os.makedirs('outputs', exist_ok=True)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if user_manager.validate_user(username, password):
        session['username'] = username
        session['role'] = user_manager.get_user_role(username)
        return redirect(url_for('main.dashboard'))
    else:
        flash("Неверный логин или пароль")
        return redirect(url_for('main.home'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    flash("Регистрация отключена.")
    return redirect(url_for('main.home'))

@main.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        role = session['role']
        return render_template('dashboard.html', username=username, role=role)
    return redirect(url_for('main.home'))

@main.route('/process', methods=['POST'])
def process():
    return process_file(request)

@main.route('/upload', methods=['GET', 'POST'])
def upload_files_route():
    return upload_files(request, session)

@main.route('/up_file', methods=['POST'])
def up_file_route():
    return up_file(request)

@main.route('/logout')
def timeout():
    return render_template('logout.html')

#-----------
@main.route('/create_sectors', methods=['POST'])
def create_sectors():
    save_path = request.form.get('save_path').strip()
    sector_count = int(request.form.get('sector_count', 0))
    sectors = request.form.getlist('sectors')

    for sector in sectors:
        sector = sector.strip()
        if not sector:
            continue

        sector_path = os.path.join(save_path, sector)
        os.makedirs(sector_path, exist_ok=True)

        # Здесь можно добавить логику для создания файлов
        # Например, сохранение Excel файла

    flash("Файлы успешно созданы!")
    return redirect(url_for('main.dashboard'))