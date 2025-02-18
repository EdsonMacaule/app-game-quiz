import time
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

# Carregar o arquivo do excel
df = pd.read_excel("questions.xlsx")

# Pegar as perguntas aleatoriamente
questions = df.sample(n=10).values.tolist()

# Inicializa uma lista para armazenar as perguntas já feitas
asked_questions = []

def get_random_question():
    global asked_questions

    # Verifica se ainda há perguntas disponíveis
    if len(asked_questions) >= len(questions):
        print("Todas as perguntas já foram feitas.")
        return None  # Retorna None se todas as perguntas já foram feitas
    
    # Escolhe uma pergunta aleatória da lista 'questions'
    question = random.choice(questions)

    # Verifica se a pergunta já foi feita
    while question in asked_questions:
        question = random.choice(questions)
    
    # Adiciona a pergunta à lista de perguntas já feitas
    asked_questions.append(question)

    # Retorna a pergunta e suas opções
    return question  # Retorna a pergunta completa, não precisa desempacotar aqui

# Variáveis globais
score = 0
current_question = 0
time_limit = 10  # Definindo o tempo limite em segundos
timer_running = False

def check_answer(answer):
    global score, current_question
    if answer == correct_answer.get():
        score += 1

    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        show_result()

def display_question():
    global timer_running
    timer_running = True
    question_data = get_random_question()
    
    if question_data:
        # Desempacota a pergunta e suas opções
        question_text, option1, option2, option3, option4, answer, _ = question_data
        question_label.config(text=question_text)
        option1_btn.config(text=option1, state=tk.NORMAL, command=lambda: check_answer(1))
        option2_btn.config(text=option2, state=tk.NORMAL, command=lambda: check_answer(2))
        option3_btn.config(text=option3, state=tk.NORMAL, command=lambda: check_answer(3))
        option4_btn.config(text=option4, state=tk.NORMAL, command=lambda: check_answer(4))

        correct_answer.set(answer)
        
        start_timer()  # Inicia o temporizador

def start_timer():
    global timer_running  # Declare como global para acessar a variável
    remaining_time = time_limit
    timer_label.config(text=f"Tempo restante: {remaining_time} segundos")

    def countdown():
        nonlocal remaining_time
        global timer_running  # Use global para acessar a variável timer_running
        if remaining_time > 0 and timer_running:
            remaining_time -= 1
            timer_label.config(text=f"Tempo restante: {remaining_time} segundos")
            janela.after(1000, countdown)  # Chama a função novamente após 1 segundo
        else:
            timer_running = False
            if remaining_time <= 0:
                messagebox.showwarning("Tempo Esgotado", "⏰ O tempo para responder a pergunta esgotou!")
                check_answer(-1)  # Chama check_answer com valor inválido para indicar um erro

    countdown()  # Inicia a contagem regressiva

def show_result():
    messagebox.showinfo("Quiz Finalizado", f"Parabéns! Você Completou o quiz.\n\nPontuação final: {score}/{len(questions)} ")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)
    play_again_btn.pack()

def play_again():
    global score, current_question, timer_running
    score = 0
    current_question = 0
    asked_questions.clear()  # Limpa as perguntas já feitas
    random.shuffle(questions)
    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)
    play_again_btn.pack_forget()
    timer_running = False
    timer_label.config(text="Tempo restante: 10 segundos")  # Reseta o timer

janela = tk.Tk()
janela.title('Perguntas Evangélicas')
janela.geometry("400x450")

# Definindo as cores
background_color = "#7BC950"
text_color = "#333333"
button_color = "#4CAF50"
button_text_color = "#FFFFFF"

janela.config(bg=background_color)
janela.option_add('#Font', 'Arial')

# Icon na tela
app_icon = PhotoImage(file="logo.png")
app_label = tk.Label(janela, image=app_icon, bg=background_color)
app_label.pack(pady=10)

# Componentes da Interface
question_label = tk.Label(janela, text="", wraplength=380, bg=background_color, fg=text_color, font=("Arial", 12, "bold"))
question_label.pack(pady=20)

correct_answer = tk.IntVar()

option1_btn = tk.Button(janela, text="", width=30, bg=background_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(janela, text="", width=30, bg=background_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(janela, text="", width=30, bg=background_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option3_btn.pack(pady=10)

option4_btn = tk.Button(janela, text="", width=30, bg=background_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option4_btn.pack(pady=10)

timer_label = tk.Label(janela, text=f"Tempo restante: {time_limit} segundos", bg=background_color, fg=text_color, font=("Arial", 12, "bold"))
timer_label.pack(pady=10)

play_again_btn = tk.Button(janela, command=play_again, text="Jogar Novamente", width=30, bg=background_color, fg=button_text_color, font=("Arial", 10, "bold"))

display_question()  # Exibe a primeira pergunta

janela.mainloop()