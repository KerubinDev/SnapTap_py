import tkinter as tk
from tkinter import font, messagebox
import json
import os

# Definindo as cores e fontes do Valorant
BACKGROUND_COLOR = "#111111"  # Cor de fundo escura
PRIMARY_COLOR = "#e5004f"  # Vermelho da logo do Valorant
SECONDARY_COLOR = "#1e1e1e"  # Cor dos botões
BUTTON_HOVER_COLOR = "#333333"  # Cor do botão em hover
FONT_COLOR = "#ffffff"  # Cor do texto
FONT_NAME = "Bebas Neue"  # Fonte usada no Valorant

# Função para salvar configurações
def save_settings():
    settings = {
        "bindings": bindings_var.get(),
        "disable_bind": disable_bind_var.get(),
        "esc_bind": esc_bind_var.get()
    }
    with open("settings.json", "w") as f:
        json.dump(settings, f)
    messagebox.showinfo("Configuração", "Configurações salvas com sucesso!")

# Função para carregar configurações
def load_settings():
    if os.path.exists("settings.json"):
        try:
            with open("settings.json", "r") as f:
                settings = json.load(f)
                bindings_var.set(settings.get("bindings", "WASD"))
                disable_bind_var.set(settings.get("disable_bind", "E"))
                esc_bind_var.set(settings.get("esc_bind", "ESC"))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar configurações: {e}")
    else:
        bindings_var.set("WASD")
        disable_bind_var.set("E")
        esc_bind_var.set("ESC")

def on_enter(e):
    e.widget.config(bg=BUTTON_HOVER_COLOR)

def on_leave(e):
    e.widget.config(bg=SECONDARY_COLOR)

def main():
    global bindings_var, disable_bind_var, esc_bind_var

    root = tk.Tk()
    root.title("Snap Tap Code")
    root.geometry("600x400")
    root.configure(bg=BACKGROUND_COLOR)
    
    # Definindo a fonte
    custom_font = font.Font(family=FONT_NAME, size=14)
    
    # Configurando variáveis
    bindings_var = tk.StringVar()
    disable_bind_var = tk.StringVar()
    esc_bind_var = tk.StringVar()

    # Criando o frame principal
    main_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Ajustando o grid para ficar centralizado
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_rowconfigure(1, weight=1)
    main_frame.grid_rowconfigure(2, weight=1)
    main_frame.grid_rowconfigure(3, weight=1)
    main_frame.grid_rowconfigure(4, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)

    # Adicionando uma etiqueta com texto
    label = tk.Label(main_frame, text="Bem-vindo :D", bg=BACKGROUND_COLOR, fg=FONT_COLOR, font=custom_font)
    label.grid(row=0, column=0, columnspan=2, pady=20)

    # Adicionando opções de configuração
    tk.Label(main_frame, text="Bindings", bg=BACKGROUND_COLOR, fg=FONT_COLOR, font=custom_font).grid(row=1, column=0, padx=10, pady=5, sticky="e")
    tk.OptionMenu(main_frame, bindings_var, "WASD", "Arrows", "Custom").grid(row=1, column=1, padx=10, pady=5, sticky="w")

    tk.Label(main_frame, text="Disable Bind Key", bg=BACKGROUND_COLOR, fg=FONT_COLOR, font=custom_font).grid(row=2, column=0, padx=10, pady=5, sticky="e")
    tk.Entry(main_frame, textvariable=disable_bind_var, bg=SECONDARY_COLOR, fg=FONT_COLOR, font=custom_font).grid(row=2, column=1, padx=10, pady=5, sticky="w")

    tk.Label(main_frame, text="ESC Bind Key", bg=BACKGROUND_COLOR, fg=FONT_COLOR, font=custom_font).grid(row=3, column=0, padx=10, pady=5, sticky="e")
    tk.Entry(main_frame, textvariable=esc_bind_var, bg=SECONDARY_COLOR, fg=FONT_COLOR, font=custom_font).grid(row=3, column=1, padx=10, pady=5, sticky="w")

    # Criando e estilizando um botão para salvar configurações
    save_button = tk.Button(main_frame, text="Salvar Configurações", bg=PRIMARY_COLOR, fg=FONT_COLOR, font=custom_font, relief=tk.RAISED, borderwidth=2)
    save_button.grid(row=4, column=0, columnspan=2, pady=20)
    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)
    save_button.config(command=save_settings)
    
    # Carregando configurações
    load_settings()

    # Rodando a aplicação
    root.mainloop()

if __name__ == "__main__":
    main()
