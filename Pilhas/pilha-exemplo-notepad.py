import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pilha import Pilha

class SimpleNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Simples Bloco de Notas")
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.create_menu()

        self.undo_stack = Pilha()  # Pilha para desfazer
        self.redo_stack = Pilha()  # Pilha para refazer

        # Monitorar cada tecla pressionada para salvar o estado do texto
        self.text_area.bind("<Key>", self.save_undo_state)

    def create_menu(self):
        # Configuração do menu
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Adiciona o menu Arquivo
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Salvar", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.root.quit)
        self.menu_bar.add_cascade(label="Arquivo", menu=file_menu)

        # Adiciona o menu Editar
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(label="Desfazer", command=self.undo)
        edit_menu.add_command(label="Refazer", command=self.redo)
        self.menu_bar.add_cascade(label="Editar", menu=edit_menu)

    def save_undo_state(self, event=None):
        # Salva o estado atual do texto na pilha de desfazer, usando push
        current_text = self.text_area.get("1.0", tk.END)
        self.undo_stack.push(current_text)

    def open_file(self):
        # Limpando as pilhas ao abrir um arquivo
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
                self.undo_stack.clear()
                self.redo_stack.clear()

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def undo(self):
        if not self.undo_stack.is_empty():
            current_text = self.text_area.get("1.0", tk.END)
            self.redo_stack.push(current_text)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", self.undo_stack.pop())
            if self.undo_stack.is_empty():
                self.text_area.delete("1.0", tk.END)

    def redo(self):
        if not self.redo_stack.is_empty():
            current_text = self.text_area.get("1.0", tk.END)
            self.undo_stack.push(current_text)
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", self.redo_stack.pop())

if __name__ == "__main__":
    root = tk.Tk()
    SimpleNotepad(root)
    root.mainloop()
